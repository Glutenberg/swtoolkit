""" isldworks is a direct reimplementation of the ISldWorks interface
in the SolidWorks API.

http://help.solidworks.com/2020/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks.html
"""

import win32com.client
import pythoncom

from ..com import COM


class ISldWorks:
    def __init__(self):
        self._isldworks = COM("SldWorks.Application")

    @property
    def _instance(self):
        return self._isldworks

    def _active_doc(self):
        return self._instance.ActiveDoc

    def _get_visible(self):
        """Gets the visibility of the SolidWorks session."""
        return self._instance.Visible

    def _set_visible(self, state: bool):
        """Sets the visibility of the SolidWorks session.

        Args:
            state (bool): The visibility state. True is visible
        """
        self._instance.Visible = state

    def _get_frame_state(self):
        return self._instance.FrameState

    def _set_frame_state(self, state: int):
        self._instance.FrameState = state

    @property
    def startup_completed(self):
        return self._instance.StartupProcessCompleted

    def _opendoc6(
        self, filename: str, type_value: int, options: int, configuration: str
    ):
        """Opens a native solidworks document """

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, filename.replace("\\", "/"))
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, type_value)
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, options)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, configuration)
        arg5 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg6 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)

        openDoc = self._instance.OpenDoc6
        openDoc(arg1, arg2, arg3, arg4, arg5, arg6)

        return arg5, arg6  # (Errors, Warnings)

    def activate_doc(self, *args, **kwargs):
        # Activates a loaded document and rebuilds it as specified.

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, args[0])
        arg2 = win32com.client.VARIANT(pythoncom.VT_BOOL, kwargs["use_user_preference"])
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, kwargs["option"])
        arg4 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)

        ActivateDoc = self._instance.ActivateDoc3
        ActivateDoc(arg1, arg2, arg3, arg4)

        return arg4

    def close_all_documents(self, include_unsaved: bool):
        """Closes all open documents

        :param include_unsaved: Include unsaved documents is function execution
        :type include_unsaved: bool
        :return: Execution feedback. True if successeful
        :rtype: bool
        """

        arg1 = win32com.client.VARIANT(pythoncom.VT_BOOL, include_unsaved)
        return self._instance.CloseAllDocuments(arg1)

    def close_doc(self, name):
        arg = win32com.client.VARIANT(pythoncom.VT_BSTR, name)
        return self._instance.CloseDoc(arg)

    def new_document(self, template_name, paper_size, width, height):
        pass

    def move_document(self, *args, **kwargs):
        pass

    def is_background_processing_complete(self, path):
        pass

    def load_file(self, file_name, arg_string, import_data, errors):
        pass

    def preview_doc(self):
        pass

    def quit_doc(self):
        pass

    def run_command(self):
        pass

    def run_macro(self):
        pass

    def send_msg_to_user(self):
        pass

    def save_settings(self):
        pass

    def get_cwd(self):
        return self._instance.GetCurrentWorkingDirectory()

    def _get_documents(self):
        return self._instance.GetDocuments

    def exit_app(self):
        self._instance.ExitApp()

    def activate_task_pane(self):
        pass

    def get_imodeler(self):
        return self._instance.GetModeler()

    def get_mass_properties(self):
        pass

    def get_user_unit(self):
        pass

    def get_template_sizes(self):
        pass

    def _get_process_id(self):
        return self._instance.GetProcessID

    def get_imathutility(self):
        return self._instance.IGetMathUtility()

    def loadfile4(self):
        pass
