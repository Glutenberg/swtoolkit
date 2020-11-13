from .interfaces.icomponent import IComponent


class Component(IComponent):
    def __init__(self, system_object):
        super().__init__(system_object)

    def __repr__(self):
        return f"{self.__class__.__name__} <{self.name}>"

    def __str__(self):
        return self.name
