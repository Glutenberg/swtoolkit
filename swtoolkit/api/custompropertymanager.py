from .interfaces.icustompropertymanager import ICustomPropertyManager


class CustomPropertyManager(ICustomPropertyManager):
    def __init__(self, parent, config_name):
        super().__init__(parent, config_name)

    def get_all(self):
        arg1, arg2, arg3, arg4, arg5 = self.get_all3()
        return tuple(zip(arg5.value, arg4.value, arg3.value, arg2.value, arg1.value))