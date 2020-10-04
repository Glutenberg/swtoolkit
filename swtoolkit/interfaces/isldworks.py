import os

import win32com.client
import pythoncom


class ISldWorks:
    def __init__(self):
        self.swcom = win32com.client.Dispatch("SldWorks.Application")

    def __enter__(self):
        return self.swcom

    def __exit__(self):
        self.swcom = None
        return True

    @property
    def active_doc(self):
        return self.swcom.ActiveDoc

    @property
    def is_visible(self):
        return self.swcom.Visible

    @property
    def startup_completed(self):
        return self.swcom.StartupProcessCompleted

    def open(self, file_path):
        """Opens specified document
        :param file_path: The path of the file to be opened
        :type name: raw str
        """

        self.path = file_path
        self.path = self.path.replace("\\", "/")

        if os.path.splitext(self.path)[1] == ".SLDPRT":
            self.type_value = 1
        elif os.path.splitext(self.path)[1] == ".SLDASM":
            self.type_value = 2
        elif os.path.splitext(self.path)[1] == ".SLDDRW":
            self.type_value = 3
        else:
            print("Invalid Document Type")
            return

        openDoc = self.swcom.OpenDoc6
        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, self.path)
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, self.type_value)
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, 1)
        arg5 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 2)
        arg6 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 128)

        openDoc(arg1, arg2, arg3, "", arg5, arg6)

    def save(self):
        """Saves active document
        :param rebuild: Set True to rebuild part before saving
        """
        arg1 = win32com.client.VARIANT(pythoncom.VT_I4, 1)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 1)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 1)

        self.model = self.swcom.ActiveDoc
        self.model.save3(arg1, arg2, arg3)
