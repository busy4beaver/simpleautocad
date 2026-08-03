from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSurface import AcadSurface


class AcadSweptSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Length: float = proxy_property(float, 'Length', AccessMode.ReadOnly)
    ProfileRotation: float = proxy_property(float, 'ProfileRotation', AccessMode.ReadWrite)
    Scale: float = proxy_property(float, 'Scale', AccessMode.ReadWrite)
    Twist: float = proxy_property(float, 'Twist', AccessMode.ReadWrite)
