from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray


class AcadBlockReference(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    EffectiveName = proxy_property(str, 'EffectiveName', AccessMode.ReadOnly)
    HasAttributes = proxy_property(bool, 'HasAttributes', AccessMode.ReadOnly)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    InsUnits = proxy_property(str, 'InsUnits', AccessMode.ReadOnly)
    InsUnitsFactor = proxy_property(float, 'InsUnitsFactor', AccessMode.ReadOnly)
    IsDynamicBlock = proxy_property(bool, 'IsDynamicBlock', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    XEffectiveScaleFactor = proxy_property(float, 'XEffectiveScaleFactor', AccessMode.ReadWrite)
    XScaleFactor = proxy_property(float, 'XScaleFactor', AccessMode.ReadWrite)
    YEffectiveScaleFactor = proxy_property(float, 'YEffectiveScaleFactor', AccessMode.ReadWrite)
    YScaleFactor = proxy_property(float, 'YScaleFactor', AccessMode.ReadWrite)
    ZEffectiveScaleFactor = proxy_property(float, 'ZEffectiveScaleFactor', AccessMode.ReadWrite)
    ZScaleFactor = proxy_property(float, 'ZScaleFactor', AccessMode.ReadWrite)

    def ConvertToAnonymousBlock(self) -> None:
        self._obj.ConvertToAnonymousBlock()

    def ConvertToStaticBlock(self, newBlockName: str) -> None:
        self._obj.ConvertToStaticBlock(newBlockName)

    def Copy(self) -> AcadBlockReference:
        return AcadBlockReference(self._obj.Copy())

    def Explode(self) -> vObjectArray:
        return vObjectArray(self._obj.Explode())

    def GetAttributes(self) -> vObjectArray:
        return vObjectArray(self._obj.GetAttributes())

    def GetConstantAttributes(self) -> vObjectArray:
        return vObjectArray(self._obj.GetConstantAttributes())

    def GetDynamicBlockProperties(self) -> vObjectArray:
        return vObjectArray(self._obj.GetDynamicBlockProperties())

    def ResetBlock(self) -> None:
        self._obj.ResetBlock()
