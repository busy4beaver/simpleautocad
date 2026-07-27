from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadBlockReference import AcadBlockReference


class AcadExternalReference(AcadBlockReference):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    LayerPropertyOverrides = proxy_property(bool, 'LayerPropertyOverrides', AccessMode.ReadOnly)
    Path = proxy_property(str, 'Path', AccessMode.ReadWrite)

    def Copy(self) -> AcadExternalReference:
        return AcadExternalReference(self._obj.Copy())
