from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d
from ...Types.VarType import vObjectArray


class AcadPolygonMesh(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    MClose = proxy_property(bool, 'MClose', AccessMode.ReadWrite)
    MDensity = proxy_property(int, 'MDensity', AccessMode.ReadWrite)
    MVertexCount = proxy_property(int, 'MVertexCount', AccessMode.ReadOnly)
    NClose = proxy_property(bool, 'NClose', AccessMode.ReadWrite)
    NDensity = proxy_property(int, 'NDensity', AccessMode.ReadWrite)
    NVertexCount = proxy_property(int, 'NVertexCount', AccessMode.ReadOnly)
    Type = proxy_property('AcPolymeshType', 'Type', AccessMode.ReadWrite)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def Copy(self) -> AcadPolygonMesh:
        return AcadPolygonMesh(self._obj.Copy())

    def AppendVertex(self, Point: PyGePoint3d) -> None:
        self._obj.AppendVertex(Point())

    def Explode(self) -> vObjectArray:
        return vObjectArray(self._obj.Explode())
