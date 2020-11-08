import win32com.client
import pythoncom


class IFeature:
    def __init__(self, system_object):
        self._instance = system_object

    @property
    def name(self):
        return self._instance.Name

    @property
    def description(self):
        return self._instance.Description

    @property
    def id_(self):
        return self._instance.GetID

    @property
    def type_(self):
        return self.get_type_name()

    def get_type_name(self):
        return self._instance.GetTypeName

    def get_type_name2(self):
        return self._instance.GetTypeName2

    def select2(self, append, mark):
        arg1 = win32com.client.VARIANT(pythoncom.VT_BOOL, append)
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, mark)
        return self._instance.Select2(arg1, arg2)

    def add_comment(self, comment):
        arg = win32com.client.VARIANT(pythoncom.VT_BSTR, comment)
        return self._instance.AddComment(arg)

    def get_children(self):
        return self._instance.GetChildren

    def get_parents(self):
        return self._instance.Parents

    def get_owner_feature(self):
        return self._instance.GetOwnerFeature

    def get_next_feature(self):
        return self._instance.GetNextFeature

    def get_box(self):
        arg = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        self._instance.GetBox(arg)
        return arg.value
