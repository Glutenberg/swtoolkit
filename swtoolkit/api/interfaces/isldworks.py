import os

import win32com.client
import pythoncom

from ..com import COM


class ISldWorks:
    def __init__(self):
        self._isldworks = COM("SldWorks.Application")
        self._isldworks.Visible = True

    @property
    def _instance(self):
        return self._isldworks

    @property
    def _active_doc(self):
        return self._instance.ActiveDoc

    @property
    def frame_state(self):
        pass

    @property
    def startup_completed(self):
        return self._instance.StartupProcessCompleted

    def opendoc6(self, filename, type_value, options, configuration):
        """Opens specified document
        :param file_path: The path of the file to be opened
        :type name: raw str
        FileName, Type, Options, Configuration, Errors, Warnings
        """
        # if os.path.splitext(path)[1] == ".SLDPRT":
        #     type_value = 1
        # elif os.path.splitext(path)[1] == ".SLDASM":
        #     type_value = 2
        # elif os.path.splitext(path)[1] == ".SLDDRW":
        #     type_value = 3
        # else:
        #     raise ValueError("Incompatible File Type")

        openDoc = self._instance.OpenDoc6

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, filename.replace("\\", "/"))
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, type_value)
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, options)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, configuration)
        arg5 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 2)
        arg6 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 128)

        openDoc(arg1, arg2, arg3, arg4, arg5, arg6)

        return arg5, arg6  # (Errors, Warnings)

    # def opendoc6(self, file_path):
    #     """Opens specified document
    #     :param file_path: The path of the file to be opened
    #     :type name: raw str
    #     FileName, Type, Options, Configuration, Errors, Warnings
    #     """

    #     path = file_path
    #     path = path.replace("\\", "/")
    #     options = None
    #     config = ""

    #     if os.path.splitext(path)[1] == ".SLDPRT":
    #         type_value = 1
    #     elif os.path.splitext(path)[1] == ".SLDASM":
    #         type_value = 2
    #     elif os.path.splitext(path)[1] == ".SLDDRW":
    #         type_value = 3
    #     else:
    #         raise ValueError("Incompatible File Type")

    #     openDoc = self._isldworks.OpenDoc6
    #     arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, path)
    #     arg2 = win32com.client.VARIANT(pythoncom.VT_I4, type_value)
    #     arg3 = win32com.client.VARIANT(pythoncom.VT_I4, 1)
    #     arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, config)
    #     arg5 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 2)
    #     arg6 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 128)

    #     openDoc(arg1, arg2, arg3, arg4, arg5, arg6)

    def activate_doc(self, *args, **kwargs):
        """Activates a loaded document and rebuilds it as specified.
        :param name: The name of the loaded document
        :type name: str
        :param use_user_preferences: True to rebuild as per the
        swRebuildOnActivation system option; false to rebuild as per Option
        :type use_user_preferences: bool
        :param option: rebuild option
        :type option: int
        :return: model document object
        """

        ActivateDoc = self._instance.ActivateDoc3
        errors = None
        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, args[0])
        arg2 = win32com.client.VARIANT(pythoncom.VT_BOOL, kwargs["use_user_preference"])
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, kwargs["option"])
        arg4 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, errors)

        ActivateDoc(arg1, arg2, arg3, arg4)
        return arg4

    def close_all_documents(self):
        pass

    def close_doc(self, doc_name):
        pass

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

    def get_documents(self):
        pass

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

    def get_imathutility(self):
        return self._instance.IGetMathUtility()
