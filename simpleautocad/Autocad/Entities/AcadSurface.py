from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadSurface(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    EdgeExtensionDistances = proxy_property(float, 'EdgeExtensionDistances', AccessMode.ReadWrite)
    MaintainAssociativity = proxy_property(int, 'MaintainAssociativity', AccessMode.ReadWrite)
    ShowAssociativity = proxy_property(bool, 'ShowAssociativity', AccessMode.ReadWrite)
    SurfaceType = proxy_property(str, 'SurfaceType', AccessMode.ReadOnly)
    SurfTrimAssociativity = proxy_property(bool, 'SurfTrimAssociativity', AccessMode.ReadWrite)
    UIsolineDensity = proxy_property(int, 'UIsolineDensity', AccessMode.ReadWrite)
    VIsolineDensity = proxy_property(int, 'VIsolineDensity', AccessMode.ReadWrite)
    WireframeType = proxy_property('AcWireframeType', 'WireframeType', AccessMode.ReadWrite)

    def Copy(self) -> AcadSurface:
        return AcadSurface(self._obj.Copy())
