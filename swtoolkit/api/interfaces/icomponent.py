import win32com.client
import pythoncom


class IComponent:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object

    @property
    def name(self):
        return self._instance.Name2

    @property
    def identity(self):
        return self._instance.GetID

    @property
    def path(self):
        return self._instance.GetPathName

    def is_supressed(self):
        return self._instance.GetSuppression2
