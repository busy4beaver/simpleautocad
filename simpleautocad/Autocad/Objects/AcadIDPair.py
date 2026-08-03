from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject


class AcadIDPair(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    IsCloned: bool = proxy_property(bool, 'IsCloned', AccessMode.ReadOnly)
    IsOwnerXlated: bool = proxy_property(bool, 'IsOwnerXlated', AccessMode.ReadOnly)
    IsPrimary: bool = proxy_property(bool, 'IsPrimary', AccessMode.ReadOnly)
    Key: int = proxy_property(int, 'Key', AccessMode.ReadOnly)
    Value: int = proxy_property(int, 'Value', AccessMode.ReadOnly)
