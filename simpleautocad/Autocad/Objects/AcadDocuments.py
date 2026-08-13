from __future__ import annotations

from typing import TYPE_CHECKING

from ..Base import AppObject, AppObjectCollection
from ..Proxy import proxy_property, AccessMode
from .AcadDocument import AcadDocument

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication
    from ...Types.VarType import vBool, vPassword


class AcadDocuments(AppObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, TemplateName: str = None) -> AcadDocument:
        if TemplateName is None:
            return AcadDocument(self._obj.Add())
        return AcadDocument(self._obj.Add(TemplateName))

    def Close(self) -> None:
        self._obj.Close()

    def Item(self, Index: int | str) -> AcadDocument:
        return AcadDocument(self._obj.Item(Index))

    def Open(self, Name: str, ReadOnly: vBool = None, Password: vPassword = None) -> AcadDocument:
        if ReadOnly is None and Password is None:
            return AcadDocument(self._obj.Open(Name))
        if Password is None:
            return AcadDocument(self._obj.Open(Name, ReadOnly))
        return AcadDocument(self._obj.Open(Name, ReadOnly if ReadOnly is not None else False, Password))

    def __iter__(self):
        for item in self._obj:
            yield AcadDocument(item)
