from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadBlock import AcadBlock


class AcadModelSpace(AcadBlock):
    def __init__(self, obj) -> None:
        super().__init__(obj)
