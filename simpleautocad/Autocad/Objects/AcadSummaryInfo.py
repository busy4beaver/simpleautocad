from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from ...Types.VarType import vStringArray


class AcadSummaryInfo(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Author = proxy_property(str, 'Author', AccessMode.ReadWrite)
    Comments = proxy_property(str, 'Comments', AccessMode.ReadWrite)
    HyperlinkBase = proxy_property(str, 'HyperlinkBase', AccessMode.ReadWrite)
    Keywords = proxy_property(str, 'Keywords', AccessMode.ReadWrite)
    LastSavedBy = proxy_property(str, 'LastSavedBy', AccessMode.ReadWrite)
    RevisionNumber = proxy_property(str, 'RevisionNumber', AccessMode.ReadWrite)
    Subject = proxy_property(str, 'Subject', AccessMode.ReadWrite)
    Title = proxy_property(str, 'Title', AccessMode.ReadWrite)

    def AddCustomInfo(self, key: str, Value: str) -> None:
        self._obj.AddCustomInfo(key, Value)

    def GetCustomByIndex(self, Index: int) -> tuple:
        pKey, pValue = self._obj.GetCustomByIndex(Index)
        return pKey, pValue

    def GetCustomByKey(self, pKey: str) -> vStringArray:
        pValue = self._obj.GetCustomByKey(pKey)
        return vStringArray(pValue)

    def NumCustomInfo(self) -> int:
        return self._obj.NumCustomInfo()

    def RemoveCustomByIndex(self, Index: int) -> None:
        self._obj.RemoveCustomByIndex(Index)

    def RemoveCustomByKey(self, key: str) -> None:
        self._obj.RemoveCustomByKey(key)

    def SetCustomByIndex(self, Index: int, key: str, Value: str) -> None:
        self._obj.SetCustomByIndex(Index, key, Value)

    def SetCustomByKey(self, key: str, Value: str) -> None:
        self._obj.SetCustomByKey(key, Value)
