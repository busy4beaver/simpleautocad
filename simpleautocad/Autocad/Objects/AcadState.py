from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject


class AcadState(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    IsQuiescent: bool = proxy_property(bool, 'IsQuiescent', AccessMode.ReadOnly)
