from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.Ac import AcColor

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication

# OLE_COLOR is a COM color integer; treat as int for typing
OLE_COLOR = int


class AcadPreferencesDisplay(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    AutoTrackingVecColor: OLE_COLOR = proxy_property(int, 'AutoTrackingVecColor', AccessMode.ReadWrite)
    CursorSize: int = proxy_property(int, 'CursorSize', AccessMode.ReadWrite)
    DisplayLayoutTabs: bool = proxy_property(bool, 'DisplayLayoutTabs', AccessMode.ReadWrite)
    DisplayScreenMenu: bool = proxy_property(bool, 'DisplayScreenMenu', AccessMode.ReadWrite)
    DisplayScrollBars: bool = proxy_property(bool, 'DisplayScrollBars', AccessMode.ReadWrite)
    DockedToolbarSpace: bool = proxy_property(bool, 'DockedToolbarSpace', AccessMode.ReadWrite)
    GraphicsWinLayoutBackgrndColor: OLE_COLOR = proxy_property(int, 'GraphicsWinLayoutBackgrndColor', AccessMode.ReadWrite)
    GraphicsWinModelBackgrndColor: OLE_COLOR = proxy_property(int, 'GraphicsWinModelBackgrndColor', AccessMode.ReadWrite)
    HistoryDays: int = proxy_property(int, 'HistoryDays', AccessMode.ReadWrite)
    ImageFrameHighlight: bool = proxy_property(bool, 'ImageFrameHighlight', AccessMode.ReadWrite)
    LayoutCreateViewport: bool = proxy_property(bool, 'LayoutCreateViewport', AccessMode.ReadWrite)
    LayoutCrosshairColor: OLE_COLOR = proxy_property(int, 'LayoutCrosshairColor', AccessMode.ReadWrite)
    LayoutDisplayMargins: bool = proxy_property(bool, 'LayoutDisplayMargins', AccessMode.ReadWrite)
    LayoutDisplayPaper: bool = proxy_property(bool, 'LayoutDisplayPaper', AccessMode.ReadWrite)
    LayoutDisplayPaperShadow: bool = proxy_property(bool, 'LayoutDisplayPaperShadow', AccessMode.ReadWrite)
    LayoutShowPlotSetup: bool = proxy_property(bool, 'LayoutShowPlotSetup', AccessMode.ReadWrite)
    MaxAutoCADWindow: bool = proxy_property(bool, 'MaxAutoCADWindow', AccessMode.ReadWrite)
    ModelCrosshairColor: OLE_COLOR = proxy_property(int, 'ModelCrosshairColor', AccessMode.ReadWrite)
    ShowRasterImage: bool = proxy_property(bool, 'ShowRasterImage', AccessMode.ReadWrite)
    TextEditorColorScheme: AcColor = proxy_property('AcColor', 'TextEditorColorScheme', AccessMode.ReadWrite)
    TrueColorImages: bool = proxy_property(bool, 'TrueColorImages', AccessMode.ReadWrite)
    XRefFadeIntensity: int = proxy_property(int, 'XRefFadeIntensity', AccessMode.ReadWrite)
