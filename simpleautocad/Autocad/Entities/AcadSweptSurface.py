from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSurface import AcadSurface


class AcadSweptSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Bank = proxy_property(bool, 'Bank', AccessMode.ReadWrite)
    ProfileRotation = proxy_property(float, 'ProfileRotation', AccessMode.ReadWrite)
    Scale = proxy_property(float, 'Scale', AccessMode.ReadWrite)
    Twist = proxy_property(float, 'Twist', AccessMode.ReadWrite)

    def Copy(self) -> AcadSweptSurface:
        return AcadSweptSurface(self._obj.Copy())
