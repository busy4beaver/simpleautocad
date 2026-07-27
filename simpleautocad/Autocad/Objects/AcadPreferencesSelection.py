from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesSelection(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    DisplayGrips = proxy_property(bool, 'DisplayGrips', AccessMode.ReadWrite)
    DisplayGripsWithinBlocks = proxy_property(bool, 'DisplayGripsWithinBlocks', AccessMode.ReadWrite)
    GripColorSelected = proxy_property('AcColor', 'GripColorSelected', AccessMode.ReadWrite)
    GripColorUnselected = proxy_property('AcColor', 'GripColorUnselected', AccessMode.ReadWrite)
    GripSize = proxy_property(int, 'GripSize', AccessMode.ReadWrite)
    PickAdd = proxy_property(bool, 'PickAdd', AccessMode.ReadWrite)
    PickAuto = proxy_property(bool, 'PickAuto', AccessMode.ReadWrite)
    PickBoxSize = proxy_property(int, 'PickBoxSize', AccessMode.ReadWrite)
    PickDrag = proxy_property(bool, 'PickDrag', AccessMode.ReadWrite)
    PickFirst = proxy_property(bool, 'PickFirst', AccessMode.ReadWrite)
    PickGroup = proxy_property(bool, 'PickGroup', AccessMode.ReadWrite)
