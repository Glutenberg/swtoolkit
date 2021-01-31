import win32com
import pythoncom

from ..custompropertymanager import CustomPropertyManager


class IModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension

    def custom_property_manager(self, config_name):
        return CustomPropertyManager(self._instance, config_name)

    def rebuild(self, options):
        arg = win32com.client.VARIANT(pythoncom.VT_I4, options)
        return self._instance.Rebuild(arg)

    def select_by_id2(self):
        pass

    def view_zoom_to_sheet(self):
        pass

    def save_as3(self):
        pass

    def save_pack_and_go(self):
        pass

    def set_user_preference_toggle(self):
        pass
