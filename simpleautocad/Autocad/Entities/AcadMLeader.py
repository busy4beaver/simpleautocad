from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3dArray, PyGeVector3d
from ...Types.VarType import vDoubleArray
from .AcadLeader import AcadLeader


class AcadMLeader(AcadEntity):
    def __init__(self, obj, leaderLineIndex=0) -> None:
        self.leaderLineIndex = leaderLineIndex
        super().__init__(obj)

    ArrowheadBlock = proxy_property(str, 'ArrowheadBlock', AccessMode.ReadWrite)
    ArrowheadSize = proxy_property(float, 'ArrowheadSize', AccessMode.ReadWrite)
    ArrowheadType = proxy_property('AcDimArrowheadType', 'ArrowheadType', AccessMode.ReadWrite)
    BlockConnectionType = proxy_property('AcBlockConnectionType', 'BlockConnectionType', AccessMode.ReadWrite)
    BlockScale = proxy_property(int, 'BlockScale', AccessMode.ReadWrite)
    ContentBlockName = proxy_property(str, 'ContentBlockName', AccessMode.ReadWrite)
    ContentBlockType = proxy_property('AcPredefBlockType', 'ContentBlockType', AccessMode.ReadWrite)
    ContentType = proxy_property('AcMLeaderContentType', 'ContentType', AccessMode.ReadWrite)
    DogLegged = proxy_property(bool, 'DogLegged', AccessMode.ReadWrite)
    DoglegLength = proxy_property(float, 'DoglegLength', AccessMode.ReadWrite)
    LandingGap = proxy_property(float, 'LandingGap', AccessMode.ReadWrite)
    LeaderCount = proxy_property(int, 'LeaderCount', AccessMode.ReadOnly)
    LeaderLineColor = proxy_property('AcadAcCmColor', 'LeaderLineColor', AccessMode.ReadWrite)
    LeaderLinetype = proxy_property(str, 'LeaderLinetype', AccessMode.ReadWrite)
    LeaderLineWeight = proxy_property('AcLineWeight', 'LeaderLineWeight', AccessMode.ReadWrite)
    LeaderType = proxy_property('AcMLeaderType', 'LeaderType', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    StyleName = proxy_property(str, 'StyleName', AccessMode.ReadWrite)
    TextAttachmentDirection = proxy_property('AcTextAttachmentDirection', 'TextAttachmentDirection', AccessMode.ReadWrite)
    TextBackgroundFill = proxy_property(bool, 'TextBackgroundFill', AccessMode.ReadWrite)
    TextBottomAttachmentType = proxy_property('AcVerticalTextAttachmentType', 'TextBottomAttachmentType', AccessMode.ReadWrite)
    TextDirection = proxy_property('AcDrawingDirection', 'TextDirection', AccessMode.ReadWrite)
    TextFrameDisplay = proxy_property(bool, 'TextFrameDisplay', AccessMode.ReadWrite)
    TextHeight = proxy_property(float, 'TextHeight', AccessMode.ReadWrite)
    TextJustify = proxy_property('AcAttachmentPoint', 'TextJustify', AccessMode.ReadWrite)
    TextLeftAttachmentType = proxy_property('AcTextAttachmentType', 'TextLeftAttachmentType', AccessMode.ReadWrite)
    TextLineSpacingDistance = proxy_property(float, 'TextLineSpacingDistance', AccessMode.ReadWrite)
    TextLineSpacingFactor = proxy_property(float, 'TextLineSpacingFactor', AccessMode.ReadWrite)
    TextLineSpacingStyle = proxy_property('AcLineSpacingStyle', 'TextLineSpacingStyle', AccessMode.ReadWrite)
    TextRightAttachmentType = proxy_property('AcTextAttachmentType', 'TextRightAttachmentType', AccessMode.ReadWrite)
    TextRotation = proxy_property(float, 'TextRotation', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    TextStyleName = proxy_property(str, 'TextStyleName', AccessMode.ReadWrite)
    TextTopAttachmentType = proxy_property('AcVerticalTextAttachmentType', 'TextTopAttachmentType', AccessMode.ReadWrite)
    TextWidth = proxy_property(float, 'TextWidth', AccessMode.ReadWrite)
    Type = proxy_property('AcLeaderType', 'Type', AccessMode.ReadWrite)

    def AddLeader(self) -> AcadLeader:
        return AcadLeader(self._obj.AddLeader())

    def AddLeaderLine(self, leaderIndex: int, pointArray: PyGePoint3dArray) -> int:
        return self._obj.AddLeaderLine(leaderIndex, pointArray())

    def AddLeaderLineEx(self, pointArray: PyGePoint3dArray) -> int:
        return self._obj.AddLeaderLineEx(pointArray())

    def Evaluate(self) -> None:
        self._obj.Evaluate()

    def GetBlockAttributeValue(self, attdefId: int) -> str:
        return self._obj.GetBlockAttributeValue(attdefId)

    def GetDoglegDirection(self, leaderIndex: int) -> PyGeVector3d:
        return PyGeVector3d(self._obj.GetDoglegDirection(leaderIndex))

    def GetLeaderIndex(self, leaderLineIndex: int) -> int:
        return self._obj.GetLeaderIndex(leaderLineIndex)

    def GetLeaderLineIndexes(self, leaderIndex: int) -> vDoubleArray:
        return vDoubleArray(self._obj.GetLeaderLineIndexes(leaderIndex))

    def GetLeaderLineVertices(self, leaderLineIndex: int) -> PyGePoint3dArray:
        return PyGePoint3dArray(self._obj.GetLeaderLineVertices(leaderLineIndex))

    def GetVertexCount(self, leaderLineIndex: int) -> int:
        return self._obj.GetVertexCount(leaderLineIndex)

    def RemoveLeader(self, leaderIndex: int) -> None:
        self._obj.RemoveLeader(leaderIndex)

    def RemoveLeaderLine(self, leaderLineIndex: int) -> None:
        self._obj.RemoveLeaderLine(leaderLineIndex)

    def SetBlockAttributeValue(self, attdefId: int, value: str) -> None:
        self._obj.SetBlockAttributeValue(attdefId, value)

    def SetDoglegDirection(self, leaderIndex: int, dirVec: vDoubleArray) -> None:
        self._obj.SetDoglegDirection(leaderIndex, dirVec())

    def SetLeaderLineVertices(self, leaderLineIndex: int, pointArray: PyGePoint3dArray) -> None:
        self._obj.SetLeaderLineVertices(leaderLineIndex, pointArray())
