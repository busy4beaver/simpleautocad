from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadRasterImage import AcadRasterImage


class AcadGeomapImage(AcadRasterImage):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    GeoImageBrightness: int = proxy_property(int, 'GeoImageBrightness', AccessMode.ReadWrite)
    GeoImageContrast: int = proxy_property(int, 'GeoImageContrast', AccessMode.ReadWrite)
    GeoImagePosition: AcGeomapImagePosition = proxy_property('AcGeomapImagePosition', 'GeoImagePosition', AccessMode.ReadWrite)
    GeoImageWidth: float = proxy_property(float, 'GeoImageWidth', AccessMode.ReadWrite)
    GeoImageHeight: float = proxy_property(float, 'GeoImageHeight', AccessMode.ReadWrite)
