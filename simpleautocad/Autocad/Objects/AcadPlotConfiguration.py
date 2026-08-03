from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadPlotConfiguration(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CanonicalMediaName: str = proxy_property(str, 'CanonicalMediaName', AccessMode.ReadWrite)
    CenterPlot: bool = proxy_property(bool, 'CenterPlot', AccessMode.ReadWrite)
    ConfigName: str = proxy_property(str, 'ConfigName', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    PaperUnits: AcPlotPaperUnits = proxy_property('AcPlotPaperUnits', 'PaperUnits', AccessMode.ReadWrite)
    PlotHidden: bool = proxy_property(bool, 'PlotHidden', AccessMode.ReadWrite)
    PlotOrigin: PyGePoint2d = proxy_property('PyGePoint2d', 'PlotOrigin', AccessMode.ReadWrite)
    PlotRotation: AcPlotRotation = proxy_property('AcPlotRotation', 'PlotRotation', AccessMode.ReadWrite)
    PlotType: AcPlotType = proxy_property('AcPlotType', 'PlotType', AccessMode.ReadWrite)
    PlotViewportBorders: bool = proxy_property(bool, 'PlotViewportBorders', AccessMode.ReadWrite)
    PlotViewportsFirst: bool = proxy_property(bool, 'PlotViewportsFirst', AccessMode.ReadWrite)
    PlotWithLineweights: bool = proxy_property(bool, 'PlotWithLineweights', AccessMode.ReadWrite)
    PlotWithPlotStyles: bool = proxy_property(bool, 'PlotWithPlotStyles', AccessMode.ReadWrite)
    ScaleLineweights: bool = proxy_property(bool, 'ScaleLineweights', AccessMode.ReadWrite)
    ShowPlotStyles: bool = proxy_property(bool, 'ShowPlotStyles', AccessMode.ReadWrite)
    StandardScale: AcPlotScale = proxy_property('AcPlotScale', 'StandardScale', AccessMode.ReadWrite)
    StyleSheet: str = proxy_property(str, 'StyleSheet', AccessMode.ReadWrite)
    UseStandardScale: bool = proxy_property(bool, 'UseStandardScale', AccessMode.ReadWrite)
    ViewToPlot: str = proxy_property(str, 'ViewToPlot', AccessMode.ReadWrite)

    def CopyFrom(self, PlotConfig: AcadPlotConfiguration) -> None:
        self._obj.CopyFrom(PlotConfig())

    def GetCanonicalMediaNames(self) -> list:
        return list(self._obj.GetCanonicalMediaNames())

    def GetCustomScale(self) -> tuple:
        return self._obj.GetCustomScale()

    def GetLocaleMediaName(self, Name: str) -> str:
        return self._obj.GetLocaleMediaName(Name)

    def GetPaperMargins(self) -> tuple:
        return self._obj.GetPaperMargins()

    def GetPaperSize(self) -> tuple:
        return self._obj.GetPaperSize()

    def GetPlotDeviceNames(self) -> list:
        return list(self._obj.GetPlotDeviceNames())

    def GetPlotStyleTableNames(self) -> list:
        return list(self._obj.GetPlotStyleTableNames())

    def GetWindowToPlot(self) -> tuple:
        return self._obj.GetWindowToPlot()

    def RefreshPlotDeviceInfo(self) -> None:
        self._obj.RefreshPlotDeviceInfo()

    def SetCustomScale(self, Numerator: float, Denominator: float) -> None:
        self._obj.SetCustomScale(Numerator, Denominator)

    def SetWindowToPlot(self, LowerLeft: PyGePoint2d, UpperRight: PyGePoint2d) -> None:
        self._obj.SetWindowToPlot(LowerLeft(), UpperRight())
