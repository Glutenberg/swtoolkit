from .modeldoc import ModelDoc


class DrawingDoc(ModelDoc):
    def __init__(self, system_object):
        self.system_object = system_object
