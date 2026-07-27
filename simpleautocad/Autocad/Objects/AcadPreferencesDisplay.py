from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesDisplay(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    AutoTrackingVecColor = proxy_property('OLE_COLOR', 'AutoTrackingVecColor', AccessMode.ReadWrite)
    CursorSize = proxy_property(int, 'CursorSize', AccessMode.ReadWrite)
    DisplayLayoutTabs = proxy_property(bool, 'DisplayLayoutTabs', AccessMode.ReadWrite)
    DisplayScreenMenu = proxy_property(bool, 'DisplayScreenMenu', AccessMode.ReadWrite)
    DisplayScrollBars = proxy_property(bool, 'DisplayScrollBars', AccessMode.ReadWrite)
    DockedVisibleLines = proxy_property(int, 'DockedVisibleLines', AccessMode.ReadWrite)
    GraphicsWinLayoutBackgrndColor = proxy_property('OLE_COLOR', 'GraphicsWinLayoutBackgrndColor', AccessMode.ReadWrite)
    GraphicsWinModelBackgrndColor = proxy_property('OLE_COLOR', 'GraphicsWinModelBackgrndColor', AccessMode.ReadWrite)
    HistoryLines = proxy_property(int, 'HistoryLines', AccessMode.ReadWrite)
    ImageFrameHighlight = proxy_property(bool, 'ImageFrameHighlight', AccessMode.ReadWrite)
    LayoutCreateViewport = proxy_property(bool, 'LayoutCreateViewport', AccessMode.ReadWrite)
    LayoutCrosshairColor = proxy_property('OLE_COLOR', 'LayoutCrosshairColor', AccessMode.ReadWrite)
    LayoutDisplayMargins = proxy_property(bool, 'LayoutDisplayMargins', AccessMode.ReadWrite)
    LayoutDisplayPaper = proxy_property(bool, 'LayoutDisplayPaper', AccessMode.ReadWrite)
    LayoutDisplayPaperShadow = proxy_property(bool, 'LayoutDisplayPaperShadow', AccessMode.ReadWrite)
    MaxAutoCADWindow = proxy_property(bool, 'MaxAutoCADWindow', AccessMode.ReadWrite)
    ModelCrosshairColor = proxy_property('OLE_COLOR', 'ModelCrosshairColor', AccessMode.ReadWrite)
    ShowRasterImage = proxy_property(bool, 'ShowRasterImage', AccessMode.ReadWrite)
    TextFont = proxy_property(str, 'TextFont', AccessMode.ReadWrite)
    TextFontSize = proxy_property(int, 'TextFontSize', AccessMode.ReadWrite)
    TextFontStyle = proxy_property('AcTextFontStyle', 'TextFontStyle', AccessMode.ReadWrite)
    TextWinBackgrndColor = proxy_property('OLE_COLOR', 'TextWinBackgrndColor', AccessMode.ReadWrite)
    TextWinTextColor = proxy_property('OLE_COLOR', 'TextWinTextColor', AccessMode.ReadWrite)
    TrueColorImages = proxy_property(bool, 'TrueColorImages', AccessMode.ReadWrite)
    XRefFadeIntensity = proxy_property(int, 'XRefFadeIntensity', AccessMode.ReadWrite)
