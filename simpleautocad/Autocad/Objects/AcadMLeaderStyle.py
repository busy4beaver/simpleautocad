from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.Ge import PyGePoint3dArray
from ...Types.Ac import (
    AcBlockConnectionType,
    AcMLeaderContentType,
    AcLineWeight,
    AcLeaderType,
    AcTextAlignmentType,
    AcTextAttachmentType,
)

if TYPE_CHECKING:
    from .AcadAcCmColor import AcadAcCmColor


class AcadMLeaderStyle(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AlignSpace: int = proxy_property(int, 'AlignSpace', AccessMode.ReadWrite)
    Annotative: bool = proxy_property(bool, 'Annotative', AccessMode.ReadWrite)
    ArrowSize: int = proxy_property(int, 'ArrowSize', AccessMode.ReadWrite)
    ArrowSymbol: str = proxy_property(str, 'ArrowSymbol', AccessMode.ReadWrite)
    BitFlags: int = proxy_property(int, 'BitFlags', AccessMode.ReadWrite)
    Block: str = proxy_property(str, 'Block', AccessMode.ReadWrite)
    BlockColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'BlockColor', AccessMode.ReadWrite)
    BlockConnectionType: AcBlockConnectionType = proxy_property('AcBlockConnectionType', 'BlockConnectionType', AccessMode.ReadWrite)
    BlockRotation: float = proxy_property(float, 'BlockRotation', AccessMode.ReadWrite)
    BlockScale: float = proxy_property(float, 'BlockScale', AccessMode.ReadWrite)
    BreakSize: float = proxy_property(float, 'BreakSize', AccessMode.ReadWrite)
    ContentType: AcMLeaderContentType = proxy_property('AcMLeaderContentType', 'ContentType', AccessMode.ReadWrite)
    Description: str = proxy_property(str, 'Description', AccessMode.ReadWrite)
    DoglegLength: float = proxy_property(float, 'DoglegLength', AccessMode.ReadWrite)
    DrawLeaderOrderType: int = proxy_property(int, 'DrawLeaderOrderType', AccessMode.ReadWrite)
    DrawMLeaderOrderType: int = proxy_property(int, 'DrawMLeaderOrderType', AccessMode.ReadWrite)
    EnableBlockScale: bool = proxy_property(bool, 'EnableBlockScale', AccessMode.ReadWrite)
    EnableDogleg: bool = proxy_property(bool, 'EnableDogleg', AccessMode.ReadWrite)
    EnableFrameText: bool = proxy_property(bool, 'EnableFrameText', AccessMode.ReadWrite)
    EnableLanding: bool = proxy_property(bool, 'EnableLanding', AccessMode.ReadWrite)
    FirstSegmentAngleConstraint: int = proxy_property(int, 'FirstSegmentAngleConstraint', AccessMode.ReadWrite)
    LandingGap: float = proxy_property(float, 'LandingGap', AccessMode.ReadWrite)
    LeaderLineColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'LeaderLineColor', AccessMode.ReadWrite)
    LeaderLineType: str = proxy_property(str, 'LeaderLineType', AccessMode.ReadWrite)
    LeaderLineTypeId: int = proxy_property(int, 'LeaderLineTypeId', AccessMode.ReadWrite)
    LeaderLineWeight: AcLineWeight = proxy_property('AcLineWeight', 'LeaderLineWeight', AccessMode.ReadWrite)
    LeaderType: AcLeaderType = proxy_property('AcLeaderType', 'LeaderType', AccessMode.ReadWrite)
    MaxLeaderSegmentsPoints: int = proxy_property(int, 'MaxLeaderSegmentsPoints', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Scale: float = proxy_property(float, 'Scale', AccessMode.ReadWrite)
    SecondSegmentAngleConstraint: int = proxy_property(int, 'SecondSegmentAngleConstraint', AccessMode.ReadWrite)
    TextAlignmentType: AcTextAlignmentType = proxy_property('AcTextAlignmentType', 'TextAlignmentType', AccessMode.ReadWrite)
    TextAngleType: int = proxy_property(int, 'TextAngleType', AccessMode.ReadWrite)
    TextColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'TextColor', AccessMode.ReadWrite)
    TextHeight: float = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextLeftAttachmentType: AcTextAttachmentType = proxy_property('AcTextAttachmentType', 'TextLeftAttachmentType', AccessMode.ReadWrite)
    TextRightAttachmentType: AcTextAttachmentType = proxy_property('AcTextAttachmentType', 'TextRightAttachmentType', AccessMode.ReadWrite)
    TextString: str = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyle: str = proxy_property(str, 'TextStyle', AccessMode.ReadWrite)
    TextStyleName: str = proxy_property(str, 'TextStyleName', AccessMode.ReadWrite)

    def GetBoundingBox(self) -> PyGePoint3dArray:
        MinPoint, MaxPoint = self._obj.GetBoundingBox()
        return PyGePoint3dArray(MinPoint, MaxPoint)
