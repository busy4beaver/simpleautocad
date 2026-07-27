from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadSecurityParams(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Action = proxy_property('AcadSecurityParamsType', 'Action', AccessMode.ReadWrite)
    Algorithm = proxy_property('AcadSecurityParamsConstants', 'Algorithm', AccessMode.ReadWrite)
    Comment = proxy_property(str, 'Comment', AccessMode.ReadWrite)
    Issuer = proxy_property(str, 'Issuer', AccessMode.ReadWrite)
    KeyLength = proxy_property(int, 'KeyLength', AccessMode.ReadWrite)
    Password = proxy_property(str, 'Password', AccessMode.ReadWrite)
    ProviderName = proxy_property(str, 'ProviderName', AccessMode.ReadWrite)
    ProviderType = proxy_property(int, 'ProviderType', AccessMode.ReadWrite)
    SerialNumber = proxy_property(str, 'SerialNumber', AccessMode.ReadWrite)
    Subject = proxy_property(str, 'Subject', AccessMode.ReadWrite)
    TimeServer = proxy_property(str, 'TimeServer', AccessMode.ReadWrite)
