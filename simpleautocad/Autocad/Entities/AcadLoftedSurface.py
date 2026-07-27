from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadLoftedSurface(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Closed = proxy_property(bool, 'Closed', AccessMode.ReadWrite)
    EdgeExtensionDistances = proxy_property('Variant', 'EdgeExtensionDistances', AccessMode.ReadWrite)
    EndDraftAngle = proxy_property(float, 'EndDraftAngle', AccessMode.ReadWrite)
    EndDraftMagnitude = proxy_property(int, 'EndDraftMagnitude', AccessMode.ReadWrite)
    EndSmoothContinuity = proxy_property(int, 'EndSmoothContinuity', AccessMode.ReadWrite)
    EndSmoothMagnitude = proxy_property(float, 'EndSmoothMagnitude', AccessMode.ReadWrite)
    MaintainAssociativity = proxy_property(int, 'MaintainAssociativity', AccessMode.ReadWrite)
    NumCrossSections = proxy_property(int, 'NumCrossSections', AccessMode.ReadWrite)
    NumGuidePaths = proxy_property(int, 'NumGuidePaths', AccessMode.WriteOnly)
    Periodic = proxy_property(bool, 'Periodic', AccessMode.ReadWrite)
    ShowAssociativity = proxy_property(bool, 'ShowAssociativity', AccessMode.ReadWrite)
    StartDraftAngle = proxy_property(float, 'StartDraftAngle', AccessMode.ReadWrite)
    StartDraftMagnitude = proxy_property(int, 'StartDraftMagnitude', AccessMode.ReadWrite)
    StartSmoothContinuity = proxy_property(int, 'StartSmoothContinuity', AccessMode.ReadWrite)
    StartSmoothMagnitude = proxy_property(float, 'StartSmoothMagnitude', AccessMode.ReadWrite)
    SurfaceNormals = proxy_property(int, 'SurfaceNormals', AccessMode.ReadWrite)
    SurfaceType = proxy_property(str, 'SurfaceType', AccessMode.ReadOnly)
    SurfTrimAssociativity = proxy_property(bool, 'SurfTrimAssociativity', AccessMode.ReadWrite)
    UIsolineDensity = proxy_property(int, 'UIsolineDensity', AccessMode.ReadWrite)
    VIsolineDensity = proxy_property(int, 'VIsolineDensity', AccessMode.ReadWrite)
    WireframeType = proxy_property('AcWireframeType', 'WireframeType', AccessMode.ReadWrite)

    def Copy(self) -> AcadLoftedSurface:
        return AcadLoftedSurface(self._obj.Copy())
