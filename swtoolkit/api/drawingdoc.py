from .modeldoc import ModelDoc
from .interfaces.idrawingdoc import IDrawingDoc


class DrawingDoc(IDrawingDoc, ModelDoc):
    def __init__(self, system_object):
        super().__init__(system_object)
