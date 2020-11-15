from .component import Component
from .modeldoc import ModelDoc
from .interfaces.iassemblydoc import IAssemblyDoc


class AssemblyDoc(ModelDoc, IAssemblyDoc):
    def __init__(self, system_object):
        super().__init__(system_object)

    def get_components(self, top_level_only: bool = True):
        return [
            Component(system_object)
            for system_object in self._get_components(top_level_only)
        ]
