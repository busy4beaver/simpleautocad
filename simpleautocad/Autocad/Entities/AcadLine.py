from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray


class AcadLine(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Angle = proxy_property(float, 'Angle', AccessMode.ReadOnly)
    Delta = proxy_property('vDoubleArray', 'Delta', AccessMode.ReadOnly)
    EndPoint = proxy_property('PyGePoint3d', 'EndPoint', AccessMode.ReadWrite)
    Length = proxy_property(float, 'Length', AccessMode.ReadOnly)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    StartPoint = proxy_property('PyGePoint3d', 'StartPoint', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)

    def Offset(self, Distance: float) -> vObjectArray:
        return vObjectArray(self._obj.Offset(Distance))

    def Copy(self) -> AcadLine:
        return AcadLine(self._obj.Copy())
