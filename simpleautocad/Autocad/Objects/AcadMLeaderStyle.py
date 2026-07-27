from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.Ge import PyGePoint3dArray


class AcadMLeaderStyle(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AlignSpace = proxy_property(int, 'AlignSpace', AccessMode.ReadWrite)
    Annotative = proxy_property(bool, 'Annotative', AccessMode.ReadWrite)
    ArrowSize = proxy_property(int, 'ArrowSize', AccessMode.ReadWrite)
    ArrowSymbol = proxy_property(str, 'ArrowSymbol', AccessMode.ReadWrite)
    BitFlags = proxy_property(int, 'BitFlags', AccessMode.ReadWrite)
    Block = proxy_property(str, 'Block', AccessMode.ReadOnly)
    BlockColor = proxy_property('AcadAcCmColor', 'BlockColor', AccessMode.ReadWrite)
    BlockConnectionType = proxy_property('AcBlockConnectionType', 'BlockConnectionType', AccessMode.ReadWrite)
    BlockRotation = proxy_property(float, 'BlockRotation', AccessMode.ReadWrite)
    BlockScale = proxy_property(float, 'BlockScale', AccessMode.ReadWrite)
    BreakSize = proxy_property(float, 'BreakSize', AccessMode.ReadWrite)
    ContentType = proxy_property('AcMLeaderContentType', 'ContentType', AccessMode.ReadWrite)
    Description = proxy_property(str, 'Description', AccessMode.ReadWrite)
    DoglegLength = proxy_property(float, 'DoglegLength', AccessMode.ReadWrite)
    DrawLeaderOrderType = proxy_property('AcDrawLeaderOrderType', 'DrawLeaderOrderType', AccessMode.ReadWrite)
    DrawMLeaderOrderType = proxy_property('AcDrawLeaderOrderType', 'DrawMLeaderOrderType', AccessMode.ReadWrite)
    EnableBlockRotation = proxy_property(bool, 'EnableBlockRotation', AccessMode.ReadWrite)
    EnableBlockScale = proxy_property(bool, 'EnableBlockScale', AccessMode.ReadWrite)
    EnableDogleg = proxy_property(bool, 'EnableDogleg', AccessMode.ReadWrite)
    EnableFrameText = proxy_property(bool, 'EnableFrameText', AccessMode.ReadWrite)
    EnableLanding = proxy_property(bool, 'EnableLanding', AccessMode.ReadWrite)
    FirstSegmentAngleConstraint = proxy_property(int, 'FirstSegmentAngleConstraint', AccessMode.ReadWrite)
    LandingGap = proxy_property(float, 'LandingGap', AccessMode.ReadWrite)
    LeaderLineColor = proxy_property('AcadAcCmColor', 'LeaderLineColor', AccessMode.ReadWrite)
    LeaderLinetype = proxy_property(str, 'LeaderLinetype', AccessMode.ReadWrite)
    LeaderLineTypeId = proxy_property(int, 'LeaderLineTypeId', AccessMode.ReadWrite)
    LeaderLineWeight = proxy_property('AcLineWeight', 'LeaderLineWeight', AccessMode.ReadWrite)
    MaxLeaderSegmentsPoints = proxy_property(int, 'MaxLeaderSegmentsPoints', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    OverwritePropChanged = proxy_property(bool, 'OverwritePropChanged', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    SecondSegmentAngleConstraint = proxy_property(int, 'SecondSegmentAngleConstraint', AccessMode.ReadWrite)
    TextAlignmentType = proxy_property('AcTextAlignmentType', 'TextAlignmentType', AccessMode.ReadWrite)
    TextAngleType = proxy_property('AcTextAngleType', 'TextAngleType', AccessMode.ReadWrite)
    TextAttachmentDirection = proxy_property('AcTextAttachmentDirection', 'TextAttachmentDirection', AccessMode.ReadWrite)
    TextBottomAttachmentType = proxy_property('AcVerticalTextAttachmentType', 'TextBottomAttachmentType', AccessMode.ReadWrite)
    TextColor = proxy_property('AcColor', 'TextColor', AccessMode.ReadWrite)
    TextHeight = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextLeftAttachmentType = proxy_property('AcTextAttachmentType', 'TextLeftAttachmentType', AccessMode.ReadWrite)
    TextRightAttachmentType = proxy_property('AcTextAttachmentType', 'TextRightAttachmentType', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyle = proxy_property(str, 'TextStyle', AccessMode.ReadWrite)
    TextTopAttachmentType = proxy_property('AcVerticalTextAttachmentType', 'TextTopAttachmentType', AccessMode.ReadWrite)

    def GetBoundingBox(self) -> PyGePoint3dArray:
        MinPoint, MaxPoint = self._obj.GetBoundingBox()
        return PyGePoint3dArray(MinPoint, MaxPoint)
