from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadDatabase import AcadDatabase, IAcadDatabase
from .AcadUCS import AcadUCS
from ...Types.Ac import AcActiveSpace, AcWindowState, AcRegenType, AcSaveAsType
from ...Types.Ge import PyGePoint3d
from ...Types.VarType import Variant


class AcadDocument(AcadDatabase):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Active = proxy_property(bool, 'Active', AccessMode.ReadOnly)
    ActiveDimStyle = proxy_property('AcadDimStyle', 'ActiveDimStyle', AccessMode.ReadWrite)
    ActiveLayer = proxy_property('AcadLayer', 'ActiveLayer', AccessMode.ReadWrite)
    ActiveLayout = proxy_property('AcadLayout', 'ActiveLayout', AccessMode.ReadWrite)
    ActiveLinetype = proxy_property('AcadLineType', 'ActiveLinetype', AccessMode.ReadWrite)
    ActiveMaterial = proxy_property('AcadMaterial', 'ActiveMaterial', AccessMode.ReadWrite)
    ActivePViewport = proxy_property('AcadPViewport', 'ActivePViewport', AccessMode.ReadWrite)
    ActiveSelectionSet = proxy_property('AcadSelectionSet', 'ActiveSelectionSet', AccessMode.ReadOnly)
    ActiveSpace = proxy_property('AcActiveSpace', 'ActiveSpace', AccessMode.ReadWrite)
    ActiveTextStyle = proxy_property('AcadTextStyle', 'ActiveTextStyle', AccessMode.ReadWrite)
    ActiveUCS = proxy_property('AcadUCS', 'ActiveUCS', AccessMode.ReadWrite)
    ActiveViewport = proxy_property('AcadViewport', 'ActiveViewport', AccessMode.ReadWrite)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Database = proxy_property('IAcadDatabase', 'Database', AccessMode.ReadOnly)
    FullName = proxy_property(str, 'FullName', AccessMode.ReadOnly)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    HWND = proxy_property(int, 'HWND', AccessMode.ReadOnly)
    MSpace = proxy_property(bool, 'MSpace', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadOnly)
    ObjectSnapMode = proxy_property(bool, 'ObjectSnapMode', AccessMode.ReadWrite)
    Path = proxy_property(str, 'Path', AccessMode.ReadOnly)
    PickfirstSelectionSet = proxy_property('AcadSelectionSet', 'PickfirstSelectionSet', AccessMode.ReadOnly)
    Plot = proxy_property('AcadPlot', 'Plot', AccessMode.ReadOnly)
    ReadOnly = proxy_property(bool, 'ReadOnly', AccessMode.ReadOnly)
    Saved = proxy_property(bool, 'Saved', AccessMode.ReadOnly)
    SelectionSets = proxy_property('AcadSelectionSets', 'SelectionSets', AccessMode.ReadOnly)
    SummaryInfo = proxy_property('AcadSummaryInfo', 'SummaryInfo', AccessMode.ReadOnly)
    Utility = proxy_property('AcadUtility', 'Utility', AccessMode.ReadOnly)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)
    WindowState = proxy_property('AcWindowState', 'WindowState', AccessMode.ReadWrite)
    WindowTitle = proxy_property(str, 'WindowTitle', AccessMode.ReadOnly)

    def Activate(self) -> None:
        self._obj.Activate()

    def AuditInfo(self, FixError: bool) -> None:
        self._obj.AuditInfo(FixError)

    def Close(self, SaveChanges: bool = False, FileName: str = '') -> None:
        self._obj.Close(SaveChanges, FileName)

    def EndUndoMark(self) -> None:
        self._obj.EndUndoMark()

    def Export(self, FileName: str, Extension: str, SelectionSet) -> None:
        self._obj.Export(FileName, Extension, SelectionSet)

    def GetVariable(self, Name: str):
        return self._obj.GetVariable(Name)

    def Import(self, FileName: str, InsertionPoint: PyGePoint3d, ScaleFactor: float):
        from ..Entities.AcadBlockReference import AcadBlockReference
        ref = self._obj.Import(FileName, InsertionPoint(), ScaleFactor)
        return AcadBlockReference(ref) if ref else None

    def LoadShapeFile(self, FullName: str) -> None:
        self._obj.LoadShapeFile(FullName)

    def New(self, TemplateFileName: str) -> AcadDocument:
        return AcadDocument(self._obj.New(TemplateFileName))

    def Open(self, Name: str, ReadOnly: bool = False):
        return self._obj.Open(Name, ReadOnly)

    def PostCommand(self, Command: str) -> None:
        self._obj.PostCommand(Command)

    def PurgeAll(self) -> None:
        self._obj.PurgeAll()

    def Regen(self, WhichViewports: AcRegenType) -> None:
        self._obj.Regen(WhichViewports)

    def Save(self) -> None:
        self._obj.Save()

    def SaveAs(
        self,
        FileName: str,
        FileType: AcSaveAsType = AcSaveAsType.acNative,
        SecurityParams=None,
    ) -> None:
        if SecurityParams is None:
            self._obj.SaveAs(FileName, FileType)
        else:
            raise Exception('AcadSecurityParams не поддерживается')

    def SendCommand(self, Command: str) -> None:
        self._obj.SendCommand(Command)

    def SetVariable(self, Name: str, Value: Variant) -> None:
        self._obj.SetVariable(Name, Value())

    def StartUndoMark(self) -> None:
        self._obj.StartUndoMark()

    def WBlock(self, FileName: str, SelectionSet) -> None:
        self._obj.WBlock(FileName, SelectionSet)
