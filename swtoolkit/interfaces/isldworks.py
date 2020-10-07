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

    def close_all_documents(self):
        pass

    def close_doc(self, doc_name):
        pass

    def new_document(self, template_name, paper_size, width, height):
        pass

    def move_document(
        self,
        source_doc,
        dest_doc,
        child_count,
        from_children,
        to_children,
        option,
        value,
    ):
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
