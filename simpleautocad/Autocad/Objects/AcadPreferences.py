from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferences(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Display = proxy_property('AcadPreferencesDisplay', 'Display', AccessMode.ReadOnly)
    Drafting = proxy_property('AcadPreferencesDrafting', 'Drafting', AccessMode.ReadOnly)
    Files = proxy_property('AcadPreferencesFiles', 'Files', AccessMode.ReadOnly)
    OpenSave = proxy_property('AcadPreferencesOpenSave', 'OpenSave', AccessMode.ReadOnly)
    Output = proxy_property('AcadPreferencesOutput', 'Output', AccessMode.ReadOnly)
    Profiles = proxy_property('AcadPreferencesProfiles', 'Profiles', AccessMode.ReadOnly)
    Selection = proxy_property('AcadPreferencesSelection', 'Selection', AccessMode.ReadOnly)
    System = proxy_property('AcadPreferencesSystem', 'System', AccessMode.ReadOnly)
    User = proxy_property('AcadPreferencesUser', 'User', AccessMode.ReadOnly)
