from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadDimension import AcadDimension
from ...Types.Ge import PyGePoint3d, PyGeVector3d
from ...Types.Ac import AcAngleUnits, AcDimPrecision, AcDimTextMovement, AcDimVerticalJustification


class AcadDim3PointAngular(AcadDimension):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AngleFormat: AcAngleUnits = proxy_property('AcAngleUnits', 'AngleFormat', AccessMode.ReadWrite)
    AngleVertex: PyGePoint3d = proxy_property('PyGePoint3d', 'AngleVertex', AccessMode.ReadWrite)
    Arrowhead1Block: str = proxy_property(str, 'Arrowhead1Block', AccessMode.ReadWrite)
    Arrowhead1Type: AcDimArrowheadType = proxy_property('AcDimArrowheadType', 'Arrowhead1Type', AccessMode.ReadWrite)
    Arrowhead2Block: str = proxy_property(str, 'Arrowhead2Block', AccessMode.ReadWrite)
    Arrowhead2Type: AcDimArrowheadType = proxy_property('AcDimArrowheadType', 'Arrowhead2Type', AccessMode.ReadWrite)
    ArrowheadSize: float = proxy_property(float, 'ArrowheadSize', AccessMode.ReadWrite)
    DimLine1Suppress: bool = proxy_property(bool, 'DimLine1Suppress', AccessMode.ReadWrite)
    DimLine2Suppress: bool = proxy_property(bool, 'DimLine2Suppress', AccessMode.ReadWrite)
    DimLineInside: bool = proxy_property(bool, 'DimLineInside', AccessMode.ReadWrite)
    ExtensionLineExtend: float = proxy_property(float, 'ExtensionLineExtend', AccessMode.ReadWrite)
    ExtensionLineOffset: float = proxy_property(float, 'ExtensionLineOffset', AccessMode.ReadWrite)
    ExtLine1EndPoint: PyGePoint3d = proxy_property('PyGePoint3d', 'ExtLine1EndPoint', AccessMode.ReadWrite)
    ExtLine1Suppress: bool = proxy_property(bool, 'ExtLine1Suppress', AccessMode.ReadWrite)
    ExtLine2EndPoint: PyGePoint3d = proxy_property('PyGePoint3d', 'ExtLine2EndPoint', AccessMode.ReadWrite)
    ExtLine2Suppress: bool = proxy_property(bool, 'ExtLine2Suppress', AccessMode.ReadWrite)
    Fit: AcDimFit = proxy_property('AcDimFit', 'Fit', AccessMode.ReadWrite)
    ForceLineInside: bool = proxy_property(bool, 'ForceLineInside', AccessMode.ReadWrite)
    HorizontalTextPosition: AcDimHorizontalJustification = proxy_property('AcDimHorizontalJustification', 'HorizontalTextPosition', AccessMode.ReadWrite)
    TextInside: bool = proxy_property(bool, 'TextInside', AccessMode.ReadWrite)
    TextInsideAlign: bool = proxy_property(bool, 'TextInsideAlign', AccessMode.ReadWrite)
    TextMovement: AcDimTextMovement = proxy_property('AcDimTextMovement', 'TextMovement', AccessMode.ReadWrite)
    TextOutsideAlign: bool = proxy_property(bool, 'TextOutsideAlign', AccessMode.ReadWrite)
    TextPrecision: AcDimPrecision = proxy_property('AcDimPrecision', 'TextPrecision', AccessMode.ReadWrite)
    TextSuppressLeadingZeros: bool = proxy_property(bool, 'TextSuppressLeadingZeros', AccessMode.ReadWrite)
    TextSuppressTrailingZeros: bool = proxy_property(bool, 'TextSuppressTrailingZeros', AccessMode.ReadWrite)
    VerticalTextPosition: AcDimVerticalJustification = proxy_property('AcDimVerticalJustification', 'VerticalTextPosition', AccessMode.ReadWrite)
