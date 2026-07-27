"""
Модуль для автоматических повторных попыток COM-вызовов.

Предоставляет декоратор `retry_com`, который можно применять к методам,
работающим с COM-объектами. При возникновении перехватываемого исключения
(по умолчанию `com_error`) декоратор анализирует HRESULT и повторяет вызов
с экспоненциальной задержкой. Если ошибка указывает на потерю связи
с сервером, и у объекта есть метод `_reconnect_com()`, он будет вызван
для восстановления соединения.
"""

import time
import logging
from functools import wraps
from pywintypes import com_error

# Настройка логгера (по умолчанию ничего не выводит)
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# Часто встречающиеся HRESULT
RPC_E_CALL_REJECTED = -2147418111      # 0x80010101 – вызов отклонён
RPC_E_SERVERFAULT   = -2147418113      # 0x80010103 – сбой сервера
RPC_E_DISCONNECTED  = -2147418109      # 0x80010108 – соединение разорвано
CO_E_OBJNOTCONNECTED = -2147220992     # 0x800401F3 – объект не подключён
RPC_S_SERVER_UNAVAILABLE = -2147023170 # 0x800706BA – сервер недоступен
E_FAIL              = -2147467259      # 0x80004005 – общая ошибка

# Кортежи по умолчанию
DEFAULT_RETRY_HRESULTS = (RPC_E_CALL_REJECTED,)
DEFAULT_RECONNECT_HRESULTS = (
    RPC_E_SERVERFAULT,
    RPC_E_DISCONNECTED,
    CO_E_OBJNOTCONNECTED,
    RPC_S_SERVER_UNAVAILABLE,
    E_FAIL,
)


def retry_com(
    exceptions=(com_error,),
    hresults=DEFAULT_RETRY_HRESULTS,
    reconnect_errors=DEFAULT_RECONNECT_HRESULTS,
    max_attempts=5,
    base_delay=0.5,
    backoff=2.0,
    max_delay=10.0,
):
    """
    Декоратор для повторных попыток выполнения COM-вызова.

    При возникновении перехваченного исключения проверяется его HRESULT:
        - если код в `hresults` – выполняется повторная попытка с задержкой;
        - если код в `reconnect_errors` – вызывается метод переподключения
          (если у объекта есть `_reconnect_com()`), затем выполняется повтор.

    Параметры:
        exceptions (tuple): типы исключений для перехвата (по умолчанию com_error).
        hresults (tuple): коды HRESULT, при которых просто повторяем.
        reconnect_errors (tuple): коды HRESULT, при которых сначала переподключаемся.
        max_attempts (int): максимальное число попыток (включая первую).
        base_delay (float): начальная задержка между попытками (сек).
        backoff (float): множитель для увеличения задержки.
        max_delay (float): максимальная задержка (сек).

    Возвращает:
        обёрнутую функцию, которая будет повторять вызовы при сбоях.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = base_delay
            last_exception = None
            reconnect_func = None

            # Если первый аргумент – self и у него есть метод _reconnect_com
            if args and hasattr(args[0], '_reconnect_com'):
                reconnect_func = args[0]._reconnect_com

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except exceptions as e:
                    last_exception = e
                    should_retry = False
                    should_reconnect = False

                    # Извлекаем HRESULT
                    hr = None
                    if hasattr(e, 'hresult'):
                        hr = e.hresult
                    elif hasattr(e, 'args') and len(e.args) > 0 and isinstance(e.args[0], int):
                        hr = e.args[0]

                    if hr is not None:
                        if hr in hresults:
                            should_retry = True
                        elif hr in reconnect_errors and reconnect_func is not None:
                            should_reconnect = True
                            should_retry = True
                    else:
                        # Если не удалось определить HRESULT, проверяем текст ошибки
                        err_str = str(e).lower()
                        if 'call was rejected' in err_str:
                            should_retry = True
                        elif any(word in err_str for word in ('disconnected', 'invalid class', 'server unavailable')):
                            if reconnect_func is not None:
                                should_reconnect = True
                                should_retry = True

                    if not should_retry or attempt == max_attempts:
                        raise

                    # Переподключение, если необходимо
                    if should_reconnect:
                        logger.warning(
                            f"Потеря связи в '{func.__name__}', переподключение... "
                            f"(попытка {attempt}/{max_attempts})"
                        )
                        try:
                            reconnect_func()
                        except Exception as reconnect_error:
                            logger.error(f"Ошибка переподключения: {reconnect_error}")
                            raise last_exception

                    logger.warning(
                        f"COM-вызов '{func.__name__}' не удался (попытка {attempt}/{max_attempts}). "
                        f"Повтор через {delay:.2f} сек."
                    )
                    time.sleep(delay)
                    delay = min(delay * backoff, max_delay)

            # Если все попытки исчерпаны, пробрасываем последнее исключение
            raise last_exception

        return wrapper
    return decorator