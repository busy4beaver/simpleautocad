from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from ...Types.Ge import PyGePoint3d
from .AcadUCS import AcadUCS


class AcadUCSs(IAcadObjectCollection[AcadUCS]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(
        self,
        Origin: PyGePoint3d,
        XAxisPoint: PyGePoint3d,
        YAxisPoint: PyGePoint3d,
        Name: str,
    ) -> AcadUCS:
        return AcadUCS(self._obj.Add(Origin(), XAxisPoint(), YAxisPoint(), Name))

    def Item(self, Index: int | str) -> AcadUCS:
        return AcadUCS(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadUCS]:
        for item in self._obj:
            yield AcadUCS(item)
