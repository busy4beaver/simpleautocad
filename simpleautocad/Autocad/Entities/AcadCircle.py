from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray


class AcadCircle(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Area = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Center = proxy_property('PyGePoint3d', 'Center', AccessMode.ReadWrite)
    Circumference = proxy_property(float, 'Circumference', AccessMode.ReadWrite)
    Diameter = proxy_property(float, 'Diameter', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Radius = proxy_property(float, 'Radius', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)

    def Offset(self, Distance: float) -> vObjectArray:
        return vObjectArray(self._obj.Offset(Distance))

    def Copy(self) -> AcadCircle:
        return AcadCircle(self._obj.Copy())
