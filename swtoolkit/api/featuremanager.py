import win32com.client
import pythoncom

from .interfaces.ifeaturemanager import IFeatureManager
from .feature import Feature


class FeatureManager(IFeatureManager):
    def __init__(self, parent):
        super().__init__(parent)

    def get_features(self, top_level_only=True):
        return [
            Feature(system_object)
            for system_object in self._get_features(top_level_only)
        ]
