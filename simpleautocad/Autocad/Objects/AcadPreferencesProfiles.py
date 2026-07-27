from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadPreferencesProfiles(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ActiveProfile = proxy_property(str, 'ActiveProfile', AccessMode.ReadOnly)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)

    def CopyProfile(self, oldProfileName: str, newProfileName: str) -> None:
        self._obj.CopyProfile(oldProfileName, newProfileName)

    def DeleteProfile(self, ProfileName: str) -> None:
        self._obj.DeleteProfile(ProfileName)

    def ExportProfile(self, Profile: str, RegFile: str) -> None:
        self._obj.ExportProfile(Profile, RegFile)

    def GetAllProfileNames(self) -> tuple:
        return self._obj.GetAllProfileNames()

    def ImportProfile(self, Profile: str, RegFile: str, IncludePathInfo: bool) -> None:
        self._obj.ImportProfile(Profile, RegFile, IncludePathInfo)

    def RenameProfile(self, origProfileName: str, newProfileName: str) -> None:
        self._obj.RenameProfile(origProfileName, newProfileName)

    def ResetProfile(self, Profile: str) -> None:
        self._obj.ResetProfile(Profile)
