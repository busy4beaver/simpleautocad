from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d


class Acad3DFace(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    VisibilityEdge1 = proxy_property(bool, 'VisibilityEdge1', AccessMode.ReadWrite)
    VisibilityEdge2 = proxy_property(bool, 'VisibilityEdge2', AccessMode.ReadWrite)
    VisibilityEdge3 = proxy_property(bool, 'VisibilityEdge3', AccessMode.ReadWrite)
    VisibilityEdge4 = proxy_property(bool, 'VisibilityEdge4', AccessMode.ReadWrite)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def Copy(self) -> Acad3DFace:
        return Acad3DFace(self._obj.Copy())

    def GetInvisibleEdge(self, Index: int) -> bool:
        return self._obj.GetInvisibleEdge(Index)

    def SetInvisibleEdge(self, Index: int, State: bool) -> None:
        self._obj.SetInvisibleEdge(Index, State)
