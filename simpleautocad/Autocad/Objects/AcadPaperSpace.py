from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadBlock import AcadBlock


class AcadPaperSpace(AcadBlock):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def AddPViewport(self, Center: PyGePoint3d, Width: float, Height: float) -> AcadPViewport:
        return AcadPViewport(self._obj.AddPViewport(Center(), Width, Height))
