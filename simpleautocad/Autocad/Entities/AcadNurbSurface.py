from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSurface import AcadSurface


class AcadNurbSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CVHullDisplay: bool = proxy_property(bool, 'CVHullDisplay', AccessMode.ReadWrite)
    ShowCVHull: bool = proxy_property(bool, 'ShowCVHull', AccessMode.ReadWrite)
