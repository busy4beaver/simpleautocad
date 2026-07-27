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


def _is_com_dispatch(obj) -> bool:
    """CDispatch и похожие COM-обёртки win32com (у них часто callable == True)."""
    if isinstance(obj, CDispatch):
        return True
    # dynamic.CDispatch / другие обёртки
    try:
        from win32com.client import DispatchBaseClass
        if isinstance(obj, DispatchBaseClass):
            return True
    except Exception:
        pass
    # У сырого IDispatch часто есть _oleobj_
    if hasattr(obj, '_oleobj_') and not isinstance(obj, type):
        return True
    return False


def _unwrap_com(obj):
    """Достаёт сырой COM-dispatch из AppObject / proxy."""
    seen = set()
    while id(obj) not in seen:
        seen.add(id(obj))
        if isinstance(obj, _RetryComProxy):
            obj = object.__getattribute__(obj, '_com')
            continue
        if isinstance(obj, AppObject):
            obj = object.__getattribute__(obj, '_raw_obj')
            continue
        if hasattr(obj, '_obj') and not _is_com_dispatch(obj):
            try:
                inner = object.__getattribute__(obj, '_obj')
            except Exception:
                break
            if inner is obj:
                break
            obj = inner
            continue
        break
    return obj


class _RetryComProxy:
    """
    Прозрачная обёртка над COM-объектом.

    Цепочки вида:
        app._obj.ActiveDocument.ModelSpace.AddLine(...)
    работают так:
      - свойства, возвращающие COM (ActiveDocument, ModelSpace) →
        новый _RetryComProxy (чтобы цепочка не теряла retry);
      - методы (AddLine, TransformBy) → вызов через execute_com_call;
      - обычные значения (str, int, …) → как есть.

    Важно: CDispatch в win32com часто callable, поэтому нельзя
    решать «метод это или свойство» только через callable().
    """

    __slots__ = ('_com', '_owner')

    def __init__(self, com_obj, owner=None):
        object.__setattr__(self, '_com', com_obj)
        object.__setattr__(self, '_owner', owner)

    def _reconnect_func(self):
        owner = object.__getattribute__(self, '_owner')
        if owner is None:
            return None
        fn = getattr(owner, '_reconnect_com', None)
        return fn if callable(fn) else None

    def _wrap_result(self, result):
        """Если результат — COM-объект, оборачиваем для продолжения цепочки."""
        if result is None or isinstance(result, _RetryComProxy):
            return result
        if _is_com_dispatch(result):
            return _RetryComProxy(result, object.__getattribute__(self, '_owner'))
        return result

    def __getattr__(self, name):
        reconnect = self._reconnect_func()

        def _get():
            com = object.__getattribute__(self, '_com')
            return getattr(com, name)

        attr = execute_com_call(
            _get,
            reconnect_func=reconnect,
            max_attempts=5,
            base_delay=0.25,
        )

        # Свойство вернуло COM-объект (ActiveDocument, ModelSpace, …)
        if _is_com_dispatch(attr):
            return _RetryComProxy(attr, object.__getattribute__(self, '_owner'))

        # Обычное значение (числа, строки, кортежи, …)
        if not callable(attr):
            return attr

        # Настоящий метод COM — при вызове ретраим и заново берём с актуального _com
        def _wrapped(*args, **kwargs):
            def _invoke():
                com = object.__getattribute__(self, '_com')
                method = getattr(com, name)
                return method(*args, **kwargs)

            result = execute_com_call(
                _invoke,
                reconnect_func=self._reconnect_func(),
                max_attempts=5,
                base_delay=0.25,
            )
            return self._wrap_result(result)

        return _wrapped

    def __setattr__(self, name, value):
        if name in ('_com', '_owner'):
            object.__setattr__(self, name, value)
            return

        def _set():
            com = object.__getattribute__(self, '_com')
            setattr(com, name, value)

        execute_com_call(
            _set,
            reconnect_func=self._reconnect_func(),
            max_attempts=5,
            base_delay=0.25,
        )

    def __call__(self):
        return object.__getattribute__(self, '_com')

    def __repr__(self):
        return repr(object.__getattribute__(self, '_com'))

    def __str__(self):
        return str(object.__getattribute__(self, '_com'))

    def __iter__(self):
        com = object.__getattribute__(self, '_com')
        return iter(com)

    def __bool__(self):
        return object.__getattribute__(self, '_com') is not None


class AppObject:
    """
    Базовая обёртка над COM-объектом.

    self._obj — _RetryComProxy: любой вызов self._obj.X() и цепочки
    self._obj.A.B.Method() автоматически ретраятся при занятости сервера.
    Декораторы на каждый метод не нужны.
    """

    def __init__(self, obj):
        raw = _unwrap_com(obj)
        object.__setattr__(self, '_raw_obj', raw)
        object.__setattr__(self, '_obj', _RetryComProxy(raw, self))

    def _set_com_obj(self, com_obj):
        """Обновить COM-указатель (используется при reconnect)."""
        raw = _unwrap_com(com_obj)
        object.__setattr__(self, '_raw_obj', raw)
        proxy = object.__getattribute__(self, '_obj')
        if isinstance(proxy, _RetryComProxy):
            object.__setattr__(proxy, '_com', raw)
        else:
            object.__setattr__(self, '_obj', _RetryComProxy(raw, self))

    def __repr__(self):
        return repr(object.__getattribute__(self, '_raw_obj'))

    def __str__(self):
        return str(object.__getattribute__(self, '_raw_obj'))

    def __call__(self):
        """Вернуть сырой COM-объект (для передачи в другие COM-вызовы)."""
        return object.__getattribute__(self, '_raw_obj')

    def _com_reconnect(self):
        fn = getattr(self, '_reconnect_com', None)
        return fn if callable(fn) else None

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(name)
        return getattr(object.__getattribute__(self, '_obj'), name)


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
