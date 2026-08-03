from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSubEntity import AcadSubEntity


class AcadSubEntSolidFace(AcadSubEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Material: str = proxy_property(str, 'Material', AccessMode.ReadWrite)
