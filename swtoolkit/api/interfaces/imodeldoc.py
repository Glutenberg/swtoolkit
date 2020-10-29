import win32com.client
import pythoncom

from ..com import COM


class IModelDoc:
    def __init__(self):
        self._isldworks = COM("SldWorks.Application")

    @property
    def _instance(self):
        return self._isldworks.ActiveDoc

    @property
    def extension(self):
        return self._instance.Extension

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

    def is_weldment(self):
        pass

    def is_sheetmetal(self):
        pass

    def save3(self, option=1):
        """Saves active document
        :param rebuild: Set True to rebuild part before saving
        """

        arg2_ = None
        arg3_ = None

        arg1 = win32com.client.VARIANT(pythoncom.VT_I4, option)
        arg2 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, arg2_)
        arg3 = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, arg3_)

        retval = self._instance.save3(arg1, arg2, arg3)
        return retval

    def save_bmp(self):
        pass