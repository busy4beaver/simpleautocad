from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import IAcadObjectCollection
from ...Types.VarType import Variant, vObjectEmpty
from .AcadDocument import AcadDocument


class AcadDocuments(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, Name: str = '') -> AcadDocument:
        return AcadDocument(self._obj.Add(Name))

    def Close(self) -> None:
        self._obj.Close()

    def Item(self, Index: int) -> AcadDocument:
        return AcadDocument(self._obj.Item(Index))

    def Open(self, Name: str, ReadOnly: bool = False, Password: Variant = vObjectEmpty) -> AcadDocument:
        return AcadDocument(self._obj.Open(Name, ReadOnly, Password()))

    def __iter__(self):
        for item in self._obj:
            yield AcadDocument(item)
