from .interfaces.imodeldoc import IModelDoc


class ModelDoc(IModelDoc):
    def __init__(self):
        super().__init__()

    # def __call__(self, name=None):
    #     if name is None:
    #         super()._modeldoc = super()._imodeldoc()
    #     else:
    #         pass
