from win32com.client import GetActiveObject as AppAttach, Dispatch as AppCreate, CDispatch
from winreg import CloseKey, OpenKey, QueryValueEx, HKEY_CLASSES_ROOT
from pythoncom import CoInitialize, CoUninitialize, CoCreateInstance, CLSCTX_LOCAL_SERVER, IID_IDispatch, com_error
from abc import ABC, abstractmethod
from functools import wraps

from ..Utils.retry_com import execute_com_call


def com_server_is_running(prog_id: str):
    try:
        return AppAttach(prog_id)
    except com_error:
        return False


def get_clsid(cls):
    if cls.__app_version__:
        curver = f'{cls.__app_name__}.Application.{cls.__app_version__}'
        registry_path_clsid = r"{}\CLSID".format(curver)
    else:
        registry_path_clsid = r"{}.Application\CLSID".format(cls.__app_name__)
        registry_path_curver = r"{}.Application\CurVer".format(cls.__app_name__)
    try:
        key = OpenKey(HKEY_CLASSES_ROOT, registry_path_clsid)
        clsid = QueryValueEx(key, None)[0]
        CloseKey(key)
        if not cls.__app_version__:
            key = OpenKey(HKEY_CLASSES_ROOT, registry_path_curver)
            curver = QueryValueEx(key, None)[0]
            CloseKey(key)
            try:
                cls.__app_version__ = str(curver).split('.')[2]
            except Exception:
                pass
        return clsid, curver
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Ключ реестра '{registry_path_clsid}' не найден. "
            f"Приложение не установлено или COM не зарегистрирован."
        )
    except Exception as e:
        raise Exception(f"Произошла ошибка при чтении реестра: {e}") from e


def create_new_instance_explicitly(clsid):
    """Создаёт новый COM-экземпляр по CLSID (не ProgID)."""
    try:
        obj = CoCreateInstance(
            clsid,
            None,
            CLSCTX_LOCAL_SERVER,
            IID_IDispatch,
        )
        app = AppCreate(obj)
        return app
    except com_error as e:
        raise com_error(f"Ошибка COM при создании экземпляра приложения: {e}") from e


class AppObject:
    """
    Базовая обёртка над COM-объектом.

    Все обращения к методам self._obj автоматически проходят через
    retry (занятость сервера / кратковременные сбои).
    Если у экземпляра есть _reconnect_com — он используется при disconnect.
    """

    def __init__(self, obj):
        if not isinstance(obj, CDispatch):
            obj = obj._obj
        self._obj = obj

    def __repr__(self):
        return repr(self._obj)

    def __str__(self):
        return f'{self._obj}'

    def __call__(self):
        return self._obj

    def _com_reconnect(self):
        """Возвращает callable для reconnect, если он есть."""
        fn = getattr(self, '_reconnect_com', None)
        return fn if callable(fn) else None

    def _com_getattr(self, name: str):
        return execute_com_call(
            getattr,
            self._obj,
            name,
            reconnect_func=self._com_reconnect(),
            max_attempts=5,
            base_delay=0.25,
        )

    def _com_setattr(self, name: str, value):
        return execute_com_call(
            setattr,
            self._obj,
            name,
            value,
            reconnect_func=self._com_reconnect(),
            max_attempts=5,
            base_delay=0.25,
        )

    def _com_call(self, method_name: str, *args, **kwargs):
        method = self._com_getattr(method_name)
        return execute_com_call(
            method,
            *args,
            reconnect_func=self._com_reconnect(),
            max_attempts=5,
            base_delay=0.25,
            **kwargs,
        )

    def __getattr__(self, name):
        # Не перехватывать служебные атрибуты
        if name.startswith('_'):
            raise AttributeError(name)

        attr = self._com_getattr(name)

        # Методы COM — оборачиваем в retry при каждом вызове
        if callable(attr):
            reconnect = self._com_reconnect()

            @wraps(attr)
            def _wrapped(*args, **kwargs):
                return execute_com_call(
                    attr,
                    *args,
                    reconnect_func=reconnect,
                    max_attempts=5,
                    base_delay=0.25,
                    **kwargs,
                )

            return _wrapped

        return attr


class Application(ABC):
    def __new__(cls, dispatch_object: CDispatch = None):
        instance = super().__new__(cls)
        instance._dispatch_obj_to_init = None
        instance._is_owner = False
        instance.__app_clsid__ = None
        instance.__app_full_name__ = None
        if dispatch_object is not None:
            instance._dispatch_obj_to_init = dispatch_object
        else:
            try:
                instance._dispatch_obj_to_init = instance._manage_application_instance()
            except Exception as e:
                raise Exception(f"Ошибка запуска приложения: {e}") from e
        return instance

    def __init__(self, dispatch_object=None):
        super().__init__(self._dispatch_obj_to_init)
        del self._dispatch_obj_to_init

    @abstractmethod
    def _manage_application_instance(self):
        ...


class AppObjectCollection(AppObject):
    def __init__(self, obj):
        super().__init__(obj)

    @property
    def Count(self) -> int:
        return self._obj.Count

    def Item(self, Index: int | str) -> AppObject:
        return AppObject(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AppObject(item)


def clear_com_cache():
    import win32com.client.gencache
    import os
    import shutil

    gentype_path = win32com.client.gencache.GetGeneratePath()
    if os.path.exists(gentype_path):
        try:
            shutil.rmtree(gentype_path)
        except OSError as e:
            raise com_error(
                f"Ошибка при удалении кэша: {e}. "
                f"Закройте приложение COM-сервер и повторите попытку."
            ) from e
