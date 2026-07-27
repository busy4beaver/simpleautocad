from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d


class AcadPolyfaceMesh(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    NumberOfFaces = proxy_property(int, 'NumberOfFaces', AccessMode.ReadOnly)
    NumberOfVertices = proxy_property(int, 'NumberOfVertices', AccessMode.ReadOnly)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def Copy(self) -> AcadPolyfaceMesh:
        return AcadPolyfaceMesh(self._obj.Copy())
