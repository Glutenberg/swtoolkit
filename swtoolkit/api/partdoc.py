from .modeldoc import ModelDoc
from .interfaces.ipartdoc import IPartDoc


class PartDoc(IPartDoc, ModelDoc):
    def __init__(self, system_object):
        self.system_object = system_object
