from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray


class AcadArc(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ArcLength = proxy_property(float, 'ArcLength', AccessMode.ReadOnly)
    Area = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Center = proxy_property('PyGePoint3d', 'Center', AccessMode.ReadWrite)
    EndAngle = proxy_property(float, 'EndAngle', AccessMode.ReadWrite)
    EndPoint = proxy_property('PyGePoint3d', 'EndPoint', AccessMode.ReadOnly)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Radius = proxy_property(float, 'Radius', AccessMode.ReadWrite)
    StartAngle = proxy_property(float, 'StartAngle', AccessMode.ReadWrite)
    StartPoint = proxy_property('PyGePoint3d', 'StartPoint', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)
    TotalAngle = proxy_property(float, 'TotalAngle', AccessMode.ReadOnly)

    def Copy(self) -> AcadArc:
        return AcadArc(self._obj.Copy())

    def Offset(self, Distance: float) -> vObjectArray:
        return vObjectArray(self._obj.Offset(Distance))
