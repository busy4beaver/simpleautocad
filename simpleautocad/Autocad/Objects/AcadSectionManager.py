from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from ..Entities.AcadSection import AcadSection


class AcadSectionManager(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def GetLiveSection(self) -> AcadSection:
        return AcadSection(self._obj.GetLiveSection())

    def GetUniqueSectionName(self) -> str:
        return self._obj.GetUniqueSectionName()
