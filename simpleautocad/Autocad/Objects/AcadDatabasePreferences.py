from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadDatabasePreferences(AppObject):
    def __init__(self, obj):
        super().__init__(obj)

    AllowLongSymbolNames = proxy_property(bool, 'AllowLongSymbolNames', AccessMode.ReadWrite)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    ContourLinesPerSurface = proxy_property(int, 'ContourLinesPerSurface', AccessMode.ReadWrite)
    DisplaySilhouette = proxy_property(bool, 'DisplaySilhouette', AccessMode.ReadWrite)
    Lineweight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    LineweightDisplay = proxy_property(bool, 'LineweightDisplay', AccessMode.ReadWrite)
    ObjectSortByPlotting = proxy_property(bool, 'ObjectSortByPlotting', AccessMode.ReadWrite)
    ObjectSortByPSOutput = proxy_property(bool, 'ObjectSortByPSOutput', AccessMode.ReadWrite)
    ObjectSortByRedraws = proxy_property(bool, 'ObjectSortByRedraws', AccessMode.ReadWrite)
    ObjectSortByRegens = proxy_property(bool, 'ObjectSortByRegens', AccessMode.ReadWrite)
    ObjectSortBySelection = proxy_property(bool, 'ObjectSortBySelection', AccessMode.ReadWrite)
    ObjectSortBySnap = proxy_property(bool, 'ObjectSortBySnap', AccessMode.ReadWrite)
    OLELaunch = proxy_property(bool, 'OLELaunch', AccessMode.ReadWrite)
    RenderSmoothness = proxy_property(float, 'RenderSmoothness', AccessMode.ReadWrite)
    SegmentPerPolyline = proxy_property(int, 'SegmentPerPolyline', AccessMode.ReadWrite)
    SolidFill = proxy_property(bool, 'SolidFill', AccessMode.ReadWrite)
    TextFrameDisplay = proxy_property(bool, 'TextFrameDisplay', AccessMode.ReadWrite)
    XRefEdit = proxy_property(bool, 'XRefEdit', AccessMode.ReadWrite)
    XRefLayerVisibility = proxy_property(bool, 'XRefLayerVisibility', AccessMode.ReadWrite)
