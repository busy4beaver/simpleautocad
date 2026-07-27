from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesFiles(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ActiveInvProject = proxy_property(str, 'ActiveInvProject', AccessMode.ReadWrite)
    AltFontFile = proxy_property(str, 'AltFontFile', AccessMode.ReadWrite)
    AltTabletMenuFile = proxy_property(str, 'AltTabletMenuFile', AccessMode.ReadWrite)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    AutoSavePath = proxy_property(str, 'AutoSavePath', AccessMode.ReadWrite)
    ColorBookPath = proxy_property(str, 'ColorBookPath', AccessMode.ReadWrite)
    ConfigFile = proxy_property(str, 'ConfigFile', AccessMode.ReadOnly)
    CustomDictionary = proxy_property(str, 'CustomDictionary', AccessMode.ReadWrite)
    CustomIconPath = proxy_property(str, 'CustomIconPath', AccessMode.ReadWrite)
    DefaultInternetURL = proxy_property(str, 'DefaultInternetURL', AccessMode.ReadWrite)
    DriversPath = proxy_property(str, 'DriversPath', AccessMode.ReadWrite)
    EnterpriseMenuFile = proxy_property(str, 'EnterpriseMenuFile', AccessMode.ReadWrite)
    FontFileMap = proxy_property(str, 'FontFileMap', AccessMode.ReadWrite)
    HelpFilePath = proxy_property(str, 'HelpFilePath', AccessMode.ReadWrite)
    LogFilePath = proxy_property(str, 'LogFilePath', AccessMode.ReadWrite)
    MainDictionary = proxy_property(str, 'MainDictionary', AccessMode.ReadWrite)
    MenuFile = proxy_property(str, 'MenuFile', AccessMode.ReadWrite)
    PageSetupOverridesTemplateFile = proxy_property(str, 'PageSetupOverridesTemplateFile', AccessMode.ReadWrite)
    PlotLogFilePath = proxy_property(str, 'PlotLogFilePath', AccessMode.ReadWrite)
    PostScriptPrologFile = proxy_property(str, 'PostScriptPrologFile', AccessMode.ReadWrite)
    PrinterConfigPath = proxy_property(str, 'PrinterConfigPath', AccessMode.ReadWrite)
    PrinterDescPath = proxy_property(str, 'PrinterDescPath', AccessMode.ReadWrite)
    PrinterStyleSheetPath = proxy_property(str, 'PrinterStyleSheetPath', AccessMode.ReadWrite)
    PrintFile = proxy_property(str, 'PrintFile', AccessMode.ReadWrite)
    PrintSpoolerPath = proxy_property(str, 'PrintSpoolerPath', AccessMode.ReadWrite)
    PrintSpoolExecutable = proxy_property(str, 'PrintSpoolExecutable', AccessMode.ReadWrite)
    QNewTemplateFile = proxy_property(str, 'QNewTemplateFile', AccessMode.ReadWrite)
    SupportPath = proxy_property(str, 'SupportPath', AccessMode.ReadWrite)
    TempFilePath = proxy_property(str, 'TempFilePath', AccessMode.ReadWrite)
    TemplateDWGPath = proxy_property(str, 'TemplateDWGPath', AccessMode.ReadWrite)
    TempXRefPath = proxy_property(str, 'TempXRefPath', AccessMode.ReadWrite)
    TextEditor = proxy_property(str, 'TextEditor', AccessMode.ReadWrite)
    TextureMapPath = proxy_property(str, 'TextureMapPath', AccessMode.ReadWrite)
    ToolPalettePath = proxy_property(str, 'ToolPalettePath', AccessMode.ReadWrite)
    WorkspacePath = proxy_property(str, 'WorkspacePath', AccessMode.ReadWrite)

    def GetProjectFilePath(self, ProjectName: str):
        return self._obj.GetProjectFilePath(ProjectName)

    def SetProjectFilePath(self, ProjectName: str, ProjectFilePath: str) -> None:
        self._obj.SetProjectFilePath(ProjectName, ProjectFilePath)
