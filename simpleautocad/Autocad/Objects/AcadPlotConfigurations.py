from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadPlotConfiguration import AcadPlotConfiguration


class AcadPlotConfigurations(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str, ModelType: bool = None) -> AcadPlotConfiguration:
        if ModelType is not None:
            return AcadPlotConfiguration(self._obj.Add(Name, ModelType))
        return AcadPlotConfiguration(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadPlotConfiguration:
        return AcadPlotConfiguration(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadPlotConfiguration(item)
