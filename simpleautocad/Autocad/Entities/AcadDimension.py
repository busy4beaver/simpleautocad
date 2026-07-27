from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadDimension(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    DecimalSeparator = proxy_property(str, 'DecimalSeparator', AccessMode.ReadWrite)
    DimTxtDirection = proxy_property(bool, 'DimTxtDirection', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    StyleName = proxy_property(str, 'StyleName', AccessMode.ReadWrite)
    SuppressLeadingZeros = proxy_property(bool, 'SuppressLeadingZeros', AccessMode.ReadWrite)
    SuppressTrailingZeros = proxy_property(bool, 'SuppressTrailingZeros', AccessMode.ReadWrite)
    TextColor = proxy_property('AcColor', 'TextColor', AccessMode.ReadWrite)
    TextFill = proxy_property(bool, 'TextFill', AccessMode.ReadWrite)
    TextFillColor = proxy_property('AcColor', 'TextFillColor', AccessMode.ReadWrite)
    TextGap = proxy_property(float, 'TextGap', AccessMode.ReadWrite)
    TextHeight = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextMovement = proxy_property('AcDimTextMovement', 'TextMovement', AccessMode.ReadWrite)
    TextOverride = proxy_property(str, 'TextOverride', AccessMode.ReadWrite)
    TextPosition = proxy_property('PyGePoint3d', 'TextPosition', AccessMode.ReadWrite)
    TextPrefix = proxy_property(str, 'TextPrefix', AccessMode.ReadWrite)
    TextRotation = proxy_property(float, 'TextRotation', AccessMode.ReadWrite)
    TextStyle = proxy_property(str, 'TextStyle', AccessMode.ReadWrite)
    TextSuffix = proxy_property(str, 'TextSuffix', AccessMode.ReadWrite)
    ToleranceDisplay = proxy_property('AcDimToleranceMethod', 'ToleranceDisplay', AccessMode.ReadWrite)
    ToleranceHeightScale = proxy_property(float, 'ToleranceHeightScale', AccessMode.ReadWrite)
    ToleranceJustification = proxy_property('AcDimToleranceJustify', 'ToleranceJustification', AccessMode.ReadWrite)
    ToleranceLowerLimit = proxy_property(float, 'ToleranceLowerLimit', AccessMode.ReadWrite)
    TolerancePrecision = proxy_property('AcDimPrecision', 'TolerancePrecision', AccessMode.ReadWrite)
    ToleranceSuppressLeadingZeros = proxy_property(bool, 'ToleranceSuppressLeadingZeros', AccessMode.ReadWrite)
    ToleranceSuppressTrailingZeros = proxy_property(bool, 'ToleranceSuppressTrailingZeros', AccessMode.ReadWrite)
    ToleranceUpperLimit = proxy_property(float, 'ToleranceUpperLimit', AccessMode.ReadWrite)
    VerticalTextPosition = proxy_property('AcDimVerticalJustification', 'VerticalTextPosition', AccessMode.ReadWrite)

    def Copy(self) -> AcadDimension:
        return AcadDimension(self._obj.Copy())
