from .assemblydoc import AssemblyDoc
from .com import COM
from .drawingdoc import DrawingDoc
from .enums.enum_options import DocumentTypes
from .partdoc import PartDoc


class Doc:
    class __Doc:
        def __init__(self, system_object=None):
            self.system_object = system_object
            del self

        @property
        def _instance(self):
            if self.system_object is None:
                self.system_object = COM("SldWorks.Application").ActiveDoc
            return self.system_object

        @property
        def _doc_type(self):
            return self._instance.GetType

        @property
        def doc(self):
            if self._doc_type == DocumentTypes.ASSEMBLY.value:
                return AssemblyDoc(self._instance)
            elif self._doc_type == DocumentTypes.PART.value:
                return PartDoc(self._instance)
            elif self._doc_type == DocumentTypes.DRAWING.value:
                return DrawingDoc(self._instance)
            else:
                raise ValueError(self._doc_type)

    def __new__(cls, system_object=None):
        return cls.__Doc(system_object).doc
