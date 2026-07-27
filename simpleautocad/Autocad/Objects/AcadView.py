from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadView(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CategoryName = proxy_property(str, 'CategoryName', AccessMode.ReadWrite)
    Center = proxy_property('PyGePoint2d', 'Center', AccessMode.ReadWrite)
    Direction = proxy_property('PyGeVector3d', 'Direction', AccessMode.ReadWrite)
    HasVpAssociation = proxy_property(bool, 'HasVpAssociation', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    LayerState = proxy_property(str, 'LayerState', AccessMode.ReadWrite)
    LayoutID = proxy_property(int, 'LayoutID', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Target = proxy_property('PyGePoint3d', 'Target', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)
