from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadSubDMeshEdge(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CreaseType: AcMeshCreaseType = proxy_property('AcMeshCreaseType', 'CreaseType', AccessMode.ReadWrite)
    CreaseValue: float = proxy_property(float, 'CreaseValue', AccessMode.ReadWrite)
