from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesOpenSave(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    AutoAudit = proxy_property(bool, 'AutoAudit', AccessMode.ReadWrite)
    AutoSaveInterval = proxy_property(int, 'AutoSaveInterval', AccessMode.ReadWrite)
    CreateBackup = proxy_property(bool, 'CreateBackup', AccessMode.ReadWrite)
    DemandLoadARXApp = proxy_property('AcARXDemandLoad', 'DemandLoadARXApp', AccessMode.ReadWrite)
    FullCRCValidation = proxy_property(bool, 'FullCRCValidation', AccessMode.ReadWrite)
    IncrementalSavePercent = proxy_property(int, 'IncrementalSavePercent', AccessMode.ReadWrite)
    LogFileOn = proxy_property(bool, 'LogFileOn', AccessMode.ReadWrite)
    MRUNumber = proxy_property(int, 'MRUNumber', AccessMode.ReadOnly)
    ProxyImage = proxy_property('AcProxyImage', 'ProxyImage', AccessMode.ReadWrite)
    SaveAsType = proxy_property('AcSaveAsType', 'SaveAsType', AccessMode.ReadWrite)
    SavePreviewThumbnail = proxy_property(bool, 'SavePreviewThumbnail', AccessMode.ReadWrite)
    ShowProxyDialogBox = proxy_property(bool, 'ShowProxyDialogBox', AccessMode.ReadWrite)
    TempFileExtension = proxy_property(str, 'TempFileExtension', AccessMode.ReadWrite)
    XRefDemandLoad = proxy_property('AcXRefDemandLoad', 'XRefDemandLoad', AccessMode.ReadWrite)
