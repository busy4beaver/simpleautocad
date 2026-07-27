from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesSystem(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    BeepOnError = proxy_property(bool, 'BeepOnError', AccessMode.ReadWrite)
    DisplayOLEScale = proxy_property(bool, 'DisplayOLEScale', AccessMode.ReadWrite)
    EnableStartupDialog = proxy_property(bool, 'EnableStartupDialog', AccessMode.ReadWrite)
    LoadAcadLspInAllDocuments = proxy_property(bool, 'LoadAcadLspInAllDocuments', AccessMode.ReadWrite)
    ShowWarningMessages = proxy_property(bool, 'ShowWarningMessages', AccessMode.ReadWrite)
    SingleDocumentMode = proxy_property(bool, 'SingleDocumentMode', AccessMode.ReadWrite)
    StoreSQLIndex = proxy_property(bool, 'StoreSQLIndex', AccessMode.ReadWrite)
    TablesReadOnly = proxy_property(bool, 'TablesReadOnly', AccessMode.ReadWrite)
