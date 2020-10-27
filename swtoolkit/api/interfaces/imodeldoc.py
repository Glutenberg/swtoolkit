import win32com.client
import pythoncom

from ..com import COM


class IModelDoc:
    def __init__(self):
        self._isldworks = COM("SldWorks.Application")

    @property
    def _imodeldoc(self):
        return self._isldworks.ActiveDoc

    @property
    def extension(self):
        pass

    @property
    def feature_manager(self):
        pass

    @property
    def configuration_manager(self):
        pass

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