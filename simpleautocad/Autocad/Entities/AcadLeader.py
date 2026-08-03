from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ..Base import AppObject
from ...Types.Ge import PyGePoint3d, PyGePoint3dArray, PyGeVector3d
from ...Types.Ac import AcDimArrowheadType, AcColor, AcLineWeight, AcLeaderType


class AcadLeader(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Annotation: AppObject = proxy_property('AppObject', 'Annotation', AccessMode.ReadWrite)
    ArrowheadBlock: str = proxy_property(str, 'ArrowheadBlock', AccessMode.ReadWrite)
    ArrowheadSize: float = proxy_property(float, 'ArrowheadSize', AccessMode.ReadWrite)
    ArrowheadType: AcDimArrowheadType = proxy_property('AcDimArrowheadType', 'ArrowheadType', AccessMode.ReadWrite)
    Coordinates: PyGePoint3dArray = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    DimensionLineColor: AcColor = proxy_property('AcColor', 'DimensionLineColor', AccessMode.ReadWrite)
    DimensionLineWeight: AcLineWeight = proxy_property('AcLineWeight', 'DimensionLineWeight', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    TextGap: float = proxy_property(float, 'TextGap', AccessMode.ReadWrite)
    Type: AcLeaderType = proxy_property('AcLeaderType', 'Type', AccessMode.ReadWrite)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def Copy(self) -> AcadLeader:
        return AcadLeader(self._obj.Copy())

    def Evaluate(self) -> None:
        self._obj.Evaluate()
