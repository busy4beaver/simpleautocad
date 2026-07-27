from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ...Types.Ge import PyGePoint3d
from .AcadBlock import IAcadBlock


class AcadPaperSpace(IAcadBlock):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Name = proxy_property(str, 'Name', AccessMode.ReadOnly)

    def AddPViewport(self, Center: PyGePoint3d, Width: float, Height: float):
        from ..Entities.AcadPViewport import AcadPViewport
        return AcadPViewport(self._obj.AddPViewport(Center(), Width, Height))
