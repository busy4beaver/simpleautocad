from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.VarType import vBool
from .AcadToolbarItem import AcadToolbarItem


class AcadToolbar(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)
    DockStatus = proxy_property('AcToolbarDockStatus', 'DockStatus', AccessMode.ReadOnly)
    FloatingRows = proxy_property(int, 'FloatingRows', AccessMode.ReadWrite)
    Height = proxy_property(int, 'Height', AccessMode.ReadOnly)
    HelpString = proxy_property(str, 'HelpString', AccessMode.ReadWrite)
    LargeButtons = proxy_property(bool, 'LargeButtons', AccessMode.ReadOnly)
    Left = proxy_property(int, 'Left', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Parent = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)
    TagString = proxy_property(str, 'TagString', AccessMode.ReadOnly)
    Top = proxy_property(int, 'Top', AccessMode.ReadWrite)
    Visible = proxy_property(bool, 'Visible', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadOnly)

    def AddSeparator(self, Index: int | str) -> AcadToolbarItem:
        return AcadToolbarItem(self._obj.AddSeparator(Index))

    def AddToolbarButton(
        self,
        Index: int | str,
        Name: str,
        HelpString: str,
        Macro: str,
        FlyoutButton: vBool = None,
    ) -> AcadToolbarItem:
        if FlyoutButton is None:
            return AcadToolbarItem(
                self._obj.AddToolbarButton(Index, Name, HelpString, Macro)
            )
        return AcadToolbarItem(
            self._obj.AddToolbarButton(Index, Name, HelpString, Macro, FlyoutButton())
        )

    def Delete(self) -> None:
        self._obj.Delete()

    def Dock(self, Side) -> None:
        self._obj.Dock(Side)

    def Float(self, Top: int, Left: int, NumberFloatRows: int) -> None:
        self._obj.Float(Top, Left, NumberFloatRows)

    def Item(self, Index: int | str) -> AcadObject:
        return AcadObject(self._obj.Item(Index))
