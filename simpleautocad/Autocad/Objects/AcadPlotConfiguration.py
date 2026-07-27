from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.Ge import PyGePoint2d, PyGePoint2dArray
from ...Types.VarType import vDoubleArray


class AcadPlotConfiguration(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CanonicalMediaName = proxy_property(str, 'CanonicalMediaName', AccessMode.ReadWrite)
    CenterPlot = proxy_property(bool, 'CenterPlot', AccessMode.ReadWrite)
    ConfigName = proxy_property(str, 'ConfigName', AccessMode.ReadWrite)
    ModelType = proxy_property(bool, 'ModelType', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    PaperUnits = proxy_property('AcPlotPaperUnits', 'PaperUnits', AccessMode.ReadWrite)
    PlotHidden = proxy_property(bool, 'PlotHidden', AccessMode.ReadWrite)
    PlotOrigin = proxy_property('PyGePoint2d', 'PlotOrigin', AccessMode.ReadWrite)
    PlotRotation = proxy_property('AcPlotRotation', 'PlotRotation', AccessMode.ReadWrite)
    PlotType = proxy_property('AcPlotType', 'PlotType', AccessMode.ReadWrite)
    PlotViewportBorders = proxy_property(bool, 'PlotViewportBorders', AccessMode.ReadWrite)
    PlotViewportsFirst = proxy_property(bool, 'PlotViewportsFirst', AccessMode.ReadWrite)
    PlotWithLineweights = proxy_property(bool, 'PlotWithLineweights', AccessMode.ReadWrite)
    PlotWithPlotStyles = proxy_property(bool, 'PlotWithPlotStyles', AccessMode.ReadWrite)
    ScaleLineweights = proxy_property(bool, 'ScaleLineweights', AccessMode.ReadWrite)
    ShowPlotStyles = proxy_property(bool, 'ShowPlotStyles', AccessMode.ReadWrite)
    StandardScale = proxy_property('AcPlotScale', 'StandardScale', AccessMode.ReadWrite)
    StyleSheet = proxy_property(str, 'StyleSheet', AccessMode.ReadWrite)
    UseStandardScale = proxy_property(bool, 'UseStandardScale', AccessMode.ReadWrite)
    ViewToPlot = proxy_property(str, 'ViewToPlot', AccessMode.ReadWrite)

    def CopyFrom(self, SourceObject: 'AcadPlotConfiguration') -> None:
        self._obj.CopyFrom(SourceObject)

    def GetCanonicalMediaNames(self) -> tuple:
        return self._obj.GetCanonicalMediaNames()

    def GetCustomScale(self) -> vDoubleArray:
        Numerator, Denominator = self._obj.GetCustomScale()
        return vDoubleArray(Numerator, Denominator)

    def GetLocaleMediaName(self, Name: str) -> str:
        return self._obj.GetLocaleMediaName(Name)

    def GetPaperMargins(self) -> vDoubleArray:
        LowerLeft, UpperRight = self._obj.GetPaperMargins()
        return vDoubleArray(LowerLeft, UpperRight)

    def GetPaperSize(self) -> tuple:
        Width, Height = self._obj.GetPaperSize()
        return Width, Height

    def GetPlotDeviceNames(self) -> tuple:
        return self._obj.GetPlotDeviceNames()

    def GetPlotStyleTableNames(self) -> tuple:
        return self._obj.GetPlotStyleTableNames()

    def GetWindowToPlot(self) -> PyGePoint2dArray:
        LowerLeft, UpperRight = self._obj.GetWindowToPlot()
        return PyGePoint2dArray(LowerLeft, UpperRight)

    def RefreshPlotDeviceInfo(self) -> None:
        self._obj.RefreshPlotDeviceInfo()

    def SetCustomScale(self, Numerator: float, Denominator: float) -> None:
        self._obj.SetCustomScale(Numerator, Denominator)

    def SetWindowToPlot(self, LowerLeft: PyGePoint2d, UpperRight: PyGePoint2d) -> None:
        self._obj.SetWindowToPlot(LowerLeft(), UpperRight())
