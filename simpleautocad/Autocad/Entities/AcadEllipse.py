from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadEllipse(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Area = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Center = proxy_property('PyGePoint3d', 'Center', AccessMode.ReadWrite)
    EndAngle = proxy_property(float, 'EndAngle', AccessMode.ReadWrite)
    EndParameter = proxy_property(float, 'EndParameter', AccessMode.ReadWrite)
    EndPoint = proxy_property('PyGePoint3d', 'EndPoint', AccessMode.ReadWrite)
    MajorAxis = proxy_property('PyGeVector3d', 'MajorAxis', AccessMode.ReadWrite)
    MajorRadius = proxy_property(float, 'MajorRadius', AccessMode.ReadWrite)
    MinorAxis = proxy_property('PyGeVector3d', 'MinorAxis', AccessMode.ReadOnly)
    MinorRadius = proxy_property(float, 'MinorRadius', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    RadiusRatio = proxy_property(float, 'RadiusRatio', AccessMode.ReadWrite)
    StartAngle = proxy_property(float, 'StartAngle', AccessMode.ReadWrite)
    StartParameter = proxy_property(float, 'StartParameter', AccessMode.ReadWrite)
    StartPoint = proxy_property('PyGePoint3d', 'StartPoint', AccessMode.ReadWrite)

    def Copy(self) -> AcadEllipse:
        return AcadEllipse(self._obj.Copy())

    def Offset(self, Distance: float) -> AcadEllipse:
        return AcadEllipse(self._obj.Offset(Distance))
