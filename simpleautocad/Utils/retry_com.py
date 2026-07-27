"""
Модуль для автоматических повторных попыток COM-вызовов.

Предоставляет:
  - execute_com_call()  — низкоуровневый вызов с retry/reconnect
  - retry_com()         — декоратор для методов

При RPC_E_CALL_REJECTED (сервер занят) — только повтор с backoff.
При потере связи (disconnected / server unavailable) — если передан
reconnect_func, вызывается он, затем повтор.
"""

from __future__ import annotations

import time
import logging
from functools import wraps
from typing import Any, Callable, Optional, Sequence, Tuple, Type

from pywintypes import com_error

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# HRESULT-коды (отрицательные signed 32-bit)
RPC_E_CALL_REJECTED = -2147418111       # 0x80010101 — вызов отклонён (занят)
RPC_E_SERVERFAULT = -2147418113         # 0x80010103 — сбой сервера
RPC_E_DISCONNECTED = -2147418109        # 0x80010108 — соединение разорвано
CO_E_OBJNOTCONNECTED = -2147220995      # 0x800401FD — объект не подключён
RPC_S_SERVER_UNAVAILABLE = -2147023174  # 0x800706BA — сервер недоступен
RPC_E_INVALID_OBJECT = -2147418110      # 0x80010107

# Занят / временный отказ — только retry, без reconnect
DEFAULT_RETRY_HRESULTS: Tuple[int, ...] = (
    RPC_E_CALL_REJECTED,
)

# Потеря связи — reconnect (если есть) + retry
DEFAULT_RECONNECT_HRESULTS: Tuple[int, ...] = (
    RPC_E_SERVERFAULT,
    RPC_E_DISCONNECTED,
    CO_E_OBJNOTCONNECTED,
    RPC_S_SERVER_UNAVAILABLE,
    RPC_E_INVALID_OBJECT,
)

_BUSY_HINTS = (
    "call was rejected",
    "rejected by callee",
    "server is busy",
    "rpc_e_call_rejected",
)
_DISCONNECT_HINTS = (
    "disconnected",
    "server unavailable",
    "rpc server is unavailable",
    "the rpc server is unavailable",
    "object is not connected",
    "invalid class string",
    "catastrophic failure",
)


def _extract_hresult(exc: BaseException) -> Optional[int]:
    if hasattr(exc, "hresult") and isinstance(exc.hresult, int):
        return int(exc.hresult)
    args = getattr(exc, "args", ())
    if args and isinstance(args[0], int):
        return int(args[0])
    # Иногда HRESULT лежит во вложенном исключении
    if args and isinstance(args[0], BaseException):
        return _extract_hresult(args[0])
    return None


def _classify_error(
    exc: BaseException,
    retry_hrs: Sequence[int],
    reconnect_hrs: Sequence[int],
) -> Tuple[bool, bool]:
    """Возвращает (should_retry, should_reconnect)."""
    hr = _extract_hresult(exc)
    if hr is not None:
        if hr in retry_hrs:
            return True, False
        if hr in reconnect_hrs:
            return True, True
        # Неизвестный HRESULT — не ретраим автоматически
        return False, False

    err = str(exc).lower()
    if any(h in err for h in _BUSY_HINTS):
        return True, False
    if any(h in err for h in _DISCONNECT_HINTS):
        return True, True
    return False, False


def execute_com_call(
    func: Callable[..., Any],
    *args: Any,
    reconnect_func: Optional[Callable[[], Any]] = None,
    exceptions: Tuple[Type[BaseException], ...] = (com_error,),
    hresults: Sequence[int] = DEFAULT_RETRY_HRESULTS,
    reconnect_errors: Sequence[int] = DEFAULT_RECONNECT_HRESULTS,
    max_attempts: int = 5,
    base_delay: float = 0.3,
    backoff: float = 1.8,
    max_delay: float = 8.0,
    **kwargs: Any,
) -> Any:
    """
    Выполняет COM-вызов с повторными попытками.

    - RPC_E_CALL_REJECTED / «занят» → sleep + retry
    - disconnect-коды + reconnect_func → reconnect, затем retry
    - иначе пробрасывает исключение
    """
    delay = base_delay
    last_exception: Optional[BaseException] = None
    func_name = getattr(func, "__name__", repr(func))

    for attempt in range(1, max_attempts + 1):
        try:
            return func(*args, **kwargs)
        except exceptions as e:
            last_exception = e
            should_retry, should_reconnect = _classify_error(e, hresults, reconnect_errors)

            if not should_retry or attempt >= max_attempts:
                raise

            if should_reconnect and reconnect_func is not None:
                logger.warning(
                    "Потеря связи в '%s' (попытка %s/%s), переподключение...",
                    func_name,
                    attempt,
                    max_attempts,
                )
                try:
                    reconnect_func()
                except Exception as reconnect_error:
                    logger.error("Ошибка переподключения: %s", reconnect_error)
                    raise last_exception from reconnect_error

            logger.warning(
                "COM-вызов '%s' не удался (попытка %s/%s). Повтор через %.2f с. [%s]",
                func_name,
                attempt,
                max_attempts,
                delay,
                e,
            )
            time.sleep(delay)
            delay = min(delay * backoff, max_delay)

    assert last_exception is not None
    raise last_exception


def retry_com(
    exceptions: Tuple[Type[BaseException], ...] = (com_error,),
    hresults: Sequence[int] = DEFAULT_RETRY_HRESULTS,
    reconnect_errors: Sequence[int] = DEFAULT_RECONNECT_HRESULTS,
    max_attempts: int = 5,
    base_delay: float = 0.3,
    backoff: float = 1.8,
    max_delay: float = 8.0,
):
    """
    Декоратор для методов, работающих с COM.

    Если у self есть _reconnect_com(), при disconnect-ошибках он будет вызван.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            reconnect_func = None
            if args and hasattr(args[0], "_reconnect_com"):
                reconnect_func = args[0]._reconnect_com

            return execute_com_call(
                func,
                *args,
                reconnect_func=reconnect_func,
                exceptions=exceptions,
                hresults=hresults,
                reconnect_errors=reconnect_errors,
                max_attempts=max_attempts,
                base_delay=base_delay,
                backoff=backoff,
                max_delay=max_delay,
                **kwargs,
            )

        return wrapper

    return decorator
