from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d, PyGeVector3d
from ...Types.Ac import AcColor

if TYPE_CHECKING:
    from ..Objects.AcadTextStyle import AcadTextStyle


class AcadTolerance(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    DimensionLineColor: AcColor = proxy_property('AcColor', 'DimensionLineColor', AccessMode.ReadWrite)
    DirectionVector: PyGeVector3d = proxy_property('PyGeVector3d', 'DirectionVector', AccessMode.ReadWrite)
    InsertionPoint: PyGePoint3d = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ScaleFactor: float = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    StyleName: str = proxy_property(str, 'StyleName', AccessMode.ReadWrite)
    TextColor: AcColor = proxy_property('AcColor', 'TextColor', AccessMode.ReadWrite)
    TextHeight: float = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextString: str = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyle: AcadTextStyle = proxy_property('AcadTextStyle', 'TextStyle', AccessMode.ReadWrite)
