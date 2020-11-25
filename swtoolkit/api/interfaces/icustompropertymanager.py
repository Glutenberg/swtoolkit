import win32com.client
import pythoncom


class ICustomPropertyManager:
    def __init__(self, parent, config_name: str = str()):
        self._instance = parent.CustomPropertyManager(config_name)

    @property
    def count(self):
        return self._instance.Count

    @property
    def link_all(self):
        return self._instance.LinkAll

    @link_all.setter
    def link_all(self, state: bool):
        self._instance.LinkAll = state

    @property
    def owner(self):
        return self._instance.Owner

    def add3(self, field_name, field_type, field_value, overwrite_existing):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_type)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_value)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, overwrite_existing)

    def delete2(self):
        pass

    def get6(self):
        pass

    def set2(self):
        pass

    def _get_all3(self):

        arg1 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None
        )
        arg2 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None
        )
        arg3 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None
        )
        arg4 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None
        )
        arg5 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None
        )

        GetAll3 = self._instance.GetAll3
        GetAll3(arg1, arg2, arg3, arg4, arg5)

        return arg1, arg2, arg3, arg4, arg5

    def get_type2(self):
        pass

    def is_custom_property_editable(self):
        pass

    def link_property(self):
        pass
