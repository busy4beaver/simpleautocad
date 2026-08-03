from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray
from ...Types.Ge import PyGePoint3d, PyGeVector3d


class AcadBlockReference(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    EffectiveName: str = proxy_property(str, 'EffectiveName', AccessMode.ReadOnly)
    HasAttributes: bool = proxy_property(bool, 'HasAttributes', AccessMode.ReadOnly)
    InsertionPoint: PyGePoint3d = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    IsDynamicBlock: bool = proxy_property(bool, 'IsDynamicBlock', AccessMode.ReadOnly)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Rotation: float = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    XScaleFactor: float = proxy_property(float, 'XScaleFactor', AccessMode.ReadWrite)
    YScaleFactor: float = proxy_property(float, 'YScaleFactor', AccessMode.ReadWrite)
    ZScaleFactor: float = proxy_property(float, 'ZScaleFactor', AccessMode.ReadWrite)
    InsUnits: str = proxy_property(str, 'InsUnits', AccessMode.ReadOnly)
    InsUnitsFactor: float = proxy_property(float, 'InsUnitsFactor', AccessMode.ReadOnly)
    Layer: str = proxy_property(str, 'Layer', AccessMode.ReadWrite)
    Linetype: str = proxy_property(str, 'Linetype', AccessMode.ReadWrite)
    LinetypeScale: float = proxy_property(float, 'LinetypeScale', AccessMode.ReadWrite)

    def GetAttributes(self) -> vObjectArray:
        return vObjectArray(self._obj.GetAttributes())

    def GetConstantAttributes(self) -> vObjectArray:
        return vObjectArray(self._obj.GetConstantAttributes())

    def GetDynamicBlockProperties(self) -> vObjectArray:
        return vObjectArray(self._obj.GetDynamicBlockProperties())

    def ResetBlock(self) -> None:
        self._obj.ResetBlock()

    def ConvertToAnonymousBlock(self) -> None:
        self._obj.ConvertToAnonymousBlock()

    def ConvertToStaticBlock(self, newBlockName: str) -> None:
        self._obj.ConvertToStaticBlock(newBlockName)
