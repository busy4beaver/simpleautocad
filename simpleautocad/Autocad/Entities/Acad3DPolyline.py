from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d
from ...Types.VarType import vObjectArray


class Acad3DPolyline(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Closed = proxy_property(bool, 'Closed', AccessMode.ReadWrite)
    Coordinates = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    Length = proxy_property(float, 'Length', AccessMode.ReadOnly)
    Type = proxy_property('Ac3DPolylineType', 'Type', AccessMode.ReadWrite)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def Copy(self) -> Acad3DPolyline:
        return Acad3DPolyline(self._obj.Copy())

    def AppendVertex(self, Point: PyGePoint3d) -> None:
        self._obj.AppendVertex(Point())

    def Explode(self) -> vObjectArray:
        return vObjectArray(self._obj.Explode())
