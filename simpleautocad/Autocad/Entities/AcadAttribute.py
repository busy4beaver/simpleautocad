from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadAttribute(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Alignment = proxy_property('AcAlignment', 'Alignment', AccessMode.ReadWrite)
    Backward = proxy_property(bool, 'Backward', AccessMode.ReadWrite)
    Constant = proxy_property(bool, 'Constant', AccessMode.ReadWrite)
    FieldLength = proxy_property(int, 'FieldLength', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    Invisible = proxy_property(bool, 'Invisible', AccessMode.ReadWrite)
    LockPosition = proxy_property(bool, 'LockPosition', AccessMode.ReadWrite)
    Mode = proxy_property('AcAttributeMode', 'Mode', AccessMode.ReadWrite)
    MTextAttribute = proxy_property(bool, 'MTextAttribute', AccessMode.ReadWrite)
    MTextAttributeContent = proxy_property(str, 'MTextAttributeContent', AccessMode.ReadWrite)
    MTextBoundaryWidth = proxy_property(float, 'MTextBoundaryWidth', AccessMode.ReadWrite)
    MTextDrawingDirection = proxy_property('AcDrawingDirection', 'MTextDrawingDirection', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ObliqueAngle = proxy_property(float, 'ObliqueAngle', AccessMode.ReadWrite)
    Preset = proxy_property(bool, 'Preset', AccessMode.ReadWrite)
    PromptString = proxy_property(str, 'PromptString', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    StyleName = proxy_property(str, 'StyleName', AccessMode.ReadWrite)
    TagString = proxy_property(str, 'TagString', AccessMode.ReadWrite)
    TextAlignmentPoint = proxy_property('PyGePoint3d', 'TextAlignmentPoint', AccessMode.ReadWrite)
    TextGenerationFlag = proxy_property('AcTextGenerationFlag', 'TextGenerationFlag', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)
    UpsideDown = proxy_property(bool, 'UpsideDown', AccessMode.ReadWrite)
    Verify = proxy_property(bool, 'Verify', AccessMode.ReadWrite)

    def Copy(self) -> AcadAttribute:
        return AcadAttribute(self._obj.Copy())

    def UpdateMTextAttribute(self) -> None:
        self._obj.UpdateMTextAttribute()
