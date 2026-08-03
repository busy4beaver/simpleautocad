from __future__ import annotations

from typing import TYPE_CHECKING

from ..Base import AppObject, AppObjectCollection
from ..Proxy import proxy_property, AccessMode
from .AcadPopupMenu import AcadPopupMenu

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication


class AcadPopupMenus(AppObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Parent: AppObject = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)

    def Add(self, MenuName: str) -> AcadPopupMenu:
        return AcadPopupMenu(self._obj.Add(MenuName))

    def InsertMenuInMenuBar(self, MenuName: str, MenuBarIndex: int | str) -> None:
        self._obj.InsertMenuInMenuBar(MenuName, MenuBarIndex)

    def Item(self, Index: int | str) -> AcadPopupMenu:
        return AcadPopupMenu(self._obj.Item(Index))

    def RemoveMenuFromMenuBar(self, Index: int | str) -> None:
        self._obj.RemoveMenuFromMenuBar(Index)

    def __iter__(self):
        for item in self._obj:
            yield AcadPopupMenu(item)
