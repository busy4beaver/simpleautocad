from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadRasterImage import AcadRasterImage


class AcadGeomapImage(AcadRasterImage):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    GeoImageBrightness = proxy_property(int, 'GeoImageBrightness', AccessMode.ReadWrite)
    GeoImageContrast = proxy_property(int, 'GeoImageContrast', AccessMode.ReadWrite)
    GeoImageFade = proxy_property(int, 'GeoImageFade', AccessMode.ReadWrite)
    GeoImageHeight = proxy_property(float, 'GeoImageHeight', AccessMode.ReadOnly)
    GeoImageWidth = proxy_property(float, 'GeoImageWidth', AccessMode.ReadOnly)

    def Copy(self) -> AcadGeomapImage:
        return AcadGeomapImage(self._obj.Copy())
