from __future__ import annotations

from .AcadSubEntity import AcadSubEntity


class AcadSubEntSolidEdge(AcadSubEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)
