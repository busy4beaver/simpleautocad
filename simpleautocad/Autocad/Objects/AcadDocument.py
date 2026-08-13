from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.VarType import Variant
from ...Types.Ac import AcActiveSpace, AcWindowState

if TYPE_CHECKING:
    from ..AcadEntity import AcadEntity
    from .AcadApplication import AcadApplication
    from .AcadBlocks import AcadBlocks
    from .AcadDatabase import AcadDatabase
    from .AcadDatabasePreferences import AcadDatabasePreferences
    from .AcadDictionaries import AcadDictionaries
    from .AcadDimStyle import AcadDimStyle
    from .AcadDimStyles import AcadDimStyles
    from .AcadGroups import AcadGroups
    from .AcadLayer import AcadLayer
    from .AcadLayers import AcadLayers
    from .AcadLayout import AcadLayout
    from .AcadLayouts import AcadLayouts
    from .AcadLineType import AcadLineType
    from .AcadLineTypes import AcadLineTypes
    from .AcadMaterial import AcadMaterial
    from .AcadMaterials import AcadMaterials
    from .AcadModelSpace import AcadModelSpace
    from .AcadPaperSpace import AcadPaperSpace
    from .AcadPlot import AcadPlot
    from .AcadPlotConfigurations import AcadPlotConfigurations
    from ..Entities.AcadPViewport import AcadPViewport
    from .AcadRegisteredApplications import AcadRegisteredApplications
    from .AcadSelectionSet import AcadSelectionSet
    from .AcadSelectionSets import AcadSelectionSets
    from .AcadSummaryInfo import AcadSummaryInfo
    from .AcadTextStyle import AcadTextStyle
    from .AcadTextStyles import AcadTextStyles
    from .AcadUCS import AcadUCS
    from .AcadUCSs import AcadUCSs
    from .AcadUtility import AcadUtility
    from .AcadViewport import AcadViewport
    from .AcadViewports import AcadViewports
    from .AcadViews import AcadViews


