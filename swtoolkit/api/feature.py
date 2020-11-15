from .interfaces.ifeature import IFeature


class Feature(IFeature):
    def __init__(self, system_object):
        super().__init__(system_object)

    def __repr__(self):
        return f"{self.__class__.__name__} <{self.name}> <{self.identity}>"

    def __str__(self):
        return f"{self.name}"
