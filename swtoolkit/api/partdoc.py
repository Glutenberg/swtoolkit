from .modeldoc import ModelDoc


class PartDoc(ModelDoc):
    def __init__(self, system_object):
        self.system_object = system_object
