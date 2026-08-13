from __future__ import annotations

from typing import TYPE_CHECKING, Iterator, Optional

from ..Base import AppObject, AppObjectCollection
from ..Proxy import proxy_property, AccessMode
from .AcadMenuGroup import AcadMenuGroup
from ...Types.VarType import vBool

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication


class AcadMenuGroups(AppObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Parent: AppObject = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)

    def Load(self, MenuFileName: str, BaseMenu: Optional[vBool] = None) -> AcadMenuGroup:
        if BaseMenu is None:
            return AcadMenuGroup(self._obj.Load(MenuFileName))
        return AcadMenuGroup(self._obj.Load(MenuFileName, BaseMenu()))

    def Item(self, Index: int | str) -> AcadMenuGroup:
        return AcadMenuGroup(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadMenuGroup]:
        for item in self._obj:
            yield AcadMenuGroup(item)
