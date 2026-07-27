from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.VarType import Variant


class AcadXRecord(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    TranslateIDs = proxy_property(bool, 'TranslateIDs', AccessMode.ReadWrite)

    def GetXRecordData(self) -> tuple:
        XRecordDataType, XRecordDataValue = self._obj.GetXRecordData()
        return XRecordDataType, XRecordDataValue

    def SetXRecordData(self, XRecordDataType: Variant, XRecordData: Variant) -> None:
        self._obj.SetXRecordData(XRecordDataType(), XRecordData())
