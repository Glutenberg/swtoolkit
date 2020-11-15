class IDrawingDoc:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object
