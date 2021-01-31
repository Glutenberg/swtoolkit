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

    def _add3(self, field_name, field_type, field_value, overwrite_existing):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_type)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_value)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, overwrite_existing)
        return self._instance.Add3(arg1, arg2, arg3, arg4)

    def _delete2(self, field_name):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)
        return self._instance.Delete2(arg1)

    def _get6(
        self,
        field_name,
        use_cached,
        val_out,
        resolved_val_out,
        was_resolved,
        link_to_property,
    ):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BSTR, use_cached)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BSTR, val_out)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BSTR, resolved_val_out)
        arg5 = win32com.client.VARIANT(pythoncom.VT_BSTR, was_resolved)
        arg6 = win32com.client.VARIANT(pythoncom.VT_BSTR, link_to_property)

        return self._instance.Get6(arg1, arg2, arg3, arg4, arg5, arg6)

    def _set2(self, field_name, field_value):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_value)

        Set2 = self._instance.Set2
        retval = Set2(arg1, arg2)

        return retval

    def _get_all3(self):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg4 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg5 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)

        GetAll3 = self._instance.GetAll3
        GetAll3(arg1, arg2, arg3, arg4, arg5)

        return arg1, arg2, arg3, arg4, arg5

    def _get_type2(self, field_name):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)

        GetType2 = self._instance.GetType2
        retval = GetType2(arg1)

        return retval

    def _is_custom_property_editable(self, property_name, configuration_name):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, property_name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BSTR, configuration_name)

        IsCustomPropertyEditable = self._instance.IsCustomPropertyEditable
        retval = IsCustomPropertyEditable(arg1, arg2)
        return retval

    def _link_property(self, field_name, field_link):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, field_name)
        arg1 = win32com.client.VARIANT(pythoncom.VT_BOOL, field_link)

        LinkProperty = self._instance.LinkProperty
        retval = LinkProperty(field_name, field_link)
        return retval
