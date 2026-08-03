from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d, PyGeVector3d
from ...Types.Ac import (
    AcMLeaderType,
    AcMLeaderContentType,
    AcTextAttachmentType,
    AcTextAttachmentDirection,
    AcVerticalTextAttachmentType,
    AcHorizontalTextAttachmentType,
    AcTextAlignmentType,
    AcDrawingDirection,
    AcLineSpacingStyle,
    AcDimArrowheadType,
    AcColor,
    AcLeaderType,
    AcBlockConnectionType,
)


class AcadMLeader(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ArrowheadBlock: str = proxy_property(str, 'ArrowheadBlock', AccessMode.ReadWrite)
    ArrowheadSize: float = proxy_property(float, 'ArrowheadSize', AccessMode.ReadWrite)
    ArrowheadType: AcDimArrowheadType = proxy_property('AcDimArrowheadType', 'ArrowheadType', AccessMode.ReadWrite)
    BlockConnectionType: AcBlockConnectionType = proxy_property('AcBlockConnectionType', 'BlockConnectionType', AccessMode.ReadWrite)
    BlockScale: float = proxy_property(float, 'BlockScale', AccessMode.ReadWrite)
    ContentBlockName: str = proxy_property(str, 'ContentBlockName', AccessMode.ReadWrite)
    ContentBlockType: int = proxy_property(int, 'ContentBlockType', AccessMode.ReadWrite)
    ContentType: AcMLeaderContentType = proxy_property('AcMLeaderContentType', 'ContentType', AccessMode.ReadWrite)
    DoglegLength: float = proxy_property(float, 'DoglegLength', AccessMode.ReadWrite)
    EnableAnnotationScale: bool = proxy_property(bool, 'EnableAnnotationScale', AccessMode.ReadWrite)
    EnableDogleg: bool = proxy_property(bool, 'EnableDogleg', AccessMode.ReadWrite)
    EnableFrameText: bool = proxy_property(bool, 'EnableFrameText', AccessMode.ReadWrite)
    EnableLanding: bool = proxy_property(bool, 'EnableLanding', AccessMode.ReadWrite)
    LandingGap: float = proxy_property(float, 'LandingGap', AccessMode.ReadWrite)
    LeaderCount: int = proxy_property(int, 'LeaderCount', AccessMode.ReadOnly)
    LeaderLineColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'LeaderLineColor', AccessMode.ReadWrite)
    LeaderLineType: str = proxy_property(str, 'LeaderLineType', AccessMode.ReadWrite)
    LeaderLineTypeId: int = proxy_property(int, 'LeaderLineTypeId', AccessMode.ReadWrite)
    LeaderLineWeight: AcLineWeight = proxy_property('AcLineWeight', 'LeaderLineWeight', AccessMode.ReadWrite)
    LeaderType: AcLeaderType = proxy_property('AcLeaderType', 'LeaderType', AccessMode.ReadWrite)
    Scale: float = proxy_property(float, 'Scale', AccessMode.ReadWrite)
    StyleName: str = proxy_property(str, 'StyleName', AccessMode.ReadWrite)
    TextAlignmentType: AcTextAlignmentType = proxy_property('AcTextAlignmentType', 'TextAlignmentType', AccessMode.ReadWrite)
    TextAngleType: int = proxy_property(int, 'TextAngleType', AccessMode.ReadWrite)
    TextBackgroundFill: bool = proxy_property(bool, 'TextBackgroundFill', AccessMode.ReadWrite)
    TextColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'TextColor', AccessMode.ReadWrite)
    TextDirection: AcDrawingDirection = proxy_property('AcDrawingDirection', 'TextDirection', AccessMode.ReadWrite)
    TextFrameDisplay: bool = proxy_property(bool, 'TextFrameDisplay', AccessMode.ReadWrite)
    TextHeight: float = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextJustify: AcAttachmentPoint = proxy_property('AcAttachmentPoint', 'TextJustify', AccessMode.ReadWrite)
    TextLeftAttachmentType: AcTextAttachmentType = proxy_property('AcTextAttachmentType', 'TextLeftAttachmentType', AccessMode.ReadWrite)
    TextLineSpacingDistance: float = proxy_property(float, 'TextLineSpacingDistance', AccessMode.ReadWrite)
    TextLineSpacingFactor: float = proxy_property(float, 'TextLineSpacingFactor', AccessMode.ReadWrite)
    TextLineSpacingStyle: AcLineSpacingStyle = proxy_property('AcLineSpacingStyle', 'TextLineSpacingStyle', AccessMode.ReadWrite)
    TextRightAttachmentType: AcTextAttachmentType = proxy_property('AcTextAttachmentType', 'TextRightAttachmentType', AccessMode.ReadWrite)
    TextRotation: float = proxy_property(float, 'TextRotation', AccessMode.ReadWrite)
    TextString: str = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyleName: str = proxy_property(str, 'TextStyleName', AccessMode.ReadWrite)
    Type: AcMLeaderType = proxy_property('AcMLeaderType', 'Type', AccessMode.ReadWrite)

    def AddLeader(self) -> int:
        return self._obj.AddLeader()

    def AddLeaderLine(self, leaderIndex: int) -> int:
        return self._obj.AddLeaderLine(leaderIndex)

    def AddLeaderLineEx(self, point: PyGePoint3d) -> int:
        return self._obj.AddLeaderLineEx(point())

    def GetBlockAttributeValue(self, attdefId: int) -> str:
        return self._obj.GetBlockAttributeValue(attdefId)

    def GetDoglegDirection(self, leaderIndex: int) -> PyGeVector3d:
        return PyGeVector3d(self._obj.GetDoglegDirection(leaderIndex))

    def GetLeaderIndex(self, leaderLineIndex: int) -> int:
        return self._obj.GetLeaderIndex(leaderLineIndex)

    def GetLeaderLineIndexes(self, leaderIndex: int) -> list:
        return list(self._obj.GetLeaderLineIndexes(leaderIndex))

    def GetLeaderLineVertices(self, leaderLineIndex: int) -> list:
        return list(self._obj.GetLeaderLineVertices(leaderLineIndex))

    def GetTextFrameDisplay(self) -> bool:
        return self._obj.GetTextFrameDisplay()

    def GetVertexCount(self, leaderLineIndex: int) -> int:
        return self._obj.GetVertexCount(leaderLineIndex)

    def RemoveLeader(self, leaderIndex: int) -> None:
        self._obj.RemoveLeader(leaderIndex)

    def RemoveLeaderLine(self, leaderLineIndex: int) -> None:
        self._obj.RemoveLeaderLine(leaderLineIndex)

    def SetBlockAttributeValue(self, attdefId: int, value: str) -> None:
        self._obj.SetBlockAttributeValue(attdefId, value)

    def SetDoglegDirection(self, leaderIndex: int, dir: PyGeVector3d) -> None:
        self._obj.SetDoglegDirection(leaderIndex, dir())

    def SetLeaderLineVertices(self, leaderLineIndex: int, vertices) -> None:
        self._obj.SetLeaderLineVertices(leaderLineIndex, vertices)

    def SetTextFrameDisplay(self, display: bool) -> None:
        self._obj.SetTextFrameDisplay(display)
