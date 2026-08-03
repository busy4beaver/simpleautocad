"""
proxy_property и AccessMode — без импорта Object/Entity классов.

Типы по строковому имени ('AcadDocument', 'PyGePoint3d', …)
резолвятся лениво при первом обращении к свойству.
Это разрывает цикл: Entity → Proxy → Entity.

Для IDE: аннотации вида
    ActiveDocument: AcadDocument = proxy_property('AcadDocument', ...)
работают при наличии TYPE_CHECKING-импортов в модуле-владельце.
"""
from __future__ import annotations

import importlib
import sys
from enum import IntEnum
from typing import Any, Optional, TypeVar, Generic, overload, Type

from ..Utils.retry_com import execute_com_call


class AccessMode(IntEnum):
    ReadWrite = 0
    ReadOnly = 1
    WriteOnly = 2
    DenyFromAll = 3


_TYPE_CACHE: dict[str, Any] = {}

# Модули, где обычно лежат обёртки / enum / геометрия
_TYPE_MODULES = (
    'simpleautocad.Types.VarType',
    'simpleautocad.Types.Ac',
    'simpleautocad.Types.Xdata',
    'simpleautocad.Types.Ge',
    'simpleautocad.Types.Ge.Points',
    'simpleautocad.Types.Ge.Vector',
    'simpleautocad.Types.Ge.Matrix',
    'simpleautocad.Types',
    'simpleautocad.Autocad.Base',
    'simpleautocad.Autocad.AcadObject',
    'simpleautocad.Autocad.AcadEntity',
)


def resolve_type(name: str) -> Any:
    """Находит класс/тип по имени без циклических импортов Proxy."""
    if name in _TYPE_CACHE:
        return _TYPE_CACHE[name]

    builtins_map = {'int': int, 'float': float, 'str': str, 'bool': bool, 'tuple': tuple, 'list': list}
    if name in builtins_map:
        _TYPE_CACHE[name] = builtins_map[name]
        return builtins_map[name]

    # Уже загруженные модули пакета
    for mod_name, mod in list(sys.modules.items()):
        if mod is None or not str(mod_name).startswith('simpleautocad'):
            continue
        obj = getattr(mod, name, None)
        if obj is not None and (isinstance(obj, type) or callable(obj)):
            _TYPE_CACHE[name] = obj
            return obj

    candidates: list[str] = []
    if name.startswith('Acad') or name.startswith('IAcad'):
        candidates.extend((
            f'simpleautocad.Autocad.Objects.{name}',
            f'simpleautocad.Autocad.Entities.{name}',
        ))
    candidates.extend(_TYPE_MODULES)

    for path in candidates:
        try:
            mod = importlib.import_module(path)
        except Exception:
            continue
        obj = getattr(mod, name, None)
        if obj is not None:
            _TYPE_CACHE[name] = obj
            return obj

    raise NameError(f"Тип '{name}' не найден.")


def _unwrap_for_com(value: Any) -> Any:
    """AppObject / Variant / proxy → значение, пригодное для setattr COM."""
    if value is None or isinstance(value, (bool, int, float, str, bytes)):
        return value
    # AppObject: __call__ → _raw_obj
    if hasattr(value, '_raw_obj') and callable(value):
        try:
            return value()
        except Exception:
            pass
    # Variant: to_variant / __call__
    if hasattr(value, 'to_variant') and callable(value):
        try:
            return value()
        except Exception:
            pass
    # _RetryComProxy
    if type(value).__name__ == '_RetryComProxy':
        try:
            return object.__getattribute__(value, '_com')
        except Exception:
            pass
    return value


T = TypeVar('T')


class proxy_property(Generic[T]):
    """Дескриптор свойства COM с retry и ленивым приведением типа.

    Использование с аннотацией (рекомендуется)::

        ActiveDocument: AcadDocument = proxy_property(
            'AcadDocument', 'ActiveDocument', AccessMode.ReadOnly
        )

    Для IDE-цепочек (AutoCAD().ActiveDocument.ModelSpace) в модуле
    нужны TYPE_CHECKING-импорты соответствующих типов.
    """

    def __init__(self, rettype: Any, propertyName: str, mode: AccessMode):
        self.rettype_name: Optional[str] = rettype if isinstance(rettype, str) else None
        self.rettype = rettype
        self.propertyName = propertyName
        self.mode = mode

    def _reconnect_of(self, instance):
        fn = getattr(instance, '_reconnect_com', None)
        return fn if callable(fn) else None

    def _target_type(self, owner):
        if self.rettype_name:
            try:
                return resolve_type(self.rettype_name)
            except NameError:
                # fallback: атрибут класса-владельца
                return getattr(owner, self.rettype_name, None)
        return self.rettype

    @overload
    def __get__(self, instance: None, owner: type | None = None) -> proxy_property[T]: ...

    @overload
    def __get__(self, instance: object, owner: type | None = None) -> T: ...

    def __get__(self, instance, owner=None) -> Any:
        if self.mode is AccessMode.WriteOnly:
            raise Exception(f"Свойство '{self.propertyName}' доступно только для записи.")
        if self.mode is AccessMode.DenyFromAll:
            raise Exception(f"Свойство '{self.propertyName}' недоступно для чтения/записи.")
        if instance is None:
            return self

        value = execute_com_call(
            getattr,
            instance._obj,
            self.propertyName,
            reconnect_func=self._reconnect_of(instance),
            max_attempts=5,
            base_delay=0.25,
        )

        target_type = self._target_type(owner)
        if not target_type or target_type in (int, float, str, bool, type(None)):
            return value
        try:
            return target_type(value)
        except Exception:
            return value

    def __set__(self, instance, value: T) -> None:
        if self.mode is AccessMode.ReadOnly:
            raise AttributeError(f"Свойство '{self.propertyName}' доступно только для чтения.")
        if self.mode is AccessMode.DenyFromAll:
            raise Exception(f"Свойство '{self.propertyName}' недоступно для чтения/записи.")

        value = _unwrap_for_com(value)
        try:
            execute_com_call(
                setattr,
                instance._obj,
                self.propertyName,
                value,
                reconnect_func=self._reconnect_of(instance),
                max_attempts=5,
                base_delay=0.25,
            )
        except AttributeError:
            raise AttributeError(
                f"Невозможно установить свойство '{self.propertyName}' в базовом объекте."
            ) from None
