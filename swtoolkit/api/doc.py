from .assemblydoc import AssemblyDoc
from .partdoc import PartDoc
from .drawingdoc import DrawingDoc
from .enums.enum_options import DocumentTypes


class Doc:
    def __new__(cls, system_object):
        object_type = cls._get_type(system_object)
        return cls._get_object(system_object, object_type)

    def _get_type(system_object):
        return system_object.GetType

    def _get_object(system_object, object_type: int):
        if object_type == DocumentTypes.ASSEMBLY:
            return AssemblyDoc(system_object)
        elif object_type == DocumentTypes.PART:
            return PartDoc(system_object)
        elif object_type == DocumentTypes.DRAWING:
            return DrawingDoc(system_object)
        else:
            raise ValueError(object_type)
