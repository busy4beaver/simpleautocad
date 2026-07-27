from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from .AcadPopupMenu import AcadPopupMenu


class AcadPopupMenus(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Parent = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)

    def Add(self, Name: str) -> AcadPopupMenu:
        return AcadPopupMenu(self._obj.Add(Name))

    def InsertMenuInMenuBar(self, MenuName: str, Index: int) -> None:
        self._obj.InsertMenuInMenuBar(MenuName, Index)

    def Item(self, Index: int) -> AcadPopupMenu:
        return AcadPopupMenu(self._obj.Item(Index))

    def RemoveMenuFromMenuBar(self, Index: int) -> None:
        self._obj.RemoveMenuFromMenuBar(Index)

    def __iter__(self):
        for item in self._obj:
            yield AcadPopupMenu(item)
