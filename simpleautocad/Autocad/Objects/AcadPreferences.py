from __future__ import annotations

from typing import TYPE_CHECKING

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication
    from .AcadPreferencesDisplay import AcadPreferencesDisplay
    from .AcadPreferencesDrafting import AcadPreferencesDrafting
    from .AcadPreferencesFiles import AcadPreferencesFiles
    from .AcadPreferencesOpenSave import AcadPreferencesOpenSave
    from .AcadPreferencesOutput import AcadPreferencesOutput
    from .AcadPreferencesProfiles import AcadPreferencesProfiles
    from .AcadPreferencesSelection import AcadPreferencesSelection
    from .AcadPreferencesSystem import AcadPreferencesSystem
    from .AcadPreferencesUser import AcadPreferencesUser


class AcadPreferences(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Display: AcadPreferencesDisplay = proxy_property('AcadPreferencesDisplay', 'Display', AccessMode.ReadOnly)
    Drafting: AcadPreferencesDrafting = proxy_property('AcadPreferencesDrafting', 'Drafting', AccessMode.ReadOnly)
    Files: AcadPreferencesFiles = proxy_property('AcadPreferencesFiles', 'Files', AccessMode.ReadOnly)
    OpenSave: AcadPreferencesOpenSave = proxy_property('AcadPreferencesOpenSave', 'OpenSave', AccessMode.ReadOnly)
    Output: AcadPreferencesOutput = proxy_property('AcadPreferencesOutput', 'Output', AccessMode.ReadOnly)
    Profiles: AcadPreferencesProfiles = proxy_property('AcadPreferencesProfiles', 'Profiles', AccessMode.ReadOnly)
    Selection: AcadPreferencesSelection = proxy_property('AcadPreferencesSelection', 'Selection', AccessMode.ReadOnly)
    System: AcadPreferencesSystem = proxy_property('AcadPreferencesSystem', 'System', AccessMode.ReadOnly)
    User: AcadPreferencesUser = proxy_property('AcadPreferencesUser', 'User', AccessMode.ReadOnly)
