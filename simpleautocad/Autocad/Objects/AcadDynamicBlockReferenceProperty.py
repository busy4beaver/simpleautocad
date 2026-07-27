from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadDynamicBlockReferenceProperty(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AllowedValues = proxy_property(object, 'AllowedValues', AccessMode.ReadOnly)
    Description = proxy_property(str, 'Description', AccessMode.ReadOnly)
    PropertyName = proxy_property(str, 'PropertyName', AccessMode.ReadOnly)
    ReadOnly = proxy_property(bool, 'ReadOnly', AccessMode.ReadOnly)
    Show = proxy_property(bool, 'Show', AccessMode.ReadOnly)
    UnitsType = proxy_property(
        'AcDynamicBlockReferencePropertyUnitsType', 'UnitsType', AccessMode.ReadOnly
    )
    Value = proxy_property(object, 'Value', AccessMode.ReadWrite)
