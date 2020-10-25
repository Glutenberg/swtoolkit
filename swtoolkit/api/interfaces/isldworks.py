import os

import win32com.client
import pythoncom

from ..com import COM
from .imodeldoc import IModelDoc


class ISldWorks:
    def __init__(self, visible=True, *args, **kwargs):
        self.isldworks = COM("SldWorks.Application")
        self.isldworks.Visible = visible

    @property
    def active_doc(self):
        return self.isldworks.ActiveDoc

    @property
    def frame_state(self):
        pass

    @property
    def startup_completed(self):
        return self.isldworks.StartupProcessCompleted

    def open(self, file_path):
        """Opens specified document
        :param file_path: The path of the file to be opened
        :type name: raw str
        FileName, Type, Options, Configuration, Errors, Warnings
        """

        self.path = file_path
        self.path = self.path.replace("\\", "/")
        self.options = None
        self.config = ""

        if os.path.splitext(self.path)[1] == ".SLDPRT":
            self.type_value = 1
        elif os.path.splitext(self.path)[1] == ".SLDASM":
            self.type_value = 2
        elif os.path.splitext(self.path)[1] == ".SLDDRW":
            self.type_value = 3
        else:
            print("Invalid Document Type")
            return

        openDoc = self.isldworks.OpenDoc6
        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, self.path)
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, self.type_value)
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, 1)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, self.config)
        arg5 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 2)
        arg6 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 128)

        openDoc(arg1, arg2, arg3, arg4, arg5, arg6)

    def activate_doc(self):
        pass

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
        return self.isldworks.GetCurrentWorkingDirectory()

    def get_documents(self):
        pass

    def exit_app(self):
        self.isldworks.ExitApp()

    def activate_task_pane(self):
        pass

    def get_imodeler(self):
        return self.isldworks.GetModeler()

    def get_mass_properties(self):
        pass

    def get_user_unit(self):
        pass

    def get_template_sizes(self):
        pass

    def get_imathutility(self):
        return self.isldworks.IGetMathUtility()
