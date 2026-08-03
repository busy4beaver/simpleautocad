from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d


class Acad3DFace(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates: PyGePoint3dArray = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    VisibilityEdge1: bool = proxy_property(bool, 'VisibilityEdge1', AccessMode.ReadWrite)
    VisibilityEdge2: bool = proxy_property(bool, 'VisibilityEdge2', AccessMode.ReadWrite)
    VisibilityEdge3: bool = proxy_property(bool, 'VisibilityEdge3', AccessMode.ReadWrite)
    VisibilityEdge4: bool = proxy_property(bool, 'VisibilityEdge4', AccessMode.ReadWrite)

    def Coordinate(self, Index: int, pVal: PyGePoint3d) -> None:
        self._obj.Coordinate(Index, pVal())
