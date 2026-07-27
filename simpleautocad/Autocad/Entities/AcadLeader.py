from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d


class AcadLeader(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Annotation = proxy_property('AppObject', 'Annotation', AccessMode.ReadWrite)
    ArrowheadBlock = proxy_property(str, 'ArrowheadBlock', AccessMode.ReadWrite)
    ArrowheadSize = proxy_property(float, 'ArrowheadSize', AccessMode.ReadWrite)
    ArrowheadType = proxy_property('AcDimArrowheadType', 'ArrowheadType', AccessMode.ReadWrite)
    Coordinates = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    DimensionLineColor = proxy_property('AcColor', 'DimensionLineColor', AccessMode.ReadWrite)
    DimensionLineWeight = proxy_property('AcLineWeight', 'DimensionLineWeight', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    TextGap = proxy_property(float, 'TextGap', AccessMode.ReadWrite)
    Type = proxy_property('AcLeaderType', 'Type', AccessMode.ReadWrite)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def Copy(self) -> AcadLeader:
        return AcadLeader(self._obj.Copy())

    def Evaluate(self) -> None:
        self._obj.Evaluate()
