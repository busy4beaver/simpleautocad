from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadTolerance(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    DimensionLineColor = proxy_property('AcColor', 'DimensionLineColor', AccessMode.ReadWrite)
    DirectionVector = proxy_property('PyGeVector3d', 'DirectionVector', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    StyleName = proxy_property(str, 'StyleName', AccessMode.ReadWrite)
    TextColor = proxy_property('AcColor', 'TextColor', AccessMode.ReadWrite)
    TextHeight = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyle = proxy_property('AcadTextStyle', 'TextStyle', AccessMode.ReadWrite)
