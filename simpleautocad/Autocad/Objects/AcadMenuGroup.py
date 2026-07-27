from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadMenuGroup(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    MenuFileName = proxy_property(str, 'MenuFileName', AccessMode.ReadOnly)
    Menus = proxy_property('AcadPopupMenus', 'Menus', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Parent = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)
    Toolbars = proxy_property('AcadToolbars', 'Toolbars', AccessMode.ReadOnly)
    Type = proxy_property('AcMenuGroupType', 'Type', AccessMode.ReadOnly)

    def Save(self, MenuFileType) -> None:
        self._obj.Save(MenuFileType)

    def SaveAs(self, MenuFileName: str, MenuFileType) -> None:
        self._obj.SaveAs(MenuFileName, MenuFileType)

    def Unload(self) -> None:
        self._obj.Unload()
