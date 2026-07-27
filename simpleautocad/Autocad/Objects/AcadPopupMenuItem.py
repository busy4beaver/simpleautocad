from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPopupMenuItem(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Caption = proxy_property(str, 'Caption', AccessMode.ReadOnly)
    Check = proxy_property(bool, 'Check', AccessMode.ReadWrite)
    Enable = proxy_property(bool, 'Enable', AccessMode.ReadWrite)
    EndSubMenuLevel = proxy_property(int, 'EndSubMenuLevel', AccessMode.ReadWrite)
    HelpString = proxy_property(str, 'HelpString', AccessMode.ReadWrite)
    Index = proxy_property(str, 'Index', AccessMode.ReadOnly)
    Label = proxy_property(str, 'Label', AccessMode.ReadWrite)
    Parent = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)
    SubMenu = proxy_property('AcadPopupMenu', 'SubMenu', AccessMode.ReadOnly)
    TagString = proxy_property(str, 'TagString', AccessMode.ReadWrite)
    Type = proxy_property('AcMenuItemType', 'Type', AccessMode.ReadOnly)

    def Delete(self) -> None:
        self._obj.Delete()
