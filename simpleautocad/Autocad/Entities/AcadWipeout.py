from __future__ import annotations

from .AcadRasterImage import AcadRasterImage


class AcadWipeout(AcadRasterImage):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Copy(self) -> AcadWipeout:
        return AcadWipeout(self._obj.Copy())
