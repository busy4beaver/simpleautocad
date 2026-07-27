from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSubEntity import AcadSubEntity


class AcadSubDMeshVertex(AcadSubEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates = proxy_property('PyGePoint3d', 'Coordinates', AccessMode.ReadWrite)
