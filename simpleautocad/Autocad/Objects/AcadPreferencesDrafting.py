from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesDrafting(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AlignmentPointAcquisition = proxy_property('AcAlignmentPointAcquisition', 'AlignmentPointAcquisition', AccessMode.ReadWrite)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    AutoSnapAperture = proxy_property(bool, 'AutoSnapAperture', AccessMode.ReadWrite)
    AutoSnapApertureSize = proxy_property(int, 'AutoSnapApertureSize', AccessMode.ReadWrite)
    AutoSnapMagnet = proxy_property(bool, 'AutoSnapMagnet', AccessMode.ReadWrite)
    AutoSnapMarker = proxy_property(bool, 'AutoSnapMarker', AccessMode.ReadWrite)
    AutoSnapMarkerColor = proxy_property('AcColor', 'AutoSnapMarkerColor', AccessMode.ReadWrite)
    AutoSnapMarkerSize = proxy_property(int, 'AutoSnapMarkerSize', AccessMode.ReadWrite)
    AutoSnapToolTip = proxy_property(bool, 'AutoSnapToolTip', AccessMode.ReadWrite)
    AutoTrackTooltip = proxy_property(bool, 'AutoTrackTooltip', AccessMode.ReadWrite)
    FullScreenTrackingVector = proxy_property(bool, 'FullScreenTrackingVector', AccessMode.ReadWrite)
    PolarTrackingVector = proxy_property(bool, 'PolarTrackingVector', AccessMode.ReadWrite)
