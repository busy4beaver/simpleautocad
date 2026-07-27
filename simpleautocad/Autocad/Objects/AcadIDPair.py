from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadIDPair(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    IsCloned = proxy_property(bool, 'IsCloned', AccessMode.ReadOnly)
    IsOwnerXlated = proxy_property(bool, 'IsOwnerXlated', AccessMode.ReadOnly)
    IsPrimary = proxy_property(bool, 'IsPrimary', AccessMode.ReadOnly)
    Key = proxy_property(int, 'Key', AccessMode.ReadOnly)
