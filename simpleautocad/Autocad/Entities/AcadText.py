from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadText(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Alignment = proxy_property('AcAlignment', 'Alignment', AccessMode.ReadWrite)
    Backward = proxy_property(bool, 'Backward', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ObliqueAngle = proxy_property(float, 'ObliqueAngle', AccessMode.ReadWrite)
    TextAlignmentPoint = proxy_property('PyGePoint3d', 'TextAlignmentPoint', AccessMode.ReadWrite)
    TextGenerationFlag = proxy_property('AcTextGenerationFlag', 'TextGenerationFlag', AccessMode.ReadWrite)
    TextString = proxy_property(str, 'TextString', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)
    UpsideDown = proxy_property(bool, 'UpsideDown', AccessMode.ReadWrite)

    def Copy(self) -> AcadText:
        return AcadText(self._obj.Copy())

    def FieldCode(self) -> str:
        return self._obj.FieldCode()
