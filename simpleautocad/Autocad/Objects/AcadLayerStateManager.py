from __future__ import annotations

from ..Base import AppObject


class AcadLayerStateManager(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Mask(self, Name: str):
        return self._obj.Mask(Name)

    def Delete(self, Name: str) -> None:
        self._obj.Delete(Name)

    def Export(self, Name: str, FileName: str) -> None:
        self._obj.Export(Name, FileName)

    def Import(self, FileName: str) -> None:
        self._obj.Import(FileName)

    def Rename(self, OldName: str, NewName: str) -> None:
        self._obj.Rename(OldName, NewName)

    def Restore(self, Name: str) -> None:
        self._obj.Restore(Name)

    def Save(self, Name: str, Mask) -> None:
        self._obj.Save(Name, Mask)

    def SetDatabase(self, Database) -> None:
        self._obj.SetDatabase(Database)
