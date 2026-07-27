from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSubEntity import AcadSubEntity


class AcadSubDMeshEdge(AcadSubEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CreaseLevel = proxy_property(float, 'CreaseLevel', AccessMode.ReadWrite)
    CreaseType = proxy_property('AcMeshCreaseType', 'CreaseType', AccessMode.ReadWrite)
