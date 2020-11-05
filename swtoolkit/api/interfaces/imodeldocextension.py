from ..custompropertymanager import CustomPropertyManager


class IModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension


def custom_property_manager(self, config_name):
    return CustomPropertyManager(self._instance, config_name)