import win32com.client
import pythoncom

from ..com import COM
from ..modeldocextension import ModelDocExtension


class IModelDoc:
    def __init__(self):
        self._isldworks = COM("SldWorks.Application")
        self._instance = self._isldworks.ActiveDoc

    @property
    def extension(self):
        return ModelDocExtension(self._instance)

    @property
    def feature_manager(self):
        return self._instance.FeatureManager

    @property
    def configuration_manager(self):
        return self._instance.ConfigurationManager

    def active_view(self):
        pass

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

    def set_summaryinfo(self):
        pass

    def get_path_name(self):
        return self._instance.GetPathName

    def get_title(self):
        return self._instance.GetTitle

    def get_type(self):
        return self._instance.GetType

    def get_update_stamp(self):
        return self._instance.GetUpdateStamp

    def get_units(self):
        return self._instance.GetUnits

    def get_user_units(self, unit_type):
        return self._instance.GetUserUnit(unit_type)

    def get_save_flag(self):
        return self._instance.GetSaveFlag

    @property
    def is_weldment(self):
        """fuction to determine if a part is a weldment
        Note: Exception raised if file type is not ".SLDPRT"
        :return: True if part is a weldment
        :rtype: bool
        """

        retval = self._instance.IsWeldment
        return retval

    def is_sheetmetal(self):
        pass

    def save3(self, option=1):
        """Saves active document
        :param rebuild: Set True to rebuild part before saving
        """

        arg1 = win32com.client.VARIANT(pythoncom.VT_I4, option)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)

        retval = self._instance.save3(arg1, arg2, arg3)
        return retval, arg2, arg3

    def save_bmp(self):
        pass

    def view_zoom_to_fit2(self):
        return self._instance.ViewZoomtofit2
