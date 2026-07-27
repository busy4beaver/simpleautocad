from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadGeoPositionMarker(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Altitude = proxy_property(float, 'Altitude', AccessMode.ReadWrite)
    BackgroundFill = proxy_property(bool, 'BackgroundFill', AccessMode.ReadWrite)
    DrawingDirection = proxy_property('AcDrawingDirection', 'DrawingDirection', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    LandingGap = proxy_property(float, 'LandingGap', AccessMode.ReadWrite)
    Latitude = proxy_property(str, 'Latitude', AccessMode.ReadWrite)
    LineSpacingDistance = proxy_property(float, 'LineSpacingDistance', AccessMode.ReadWrite)
    LineSpacingFactor = proxy_property(float, 'LineSpacingFactor', AccessMode.ReadWrite)
    LineSpacingStyle = proxy_property('AcLineSpacingStyle', 'LineSpacingStyle', AccessMode.ReadWrite)
    Longitude = proxy_property(str, 'Longitude', AccessMode.ReadWrite)
    Notes = proxy_property(str, 'Notes', AccessMode.ReadWrite)
    Position = proxy_property('PyGePoint3d', 'Position', AccessMode.ReadWrite)
    Radius = proxy_property(float, 'Radius', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    TextFrameDisplay = proxy_property(bool, 'TextFrameDisplay', AccessMode.ReadWrite)
    TextJustify = proxy_property('AcAttachmentPoint', 'TextJustify', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyleName = proxy_property(str, 'TextStyleName', AccessMode.ReadWrite)
    TextWidth = proxy_property(float, 'TextWidth', AccessMode.ReadWrite)

    def Copy(self) -> AcadGeoPositionMarker:
        return AcadGeoPositionMarker(self._obj.Copy())
