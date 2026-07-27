from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesUser(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ADCInsertUnitsDefaultSource = proxy_property('AcInsertUnits', 'ADCInsertUnitsDefaultSource', AccessMode.ReadWrite)
    ADCInsertUnitsDefaultTarget = proxy_property('AcInsertUnits', 'ADCInsertUnitsDefaultTarget', AccessMode.ReadWrite)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    HyperlinkDisplayCursor = proxy_property(bool, 'HyperlinkDisplayCursor', AccessMode.ReadWrite)
    KeyboardAccelerator = proxy_property('AcKeyboardAccelerator', 'KeyboardAccelerator', AccessMode.ReadWrite)
    KeyboardPriority = proxy_property('AcKeyboardPriority', 'KeyboardPriority', AccessMode.ReadWrite)
    SCMCommandMode = proxy_property('AcDrawingAreaSCMCommand', 'SCMCommandMode', AccessMode.ReadWrite)
    SCMDefaultMode = proxy_property('AcDrawingAreaSCMDefault', 'SCMDefaultMode', AccessMode.ReadWrite)
    SCMEditMode = proxy_property('AcDrawingAreaSCMEdit', 'SCMEditMode', AccessMode.ReadWrite)
    SCMTimeMode = proxy_property(bool, 'SCMTimeMode', AccessMode.ReadWrite)
    SCMTimeValue = proxy_property(int, 'SCMTimeValue', AccessMode.ReadWrite)
    ShortCutMenuDisplay = proxy_property(bool, 'ShortCutMenuDisplay', AccessMode.ReadWrite)
