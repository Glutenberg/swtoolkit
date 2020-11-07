from .interfaces.imodeldoc import IModelDoc


class ModelDoc(IModelDoc):
    def __init__(self, parent=None):
        super().__init__(parent)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.parent},{self.get_title()})"

    def __str__(self):
        return self.get_title()

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
