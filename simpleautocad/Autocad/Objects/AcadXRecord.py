from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadXRecord(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    TranslateIDs: bool = proxy_property(bool, 'TranslateIDs', AccessMode.ReadWrite)

    def GetXRecordData(self) -> tuple:
        return self._obj.GetXRecordData()

    def SetXRecordData(self, XRecordDataType, XRecordDataValue) -> None:
        self._obj.SetXRecordData(XRecordDataType, XRecordDataValue)
