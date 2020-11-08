import win32com.client
import pythoncom


class IFeatureManager:
    def __init__(self, parent):
        self._instance = parent.FeatureManager

    def _get_features(self, top_level_only):
        arg = win32com.client.VARIANT(pythoncom.VT_BOOL, top_level_only)
        return self._instance.GetFeatures(arg)

    def get_feature_count(self, top_level_only):
        arg = win32com.client.VARIANT(pythoncom.VT_BOOL, top_level_only)
        return self._instance.GetFeatureCount(arg)
