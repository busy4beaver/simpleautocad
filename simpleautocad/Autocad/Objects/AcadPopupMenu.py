from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from .AcadPopupMenuItem import AcadPopupMenuItem


class AcadPopupMenu(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    NameNoMnemonic = proxy_property(str, 'NameNoMnemonic', AccessMode.ReadOnly)
    OnMenuBar = proxy_property(bool, 'OnMenuBar', AccessMode.ReadOnly)
    Parent = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)
    ShortcutMenu = proxy_property(bool, 'ShortcutMenu', AccessMode.ReadWrite)
    TagString = proxy_property(str, 'TagString', AccessMode.ReadOnly)

    def AddMenuItem(self, Index: int | str, Label: str, Macro: str) -> AcadPopupMenuItem:
        return AcadPopupMenuItem(self._obj.AddMenuItem(Index, Label, Macro))

    def AddSeparator(self, Index: int | str) -> AcadPopupMenuItem:
        return AcadPopupMenuItem(self._obj.AddSeparator(Index))

    def AddSubMenu(self, Index: int | str, Label: str) -> 'AcadPopupMenu':
        return AcadPopupMenu(self._obj.AddSubMenu(Index, Label))

    def InsertInMenuBar(self, Index: int | str) -> None:
        self._obj.InsertInMenuBar(Index)

    def Item(self, Index: int | str) -> 'AcadPopupMenu':
        return AcadPopupMenu(self._obj.Item(Index))

    def RemoveMenuFromMenuBar(self, Index: int) -> None:
        self._obj.RemoveMenuFromMenuBar(Index)
