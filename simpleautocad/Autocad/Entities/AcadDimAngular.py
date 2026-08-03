from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadDimension import AcadDimension


class AcadDimAngular(AcadDimension):
    def __init__(self, obj) -> None: super().__init__(obj)

    AngleFormat: AcAngleUnits = proxy_property('AcAngleUnits', 'AngleFormat', AccessMode.ReadWrite)
    DimensionLineColor: AcColor = proxy_property('AcColor', 'DimensionLineColor', AccessMode.ReadWrite)
    DimensionLineWeight: AcLineWeight = proxy_property('AcLineWeight', 'DimensionLineWeight', AccessMode.ReadWrite)
    DimLine1Suppress: bool = proxy_property(bool, 'DimLine1Suppress', AccessMode.ReadWrite)
    DimLine2Suppress: bool = proxy_property(bool, 'DimLine2Suppress', AccessMode.ReadWrite)
    ExtLine1Suppress: bool = proxy_property(bool, 'ExtLine1Suppress', AccessMode.ReadWrite)
    ExtLine2Suppress: bool = proxy_property(bool, 'ExtLine2Suppress', AccessMode.ReadWrite)
    Fit: AcDimFit = proxy_property('AcDimFit', 'Fit', AccessMode.ReadWrite)
    ForceLineInside: bool = proxy_property(bool, 'ForceLineInside', AccessMode.ReadWrite)
    HorizontalTextPosition: AcDimHorizontalJustification = proxy_property('AcDimHorizontalJustification', 'HorizontalTextPosition', AccessMode.ReadWrite)
    TextInside: bool = proxy_property(bool, 'TextInside', AccessMode.ReadWrite)
    TextInsideAlign: bool = proxy_property(bool, 'TextInsideAlign', AccessMode.ReadWrite)
    TextOutsideAlign: bool = proxy_property(bool, 'TextOutsideAlign', AccessMode.ReadWrite)
    TextPrefix: str = proxy_property(str, 'TextPrefix', AccessMode.ReadWrite)
    TextSuffix: str = proxy_property(str, 'TextSuffix', AccessMode.ReadWrite)
    ToleranceDisplay: AcDimToleranceMethod = proxy_property('AcDimToleranceMethod', 'ToleranceDisplay', AccessMode.ReadWrite)
    ToleranceHeightScale: float = proxy_property(float, 'ToleranceHeightScale', AccessMode.ReadWrite)
    ToleranceJustification: AcDimToleranceJustify = proxy_property('AcDimToleranceJustify', 'ToleranceJustification', AccessMode.ReadWrite)
    ToleranceLowerLimit: float = proxy_property(float, 'ToleranceLowerLimit', AccessMode.ReadWrite)
    TolerancePrecision: AcDimPrecision = proxy_property('AcDimPrecision', 'TolerancePrecision', AccessMode.ReadWrite)
    ToleranceSuppressLeadingZeros: bool = proxy_property(bool, 'ToleranceSuppressLeadingZeros', AccessMode.ReadWrite)
    ToleranceSuppressTrailingZeros: bool = proxy_property(bool, 'ToleranceSuppressTrailingZeros', AccessMode.ReadWrite)
    ToleranceUpperLimit: float = proxy_property(float, 'ToleranceUpperLimit', AccessMode.ReadWrite)

    def Copy(self) -> AcadDimAngular:
        return AcadDimAngular(self._obj.Copy())
