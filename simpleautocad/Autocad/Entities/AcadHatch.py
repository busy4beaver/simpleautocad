from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray


class AcadHatch(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Area = proxy_property(float, 'Area', AccessMode.ReadOnly)
    AssociativeHatch = proxy_property(bool, 'AssociativeHatch', AccessMode.ReadOnly)
    BackgroundColor = proxy_property('AcadAcCmColor', 'BackgroundColor', AccessMode.ReadWrite)
    Elevation = proxy_property(float, 'Elevation', AccessMode.ReadWrite)
    GradientAngle = proxy_property(float, 'GradientAngle', AccessMode.ReadWrite)
    GradientCentered = proxy_property(bool, 'GradientCentered', AccessMode.ReadWrite)
    GradientColor1 = proxy_property('AcadAcCmColor', 'GradientColor1', AccessMode.ReadWrite)
    GradientColor2 = proxy_property('AcadAcCmColor', 'GradientColor2', AccessMode.ReadWrite)
    GradientName = proxy_property(str, 'GradientName', AccessMode.ReadWrite)
    HatchObjectType = proxy_property('AcHatchObjectType', 'HatchObjectType', AccessMode.ReadWrite)
    HatchStyle = proxy_property('AcHatchStyle', 'HatchStyle', AccessMode.ReadWrite)
    ISOPenWidth = proxy_property('AcISOPenWidth', 'ISOPenWidth', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    NumberOfLoops = proxy_property(int, 'NumberOfLoops', AccessMode.ReadOnly)
    Origin = proxy_property('PyGePoint3d', 'Origin', AccessMode.ReadWrite)
    PatternAngle = proxy_property(float, 'PatternAngle', AccessMode.ReadWrite)
    PatternDouble = proxy_property(bool, 'PatternDouble', AccessMode.ReadWrite)
    PatternName = proxy_property(str, 'PatternName', AccessMode.ReadWrite)
    PatternScale = proxy_property(float, 'PatternScale', AccessMode.ReadWrite)
    PatternSpace = proxy_property(float, 'PatternSpace', AccessMode.ReadWrite)
    PatternType = proxy_property('AcPatternType', 'PatternType', AccessMode.ReadOnly)

    def AppendInnerLoop(self, Loop: vObjectArray) -> None:
        self._obj.AppendInnerLoop(Loop)

    def AppendOuterLoop(self, Loop: vObjectArray) -> None:
        self._obj.AppendOuterLoop(Loop)
