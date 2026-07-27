from __future__ import annotations

from .AcadSurface import AcadSurface


class AcadPlaneSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Copy(self) -> AcadPlaneSurface:
        return AcadPlaneSurface(self._obj.Copy())
