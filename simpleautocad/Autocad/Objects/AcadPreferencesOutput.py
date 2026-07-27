from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesOutput(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    AutomaticPlotLog = proxy_property(bool, 'AutomaticPlotLog', AccessMode.ReadWrite)
    ContinuousPlotLog = proxy_property(bool, 'ContinuousPlotLog', AccessMode.ReadWrite)
    DefaultOutputDevice = proxy_property(bool, 'DefaultOutputDevice', AccessMode.ReadWrite)
    DefaultPlotStyleForLayer = proxy_property(str, 'DefaultPlotStyleForLayer', AccessMode.ReadWrite)
    DefaultPlotStyleForObjects = proxy_property(str, 'DefaultPlotStyleForObjects', AccessMode.ReadWrite)
    DefaultPlotStyleTable = proxy_property(str, 'DefaultPlotStyleTable', AccessMode.ReadWrite)
    DefaultPlotToFilePath = proxy_property(str, 'DefaultPlotToFilePath', AccessMode.ReadWrite)
    OLEQuality = proxy_property('AcOleQuality', 'OLEQuality', AccessMode.ReadWrite)
    PlotLegacy = proxy_property(bool, 'PlotLegacy', AccessMode.ReadWrite)
    PlotPolicy = proxy_property('AcPlotPolicy', 'PlotPolicy', AccessMode.ReadWrite)
    PrinterPaperSizeAlert = proxy_property(bool, 'PrinterPaperSizeAlert', AccessMode.ReadWrite)
    UseLastPlotSettings = proxy_property(bool, 'UseLastPlotSettings', AccessMode.ReadWrite)