class AcadDocument(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Active: bool = proxy_property(bool, 'Active', AccessMode.ReadOnly)
    ActiveDimStyle: AcadDimStyle = proxy_property('AcadDimStyle', 'ActiveDimStyle', AccessMode.ReadWrite)
    ActiveLayer: AcadLayer = proxy_property('AcadLayer', 'ActiveLayer', AccessMode.ReadWrite)
    ActiveLayout: AcadLayout = proxy_property('AcadLayout', 'ActiveLayout', AccessMode.ReadWrite)
    ActiveLinetype: AcadLineType = proxy_property('AcadLineType', 'ActiveLinetype', AccessMode.ReadWrite)
    ActiveMaterial: AcadMaterial = proxy_property('AcadMaterial', 'ActiveMaterial', AccessMode.ReadWrite)
    ActivePViewport: AcadPViewport = proxy_property('AcadPViewport', 'ActivePViewport', AccessMode.ReadWrite)
    ActiveSelectionSet: AcadSelectionSet = proxy_property('AcadSelectionSet', 'ActiveSelectionSet', AccessMode.ReadOnly)
    ActiveSpace: AcActiveSpace = proxy_property('AcActiveSpace', 'ActiveSpace', AccessMode.ReadWrite)
    ActiveTextStyle: AcadTextStyle = proxy_property('AcadTextStyle', 'ActiveTextStyle', AccessMode.ReadWrite)
    ActiveUCS: AcadUCS = proxy_property('AcadUCS', 'ActiveUCS', AccessMode.ReadWrite)
    ActiveViewport: AcadViewport = proxy_property('AcadViewport', 'ActiveViewport', AccessMode.ReadWrite)
    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Blocks: AcadBlocks = proxy_property('AcadBlocks', 'Blocks', AccessMode.ReadOnly)
    Database: AcadDatabase = proxy_property('AcadDatabase', 'Database', AccessMode.ReadOnly)
    Dictionaries: AcadDictionaries = proxy_property('AcadDictionaries', 'Dictionaries', AccessMode.ReadOnly)
    DimStyles: AcadDimStyles = proxy_property('AcadDimStyles', 'DimStyles', AccessMode.ReadOnly)
    ElevationModelSpace: float = proxy_property(float, 'ElevationModelSpace', AccessMode.ReadWrite)
    ElevationPaperSpace: float = proxy_property(float, 'ElevationPaperSpace', AccessMode.ReadWrite)
    FullName: str = proxy_property(str, 'FullName', AccessMode.ReadOnly)
    Groups: AcadGroups = proxy_property('AcadGroups', 'Groups', AccessMode.ReadOnly)
    Height: int = proxy_property(int, 'Height', AccessMode.ReadWrite)
    HWND: int = proxy_property(int, 'HWND', AccessMode.ReadOnly)
    Layers: AcadLayers = proxy_property('AcadLayers', 'Layers', AccessMode.ReadOnly)
    Layouts: AcadLayouts = proxy_property('AcadLayouts', 'Layouts', AccessMode.ReadOnly)
    Limits: tuple = proxy_property(tuple, 'Limits', AccessMode.ReadWrite)
    Linetypes: AcadLineTypes = proxy_property('AcadLineTypes', 'Linetypes', AccessMode.ReadOnly)
    Materials: AcadMaterials = proxy_property('AcadMaterials', 'Materials', AccessMode.ReadOnly)
    ModelSpace: AcadModelSpace = proxy_property('AcadModelSpace', 'ModelSpace', AccessMode.ReadOnly)
    MSpace: bool = proxy_property(bool, 'MSpace', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadOnly)
    ObjectSnapMode: bool = proxy_property(bool, 'ObjectSnapMode', AccessMode.ReadWrite)
    PaperSpace: AcadPaperSpace = proxy_property('AcadPaperSpace', 'PaperSpace', AccessMode.ReadOnly)
    Path: str = proxy_property(str, 'Path', AccessMode.ReadOnly)
    Plot: AcadPlot = proxy_property('AcadPlot', 'Plot', AccessMode.ReadOnly)
    PlotConfigurations: AcadPlotConfigurations = proxy_property('AcadPlotConfigurations', 'PlotConfigurations', AccessMode.ReadOnly)
    Preferences: AcadDatabasePreferences = proxy_property('AcadDatabasePreferences', 'Preferences', AccessMode.ReadOnly)
    ReadOnly: bool = proxy_property(bool, 'ReadOnly', AccessMode.ReadOnly)
    RegisteredApplications: AcadRegisteredApplications = proxy_property('AcadRegisteredApplications', 'RegisteredApplications', AccessMode.ReadOnly)
    Saved: bool = proxy_property(bool, 'Saved', AccessMode.ReadOnly)
    SelectionSets: AcadSelectionSets = proxy_property('AcadSelectionSets', 'SelectionSets', AccessMode.ReadOnly)
    SummaryInfo: AcadSummaryInfo = proxy_property('AcadSummaryInfo', 'SummaryInfo', AccessMode.ReadOnly)
    TextStyles: AcadTextStyles = proxy_property('AcadTextStyles', 'TextStyles', AccessMode.ReadOnly)
    UserCoordinateSystems: AcadUCSs = proxy_property('AcadUCSs', 'UserCoordinateSystems', AccessMode.ReadOnly)
    Utility: AcadUtility = proxy_property('AcadUtility', 'Utility', AccessMode.ReadOnly)
    Viewports: AcadViewports = proxy_property('AcadViewports', 'Viewports', AccessMode.ReadOnly)
    Views: AcadViews = proxy_property('AcadViews', 'Views', AccessMode.ReadOnly)
    Width: int = proxy_property(int, 'Width', AccessMode.ReadWrite)
    WindowState: AcWindowState = proxy_property('AcWindowState', 'WindowState', AccessMode.ReadWrite)
    WindowTitle: str = proxy_property(str, 'WindowTitle', AccessMode.ReadOnly)

    def Activate(self) -> None:
        self._obj.Activate()

    def AuditInfo(self, FixErr: bool) -> None:
        self._obj.AuditInfo(FixErr)

    def Close(self, SaveChanges: bool = None, FileName: str = None) -> None:
        if SaveChanges is None and FileName is None:
            self._obj.Close()
        elif FileName is None:
            self._obj.Close(SaveChanges)
        else:
            self._obj.Close(SaveChanges if SaveChanges is not None else True, FileName)

    def EndUndoMark(self) -> None:
        self._obj.EndUndoMark()

    def Export(self, FileName: str, Extension: str, SelectionSet: AcadSelectionSet) -> None:
        self._obj.Export(FileName, Extension, SelectionSet())

    def GetVariable(self, Name: str) -> Variant:
        return Variant(self._obj.GetVariable(Name))

    def HandleToObject(self, Handle: str) -> AcadObject:
        return AcadObject(self._obj.HandleToObject(Handle))

    def Import(self, FileName: str, InsertionPoint: Variant, ScaleFactor: float) -> AcadEntity:
        from ..AcadEntity import AcadEntity
        return AcadEntity(self._obj.Import(FileName, InsertionPoint, ScaleFactor))

    def LoadShapeFile(self, FullName: str) -> None:
        self._obj.LoadShapeFile(FullName)

    def New(self, TemplateFileName: str) -> AcadDocument:
        return AcadDocument(self._obj.New(TemplateFileName))

    def ObjectIdToObject(self, ObjectID: int) -> AcadObject:
        return AcadObject(self._obj.ObjectIdToObject(ObjectID))

    def Open(self, FullName: str, ReadOnly: bool = False, Password: str = None) -> AcadDocument:
        if Password is None:
            return AcadDocument(self._obj.Open(FullName, ReadOnly))
        return AcadDocument(self._obj.Open(FullName, ReadOnly, Password))

    def PurgeAll(self) -> None:
        self._obj.PurgeAll()

    def Regen(self, WhichViewports: int) -> None:
        self._obj.Regen(WhichViewports)

    def Save(self) -> None:
        self._obj.Save()

    def SaveAs(self, FullFileName: str, SaveAsType: Variant = None, SecurityParams: Variant = None) -> None:
        if SaveAsType is None and SecurityParams is None:
            self._obj.SaveAs(FullFileName)
        elif SecurityParams is None:
            self._obj.SaveAs(FullFileName, SaveAsType)
        else:
            self._obj.SaveAs(FullFileName, SaveAsType, SecurityParams)

    def SendCommand(self, Command: str) -> None:
        self._obj.SendCommand(Command)

    def SetVariable(self, Name: str, Value: Variant) -> None:
        self._obj.SetVariable(Name, Value)

    def StartUndoMark(self) -> None:
        self._obj.StartUndoMark()

    def Wblock(self, FileName: str, SelectionSet: AcadSelectionSet) -> None:
        self._obj.Wblock(FileName, SelectionSet())
