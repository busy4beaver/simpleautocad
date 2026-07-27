from __future__ import annotations

from win32com.client import CDispatch
from pythoncom import com_error

from ..Base import (
    Application,
    AppObject,
    get_clsid,
    com_server_is_running,
    AppCreate,
    AppAttach,
    create_new_instance_explicitly,
)
from ..Proxy import proxy_property, AccessMode
from ...Utils.retry_com import retry_com
from ...Types.Ge import PyGePoint3d
from ...Types.VarType import vStringArray
from .AcadState import AcadState


class AcadApplication(Application, AppObject):
    _first_instance_initialized = False
    __app_name__ = 'AutoCAD'
    __app_version__ = None

    @staticmethod
    def set_version(version: str):
        if AcadApplication.__app_version__ is None:
            AcadApplication.__app_version__ = version

    def _manage_application_instance(self) -> CDispatch:
        if not AcadApplication._first_instance_initialized:
            clsid = get_clsid(self)
            AcadApplication.__app_clsid__ = clsid[0]
            AcadApplication.__app_full_name__ = clsid[1]
            acad_app = com_server_is_running(AcadApplication.__app_full_name__)
            self._is_owner = not bool(acad_app)
            if not acad_app:
                acad_app = AppCreate(AcadApplication.__app_full_name__)
        else:
            clsid = AcadApplication.__app_clsid__ or get_clsid(self)[0]
            acad_app = create_new_instance_explicitly(clsid)
            self._is_owner = True
        AcadApplication._first_instance_initialized = True
        return acad_app

    def _reconnect_com(self):
        """Восстанавливает связь с COM-сервером AutoCAD."""
        prog_id = AcadApplication.__app_full_name__
        if not prog_id:
            clsid_info = get_clsid(self)
            AcadApplication.__app_clsid__ = clsid_info[0]
            AcadApplication.__app_full_name__ = clsid_info[1]
            prog_id = clsid_info[1]

        try:
            attached = AppAttach(prog_id)
            if attached is not None:
                self._set_com_obj(attached)
                self._is_owner = False
                return
        except com_error:
            pass

        clsid = AcadApplication.__app_clsid__ or get_clsid(self)[0]
        self._set_com_obj(create_new_instance_explicitly(clsid))
        self._is_owner = True

    ActiveDocument = proxy_property('AcadDocument', 'ActiveDocument', AccessMode.ReadOnly)
    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Caption = proxy_property(str, 'Caption', AccessMode.ReadOnly)
    Documents = proxy_property('AcadDocuments', 'Documents', AccessMode.ReadOnly)
    FullName = proxy_property(str, 'FullName', AccessMode.ReadOnly)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    HWND = proxy_property(int, 'HWND', AccessMode.ReadOnly)
    LocaleId = proxy_property(int, 'LocaleId', AccessMode.ReadOnly)
    MenuBar = proxy_property('AcadMenuBar', 'MenuBar', AccessMode.ReadOnly)
    MenuGroups = proxy_property('AcadMenuGroups', 'MenuGroups', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadOnly)
    Path = proxy_property(str, 'Path', AccessMode.ReadOnly)
    Preferences = proxy_property('AcadPreferences', 'Preferences', AccessMode.ReadOnly)
    VBE = proxy_property('AppObject', 'VBE', AccessMode.ReadOnly)
    Version = proxy_property(str, 'Version', AccessMode.ReadOnly)
    Visible = proxy_property(bool, 'Visible', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)
    WindowLeft = proxy_property(int, 'WindowLeft', AccessMode.ReadWrite)
    WindowState = proxy_property(int, 'WindowState', AccessMode.ReadWrite)
    WindowTop = proxy_property(int, 'WindowTop', AccessMode.ReadWrite)

    @retry_com(max_attempts=5, base_delay=0.25)
    def StatusID(self, VportObj) -> bool:
        return self._obj.StatusId(VportObj())

    @retry_com(max_attempts=5, base_delay=0.25)
    def Eval(self, Expression: str) -> None:
        self._obj.Eval(Expression)

    @retry_com(max_attempts=5, base_delay=0.25)
    def GetAcadState(self) -> AcadState:
        return AcadState(self._obj.GetAcadState())

    @retry_com(max_attempts=5, base_delay=0.25)
    def GetInterfaceObject(self, ProgID: str) -> AppObject:
        return AppObject(self._obj.GetInterfaceObject(ProgID))

    @retry_com(max_attempts=5, base_delay=0.25)
    def ListARX(self) -> vStringArray:
        return vStringArray(self._obj.ListArx())

    @retry_com(max_attempts=5, base_delay=0.25)
    def LoadARX(self, Name) -> None:
        self._obj.LoadArx(Name)

    @retry_com(max_attempts=5, base_delay=0.25)
    def LoadDVB(self, Name) -> None:
        self._obj.LoadDVB(Name)

    @retry_com(max_attempts=5, base_delay=0.25)
    def Quit(self) -> None:
        self._obj.Quit()

    @retry_com(max_attempts=5, base_delay=0.25)
    def RunMacro(self, MacroPath: str) -> None:
        self._obj.RunMacro(MacroPath)

    @retry_com(max_attempts=5, base_delay=0.25)
    def UnloadARX(self, Name: str) -> None:
        self._obj.UnloadArx(Name)

    @retry_com(max_attempts=5, base_delay=0.25)
    def UnloadDVB(self, Name: str) -> None:
        self._obj.UnloadDVB(Name)

    @retry_com(max_attempts=5, base_delay=0.25)
    def Update(self) -> None:
        self._obj.Update()

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomAll(self) -> None:
        self._obj.ZoomAll()

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomCenter(self, Center: PyGePoint3d, Magnify: float) -> None:
        self._obj.ZoomCenter(Center(), Magnify)

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomExtents(self) -> None:
        self._obj.ZoomExtents()

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomPickWindow(self) -> None:
        self._obj.ZoomPickWindow()

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomPrevious(self) -> None:
        self._obj.ZoomPrevious()

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomScaled(self, Scale: float, ScaleType) -> None:
        self._obj.ZoomScaled(Scale, ScaleType)

    @retry_com(max_attempts=5, base_delay=0.25)
    def ZoomWindow(self, LowerLeft: PyGePoint3d, UpperRight: PyGePoint3d) -> None:
        self._obj.ZoomWindow(LowerLeft(), UpperRight())
