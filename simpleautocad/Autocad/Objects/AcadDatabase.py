from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from ...Types.VarType import vObjectArray, vObjectEmpty, vObject
from .AcadBlocks import AcadBlocks
from .AcadDictionaries import AcadDictionaries
from .AcadDimStyles import AcadDimStyles
from .AcadGroups import AcadGroups
from .AcadLayers import AcadLayers
from .AcadLayouts import AcadLayouts
from .AcadLineTypes import AcadLineTypes
from .AcadMaterials import AcadMaterials
from .AcadModelSpace import AcadModelSpace
from .AcadPaperSpace import AcadPaperSpace
from .AcadPlotConfigurations import AcadPlotConfigurations
from .AcadDatabasePreferences import AcadDatabasePreferences
from .AcadRegisteredApplications import AcadRegisteredApplications
from .AcadSectionManager import AcadSectionManager
from .AcadSummaryInfo import AcadSummaryInfo
from .AcadTextStyles import AcadTextStyles
from .AcadUCSs import AcadUCSs
from .AcadViewports import AcadViewports
from .AcadViews import AcadViews


class AcadDatabase(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Blocks = proxy_property('AcadBlocks', 'Blocks', AccessMode.ReadOnly)
    Dictionaries = proxy_property('AcadDictionaries', 'Dictionaries', AccessMode.ReadOnly)
    DimStyles = proxy_property('AcadDimStyles', 'DimStyles', AccessMode.ReadOnly)
    ElevationModelSpace = proxy_property(float, 'ElevationModelSpace', AccessMode.ReadWrite)
    ElevationPaperSpace = proxy_property(float, 'ElevationPaperSpace', AccessMode.ReadWrite)
    Groups = proxy_property('AcadGroups', 'Groups', AccessMode.ReadOnly)
    Layers = proxy_property('AcadLayers', 'Layers', AccessMode.ReadOnly)
    Layouts = proxy_property('AcadLayouts', 'Layouts', AccessMode.ReadOnly)
    Limits = proxy_property('vDoubleArray', 'Limits', AccessMode.ReadWrite)
    Linetypes = proxy_property('AcadLineTypes', 'Linetypes', AccessMode.ReadOnly)
    Materials = proxy_property('AcadMaterials', 'Materials', AccessMode.ReadOnly)
    ModelSpace = proxy_property('AcadModelSpace', 'ModelSpace', AccessMode.ReadOnly)
    PaperSpace = proxy_property('AcadPaperSpace', 'PaperSpace', AccessMode.ReadOnly)
    PlotConfigurations = proxy_property('AcadPlotConfigurations', 'PlotConfigurations', AccessMode.ReadOnly)
    Preferences = proxy_property('AcadDatabasePreferences', 'Preferences', AccessMode.ReadOnly)
    RegisteredApplications = proxy_property('AcadRegisteredApplications', 'RegisteredApplications', AccessMode.ReadOnly)
    SectionManager = proxy_property('AcadSectionManager', 'SectionManager', AccessMode.ReadOnly)
    SummaryInfo = proxy_property('AcadSummaryInfo', 'SummaryInfo', AccessMode.ReadOnly)
    TextStyles = proxy_property('AcadTextStyles', 'TextStyles', AccessMode.ReadOnly)
    UserCoordinateSystems = proxy_property('AcadUCSs', 'UserCoordinateSystems', AccessMode.ReadOnly)
    Viewports = proxy_property('AcadViewports', 'Viewports', AccessMode.ReadOnly)
    Views = proxy_property('AcadViews', 'Views', AccessMode.ReadOnly)

    def CopyObjects(self, Objects: vObjectArray, Owner: vObject = None) -> vObjectArray:
        IDPairs = vObjectEmpty
        return vObjectArray(self._obj.CopyObjects(Objects, Owner(), IDPairs()))

    def HandleToObject(self, Handle: str) -> AppObject:
        return AppObject(self._obj.HandleToObject(Handle))

    def ObjectIdToObject(self, ID: int) -> AppObject:
        return AppObject(self._obj.ObjectIDToObject(ID))


class IAcadDatabase(AcadDatabase):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
