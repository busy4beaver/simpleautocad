from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from .AcadRegisteredApplication import AcadRegisteredApplication


class AcadRegisteredApplications(IAcadObjectCollection[AcadRegisteredApplication]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadRegisteredApplication:
        return AcadRegisteredApplication(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadRegisteredApplication:
        return AcadRegisteredApplication(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadRegisteredApplication]:
        for item in self._obj:
            yield AcadRegisteredApplication(item)
