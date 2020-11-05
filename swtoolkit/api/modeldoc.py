from .interfaces.imodeldoc import IModelDoc


class ModelDoc(IModelDoc):
    def __init__(self):
        super().__init__()

    def get_custominfo(self):
        pass

    def get_configinfo(self):
        pass

    def get_summaryinfo(self):
        pass

    def set_custominfo(self):
        pass

    def set_configinfo(self):
        pass

    def set_summaryinfo(self, field_name, field_value):
        self._instance.SummaryInfo(field_name, field_value)

    # def __call__(self, name=None):
    #     if name is None:
    #         super()._modeldoc = super()._imodeldoc()
    #     else:
    #         pass
