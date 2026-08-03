from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadDimension import AcadDimension
from ...Types.Ac import (
    AcDimPrecision,
    AcDimUnits,
    AcColor,
    AcLineWeight,
    AcDimFit,
    AcDimFractionType,
    AcDimHorizontalJustification,
    AcDimToleranceMethod,
    AcDimToleranceJustify,
    AcDimLUnits,
    AcDimCenterType,
)


class AcadDimDiametric(AcadDimension):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AltRoundDistance: float = proxy_property(float, 'AltRoundDistance', AccessMode.ReadWrite)
    AltSuppressLeadingZeros: bool = proxy_property(bool, 'AltSuppressLeadingZeros', AccessMode.ReadWrite)
    AltSuppressTrailingZeros: bool = proxy_property(bool, 'AltSuppressTrailingZeros', AccessMode.ReadWrite)
    AltSuppressZeroFeet: bool = proxy_property(bool, 'AltSuppressZeroFeet', AccessMode.ReadWrite)
    AltSuppressZeroInches: bool = proxy_property(bool, 'AltSuppressZeroInches', AccessMode.ReadWrite)
    AltTextPrefix: str = proxy_property(str, 'AltTextPrefix', AccessMode.ReadWrite)
    AltTextSuffix: str = proxy_property(str, 'AltTextSuffix', AccessMode.ReadWrite)
    AltTolerancePrecision: AcDimPrecision = proxy_property('AcDimPrecision', 'AltTolerancePrecision', AccessMode.ReadWrite)
    AltToleranceSuppressLeadingZeros: bool = proxy_property(bool, 'AltToleranceSuppressLeadingZeros', AccessMode.ReadWrite)
    AltToleranceSuppressTrailingZeros: bool = proxy_property(bool, 'AltToleranceSuppressTrailingZeros', AccessMode.ReadWrite)
    AltToleranceSuppressZeroFeet: bool = proxy_property(bool, 'AltToleranceSuppressZeroFeet', AccessMode.ReadWrite)
    AltToleranceSuppressZeroInches: bool = proxy_property(bool, 'AltToleranceSuppressZeroInches', AccessMode.ReadWrite)
    AltUnits: bool = proxy_property(bool, 'AltUnits', AccessMode.ReadWrite)
    AltUnitsFormat: AcDimUnits = proxy_property('AcDimUnits', 'AltUnitsFormat', AccessMode.ReadWrite)
    AltUnitsPrecision: AcDimPrecision = proxy_property('AcDimPrecision', 'AltUnitsPrecision', AccessMode.ReadWrite)
    AltUnitsScale: float = proxy_property(float, 'AltUnitsScale', AccessMode.ReadWrite)
    CenterMarkSize: float = proxy_property(float, 'CenterMarkSize', AccessMode.ReadWrite)
    CenterType: AcDimCenterType = proxy_property('AcDimCenterType', 'CenterType', AccessMode.ReadWrite)
    DimensionLineColor: AcColor = proxy_property('AcColor', 'DimensionLineColor', AccessMode.ReadWrite)
    DimensionLineWeight: AcLineWeight = proxy_property('AcLineWeight', 'DimensionLineWeight', AccessMode.ReadWrite)
    DimLine1Suppress: bool = proxy_property(bool, 'DimLine1Suppress', AccessMode.ReadWrite)
    DimLine2Suppress: bool = proxy_property(bool, 'DimLine2Suppress', AccessMode.ReadWrite)
    Fit: AcDimFit = proxy_property('AcDimFit', 'Fit', AccessMode.ReadWrite)
    ForceLineInside: bool = proxy_property(bool, 'ForceLineInside', AccessMode.ReadWrite)
    FractionFormat: AcDimFractionType = proxy_property('AcDimFractionType', 'FractionFormat', AccessMode.ReadWrite)
    HorizontalTextPosition: AcDimHorizontalJustification = proxy_property('AcDimHorizontalJustification', 'HorizontalTextPosition', AccessMode.ReadWrite)
    LeaderLength: float = proxy_property(float, 'LeaderLength', AccessMode.WriteOnly)
    LinearScaleFactor: float = proxy_property(float, 'LinearScaleFactor', AccessMode.ReadWrite)
    PrimaryUnitsPrecision: AcDimPrecision = proxy_property('AcDimPrecision', 'PrimaryUnitsPrecision', AccessMode.ReadWrite)
    RoundDistance: float = proxy_property(float, 'RoundDistance', AccessMode.ReadWrite)
    SuppressLeadingZeros: bool = proxy_property(bool, 'SuppressLeadingZeros', AccessMode.ReadWrite)
    SuppressTrailingZeros: bool = proxy_property(bool, 'SuppressTrailingZeros', AccessMode.ReadWrite)
    SuppressZeroFeet: bool = proxy_property(bool, 'SuppressZeroFeet', AccessMode.ReadWrite)
    SuppressZeroInches: bool = proxy_property(bool, 'SuppressZeroInches', AccessMode.ReadWrite)
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
    ToleranceSuppressZeroFeet: bool = proxy_property(bool, 'ToleranceSuppressZeroFeet', AccessMode.ReadWrite)
    ToleranceSuppressZeroInches: bool = proxy_property(bool, 'ToleranceSuppressZeroInches', AccessMode.ReadWrite)
    ToleranceUpperLimit: float = proxy_property(float, 'ToleranceUpperLimit', AccessMode.ReadWrite)
    UnitsFormat: AcDimLUnits = proxy_property('AcDimLUnits', 'UnitsFormat', AccessMode.ReadWrite)

    def Copy(self) -> AcadDimDiametric:
        return AcadDimDiametric(self._obj.Copy())
