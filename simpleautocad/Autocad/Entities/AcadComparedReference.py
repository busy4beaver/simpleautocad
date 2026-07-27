from __future__ import annotations

from .AcadExternalReference import AcadExternalReference


class AcadComparedReference(AcadExternalReference):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Copy(self) -> AcadComparedReference:
        return AcadComparedReference(self._obj.Copy())
