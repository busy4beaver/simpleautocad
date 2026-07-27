from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadMtext(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AttachmentPoint = proxy_property('AcAttachmentPoint', 'AttachmentPoint', AccessMode.ReadWrite)
    BackgroundFill = proxy_property(bool, 'BackgroundFill', AccessMode.ReadWrite)
    DrawingDirection = proxy_property('AcDrawingDirection', 'DrawingDirection', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    LineSpacingDistance = proxy_property(float, 'LineSpacingDistance', AccessMode.ReadWrite)
    LineSpacingFactor = proxy_property(float, 'LineSpacingFactor', AccessMode.ReadWrite)
    LineSpacingStyle = proxy_property('AcLineSpacingStyle', 'LineSpacingStyle', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def FieldCode(self) -> str:
        return self._obj.FieldCode()

    def Copy(self) -> AcadMtext:
        return AcadMtext(self._obj.Copy())
