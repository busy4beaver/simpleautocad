from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPopupMenuItem(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Caption: str = proxy_property(str, 'Caption', AccessMode.ReadOnly)
    Check: bool = proxy_property(bool, 'Check', AccessMode.ReadWrite)
    Enable: bool = proxy_property(bool, 'Enable', AccessMode.ReadWrite)
    EndSubMenuLevel: int = proxy_property(int, 'EndSubMenuLevel', AccessMode.ReadWrite)
    HelpString: str = proxy_property(str, 'HelpString', AccessMode.ReadWrite)
    Index: str = proxy_property(str, 'Index', AccessMode.ReadOnly)
    Label: str = proxy_property(str, 'Label', AccessMode.ReadWrite)
    Parent: AppObject = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)
    SubMenu: AcadPopupMenu = proxy_property('AcadPopupMenu', 'SubMenu', AccessMode.ReadOnly)
    TagString: str = proxy_property(str, 'TagString', AccessMode.ReadWrite)
    Type: AcMenuItemType = proxy_property('AcMenuItemType', 'Type', AccessMode.ReadOnly)

    def Delete(self) -> None:
        self._obj.Delete()
