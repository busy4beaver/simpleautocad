from __future__ import annotations

from typing import TYPE_CHECKING

from .Base import AppObject
from .Proxy import proxy_property, AccessMode
from ..Types.VarType import vShortArray, vVariantArray

if TYPE_CHECKING:
    from .Objects.AcadApplication import AcadApplication
    from .Objects.AcadDocument import AcadDocument


class IAcadObject(AppObject):
    """The standard interface for a basic AutoCAD object."""

    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Document: AcadDocument = proxy_property('AcadDocument', 'Document', AccessMode.ReadOnly)
    Handle: str = proxy_property(str, 'Handle', AccessMode.ReadOnly)
    HasExtensionDictionary: bool = proxy_property(bool, 'HasExtensionDictionary', AccessMode.ReadOnly)
    ObjectName: str = proxy_property(str, 'ObjectName', AccessMode.ReadOnly)
    ObjectID: int = proxy_property(int, 'ObjectID', AccessMode.ReadOnly)
    OwnerID: int = proxy_property(int, 'OwnerID', AccessMode.ReadOnly)

    def GetExtensionDictionary(self):
        from .Objects.AcadDictionary import AcadDictionary
        return AcadDictionary(self._obj.GetExtensionDictionary())

    def GetXData(self, AppName: str = '') -> tuple:
        XDataType, XDataValue = self._obj.GetXData(AppName)
        return XDataType, XDataValue

    def SetXData(self, XDataType: vShortArray, XDataValue: vVariantArray) -> None:
        self._obj.SetXData(XDataType(), XDataValue())


class AcadObject(IAcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Delete(self) -> None:
        self._obj.Delete()


class IAcadObjectCollection(IAcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Item(self, Index: int | str):
        obj = self._obj.Item(Index)
        return AcadObject(obj)

    def __iter__(self):
        for item in self._obj:
            yield AcadObject(item)
