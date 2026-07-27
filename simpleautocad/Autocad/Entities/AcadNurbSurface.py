from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSurface import AcadSurface


class AcadNurbSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CvHullDisplay = proxy_property(bool, 'CvHullDisplay', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)

    def Copy(self) -> AcadNurbSurface:
        return AcadNurbSurface(self._obj.Copy())
