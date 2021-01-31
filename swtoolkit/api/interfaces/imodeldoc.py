import win32com.client
import pythoncom

from ..modeldocextension import ModelDocExtension
from ..featuremanager import FeatureManager


class IModelDoc:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object

    @property
    def extension(self):
        """Exposes additional :class:`ModelDoc` methods and attributes

        Returns:
            ModelDocExtension: ModelDocExtension exposes additional
            :class:`ModelDoc` methods and attributes
        """
        return ModelDocExtension(self._instance)

    @property
    def feature_manager(self):
        return FeatureManager(self._instance)

    @property
    def configuration_manager(self):
        return self._instance.ConfigurationManager

    def active_view(self):
        pass

    def _get_path_name(self):
        """Returns the model or document path name."""
        return self._instance.GetPathName

    def _get_title(self):
        """Returns the model or document title."""
        return self._instance.GetTitle

    def _get_type(self):
        """Returns the model or document type."""
        return self._instance.GetType

    def get_update_stamp(self):
        return self._instance.GetUpdateStamp

    def get_units(self):
        return self._instance.GetUnits

    def get_user_units(self, unit_type):
        return self._instance.GetUserUnit(unit_type)

    def get_save_flag(self):
        return self._instance.GetSaveFlag

    def get_custominfo(self):
        pass

    def get_configinfo(self):
        pass

    def get_summaryinfo(self):
        pass

    def set_custominfo(self):
        pass

    def set_configinfo(self):
        pass

    def set_summaryinfo(self, field_name, field_value):
        self._instance.SummaryInfo(field_name, field_value)

    @property
    def is_weldment(self):
        """fuction to determine if a part is a weldment Note: Exception raised
        if file type is not ".SLDPRT" :return: True if part is a weldment
        :rtype: bool
        """

        return self._instance.IsWeldment

    @property
    def is_sheetmetal(self):
        pass

    def save3(self, option=1):
        """Saves active document
        :param rebuild: Set True to rebuild part before saving
        """

        arg1 = win32com.client.VARIANT(pythoncom.VT_I4, option)
        arg2 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_I4, None
        )
        arg3 = win32com.client.VARIANT(
            pythoncom.VT_BYREF | pythoncom.VT_I4, None
        )

        retval = self._instance.save3(arg1, arg2, arg3)
        return retval, arg2, arg3

    def save_bmp(self, file_name_in, width_in, height_in):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, file_name_in)
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, width_in)
        arg3 = win32com.client.VARIANT(pythoncom.VT_I4, height_in)

        return self._instance.SaveBMP(arg1, arg2, arg3)

    def view_zoom_to_fit2(self):
        return self._instance.ViewZoomtofit2()

    def view_zoom_in(self):
        return self._instance.ViewZoomin()

    def view_zoom_out(self):
        return self._instance.ViewZoomout()

    def force_quit(self):
        return self._instance.Quit()

    def add_configuration3(self, name, comment, alternate_name, options):

        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BSTR, comment)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BSTR, alternate_name)
        arg4 = win32com.client.VARIANT(pythoncom.VT_I4, options)

        AddConfiguration = self._instance.AddConfiguration3
        return AddConfiguration(arg1, arg2, arg3, arg4)

    def show_named_view2(self, view_name, view_id):
        arg1 = win32com.client.VARIANT(pythoncom.VT_BSTR, view_name)
        arg2 = win32com.client.VARIANT(pythoncom.VT_I4, view_id)
        return self._instance.ShowNamedView2(arg1, arg2)
