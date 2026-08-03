from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject


class AcadDynamicBlockReferenceProperty(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AllowedValues: vVariantArray = proxy_property('vVariantArray', 'AllowedValues', AccessMode.ReadOnly)
    Description: str = proxy_property(str, 'Description', AccessMode.ReadOnly)
    PropertyName: str = proxy_property(str, 'PropertyName', AccessMode.ReadOnly)
    PropertyType: int = proxy_property(int, 'PropertyType', AccessMode.ReadOnly)
    ReadOnly: bool = proxy_property(bool, 'ReadOnly', AccessMode.ReadOnly)
    Show: bool = proxy_property(bool, 'Show', AccessMode.ReadOnly)
    UnitsType: AcDynamicBlockReferencePropertyUnitsType = proxy_property('AcDynamicBlockReferencePropertyUnitsType', 'UnitsType', AccessMode.ReadOnly)
    Value: object = proxy_property(object, 'Value', AccessMode.ReadWrite)
