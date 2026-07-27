from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ..AcadEntity import AcadEntity
from ...Types.VarType import vObjectArray


class AcadSortentsTable(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Block(self):
        from .AcadBlock import AcadBlock
        return AcadBlock(self._obj.Block)

    def GetFullDrawOrder(self, honorSortentsSysvar: bool) -> vObjectArray:
        Objects = self._obj.GetFullDrawOrder(honorSortentsSysvar)
        return vObjectArray(Objects)

    def GetRelativeDrawOrder(self, honorSortentsSysvar: bool) -> vObjectArray:
        Objects = self._obj.GetRelativeDrawOrder(honorSortentsSysvar)
        return vObjectArray(Objects)

    def MoveAbove(self, Target: AcadEntity) -> vObjectArray:
        Objects = self._obj.MoveAbove(Target())
        return vObjectArray(Objects)

    def MoveBelow(self, Target: AcadEntity) -> vObjectArray:
        Objects = self._obj.MoveBelow(Target())
        return vObjectArray(Objects)

    def MoveToBottom(self, Objects: vObjectArray) -> None:
        self._obj.MoveToBottom(Objects())

    def MoveToTop(self, Objects: vObjectArray) -> None:
        self._obj.MoveToTop(Objects())

    def SetRelativeDrawOrder(self, Objects: vObjectArray) -> None:
        self._obj.SetRelativeDrawOrder(Objects())

    def SwapOrder(self, Object1: AcadEntity, Object2: AcadEntity) -> None:
        self._obj.SwapOrder(Object1(), Object2())
