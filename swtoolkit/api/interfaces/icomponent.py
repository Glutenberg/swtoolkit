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

    def is_fixed(self):
        return self._instance.IsFixed

    def is_mirrored(self):
        return self._instance.IsMirrored

    def is_loaded(self):
        return self._instance.IsLoaded

    def is_hidden(self):
        return self._instance.IsHidden

    def is_pattern_instance(self):
        return self._instance.IsPatternInstance

    def is_envelope(self):
        return self._instance.IsEnvelope

    def is_root(self):
        return self._instance.IsRoot

    def _get_imported_path(self):
        return self._instance.GetImportedPath

    def _get_modeldoc2(self):
        return self._instance.GetModelDoc2

    def _get_parent(self):
        return self._instance.GetParent

    def _get_children(self):
        return self._instance.GetChildren
