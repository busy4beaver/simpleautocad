from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3dArray


class AcadPolyfaceMesh(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates: PyGePoint3dArray = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    Coordinate: PyGePoint3d = proxy_property('PyGePoint3d', 'Coordinate', AccessMode.ReadWrite)
    NumberOfFaces: int = proxy_property(int, 'NumberOfFaces', AccessMode.ReadOnly)
    NumberOfVertices: int = proxy_property(int, 'NumberOfVertices', AccessMode.ReadOnly)
