from __future__ import annotations

from typing import TYPE_CHECKING

from .AcadBlock import AcadBlock
from ...Types.Ge import PyGePoint3d

if TYPE_CHECKING:
    from ..Entities.AcadPViewport import AcadPViewport


class AcadPaperSpace(AcadBlock):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def AddPViewport(self, Center: PyGePoint3d, Width: float, Height: float) -> AcadPViewport:
        from ..Entities.AcadPViewport import AcadPViewport
        return AcadPViewport(self._obj.AddPViewport(Center(), Width, Height))
