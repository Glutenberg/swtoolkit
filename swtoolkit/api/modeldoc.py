from .interface.imodeldoc import IModelDoc


class ModelDoc(IModelDoc):
    def __init__(self):
        super.__init__()

    def __call__(self, name=None):
        if name is None:
            return self._imodeldoc()
        else:
            return None
