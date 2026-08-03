from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from .AcadAcCmColor import AcadAcCmColor
from ...Types.VarType import Variant
from ...Types.Ac import (
    AcRowType,
    AcCellAlignment,
    AcValueDataType,
    AcValueUnitType,
    AcGridLineType,
    AcLineWeight,
    AcMergeCellStyleOption,
)


class AcadTableStyle(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BitFlags: int = proxy_property(int, 'BitFlags', AccessMode.ReadWrite)
    Description: str = proxy_property(str, 'Description', AccessMode.ReadWrite)
    HeadersSuppressed: bool = proxy_property(bool, 'HeadersSuppressed', AccessMode.ReadWrite)
    HorzCellMargin: float = proxy_property(float, 'HorzCellMargin', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    TitleSuppressed: bool = proxy_property(bool, 'TitleSuppressed', AccessMode.ReadWrite)
    VertCellMargin: float = proxy_property(float, 'VertCellMargin', AccessMode.ReadWrite)

    def CreateCellStyle(self, cellStyle: str) -> None:
        self._obj.CreateCellStyle(cellStyle)

    def CreateCellStyleFromStyle(self, cellStyle: str, sourceCellStyle: str) -> None:
        self._obj.CreateCellStyleFromStyle(cellStyle, sourceCellStyle)

    def DeleteCellStyle(self, cellStyle: str) -> None:
        self._obj.DeleteCellStyle(cellStyle)

    def EnableMergeAll(self, bEnable: bool) -> None:
        self._obj.EnableMergeAll(bEnable)

    def GetAlignment(self, rowTypes: AcRowType) -> AcCellAlignment:
        return AcCellAlignment(self._obj.GetAlignment(rowTypes))

    def GetBackgroundColor(self, rowTypes: AcRowType) -> AcadAcCmColor:
        return AcadAcCmColor(self._obj.GetBackgroundColor(rowTypes))

    def GetBackgroundColorNone(self, rowTypes: AcRowType) -> bool:
        return self._obj.GetBackgroundColorNone(rowTypes)

    def GetCellClass(self, cellStyle: str) -> int:
        return self._obj.GetCellClass(cellStyle)

    def GetCellStyleId(self, cellStyle: str) -> int:
        return self._obj.GetCellStyleId(cellStyle)

    def GetCellType(self, rowTypes: AcRowType) -> int:
        return self._obj.GetCellType(rowTypes)

    def GetColor(self, rowTypes: AcRowType) -> AcadAcCmColor:
        return AcadAcCmColor(self._obj.GetColor(rowTypes))

    def GetDataType(self, rowTypes: AcRowType) -> tuple:
        pDataType, pUnitType = self._obj.GetDataType(rowTypes)
        return AcValueDataType(pDataType), AcValueUnitType(pUnitType)

    def GetFormat(self, rowTypes: AcRowType) -> str:
        return self._obj.GetFormat(rowTypes)

    def GetGridColor(self, gridLineTypes: AcGridLineType, rowTypes: AcRowType) -> AcadAcCmColor:
        return AcadAcCmColor(self._obj.GetGridColor(gridLineTypes, rowTypes))

    def GetGridLineWeight(self, gridLineTypes: AcGridLineType, rowTypes: AcRowType) -> AcLineWeight:
        return AcLineWeight(self._obj.GetGridLineWeight(gridLineTypes, rowTypes))

    def GetGridVisibility(self, gridLineTypes: AcGridLineType, rowTypes: AcRowType) -> bool:
        return self._obj.GetGridVisibility(gridLineTypes, rowTypes)

    def GetIsCellStyleInUse(self, cellStyle: str) -> bool:
        return self._obj.GetIsCellStyleInUse(cellStyle)

    def GetIsMergeAllEnabled(self) -> bool:
        return self._obj.GetIsMergeAllEnabled()

    def GetTextHeight(self, rowTypes: AcRowType) -> float:
        return self._obj.GetTextHeight(rowTypes)

    def GetTextStyle(self, rowTypes: AcRowType) -> str:
        return self._obj.GetTextStyle(rowTypes)

    def GetUniqueCellStyleName(self, baseName: str) -> str:
        return self._obj.GetUniqueCellStyleName(baseName)

    def RenameCellStyle(self, oldName: str, newName: str) -> None:
        self._obj.RenameCellStyle(oldName, newName)

    def SetAlignment(self, rowTypes: AcRowType, cellAlignment: AcCellAlignment) -> None:
        self._obj.SetAlignment(rowTypes, cellAlignment)

    def SetBackgroundColor(self, rowTypes: AcRowType, pColor: AcadAcCmColor) -> None:
        self._obj.SetBackgroundColor(rowTypes, pColor())

    def SetBackgroundColorNone(self, rowTypes: AcRowType, bValue: bool) -> None:
        self._obj.SetBackgroundColorNone(rowTypes, bValue)

    def SetCellClass(self, cellStyle: str, cellClass: int) -> None:
        self._obj.SetCellClass(cellStyle, cellClass)

    def SetColor(self, rowTypes: AcRowType, pColor: AcadAcCmColor) -> None:
        self._obj.SetColor(rowTypes, pColor())

    def SetDataType(self, rowTypes: AcRowType, nDataType: AcValueDataType, nUnitType: AcValueUnitType) -> None:
        self._obj.SetDataType(rowTypes, nDataType, nUnitType)

    def SetFormat(self, rowTypes: AcRowType, pFormat: str) -> None:
        self._obj.SetFormat(rowTypes, pFormat)

    def SetGridColor(self, gridLineTypes: AcGridLineType, rowTypes: AcRowType, pColor: AcadAcCmColor) -> None:
        self._obj.SetGridColor(gridLineTypes, rowTypes, pColor())

    def SetGridLineWeight(self, gridLineTypes: AcGridLineType, rowTypes: AcRowType, Lineweight: AcLineWeight) -> None:
        self._obj.SetGridLineWeight(gridLineTypes, rowTypes, Lineweight)

    def SetGridVisibility(self, gridLineTypes: AcGridLineType, rowTypes: AcRowType, bValue: bool) -> None:
        self._obj.SetGridVisibility(gridLineTypes, rowTypes, bValue)

    def SetTemplateId(self, templateId: int, mergeOption: AcMergeCellStyleOption) -> None:
        self._obj.SetTemplateId(templateId, mergeOption)

    def SetTextHeight(self, rowTypes: AcRowType, TextHeight: float) -> None:
        self._obj.SetTextHeight(rowTypes, TextHeight)

    def SetTextStyle(self, rowTypes: AcRowType, bstrName: str) -> None:
        self._obj.SetTextStyle(rowTypes, bstrName)
