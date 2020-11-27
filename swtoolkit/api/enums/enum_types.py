"""Contains enumerations for SolidWorks Types."""

from enum import Enum


class DocumentTypes(Enum):
    ASSEMBLY = 2
    DRAWING = 3
    IMPORTED_ASSEMBLY = 7
    IMPORTED_PART = 6
    LAYOUT = 5
    NONE = 0
    PART = 1
    SDM = 4


class CustomInfoType(Enum):
    DATE = 64
    DOUBLE = 5
    NUMBER = 3
    TEXT = 30
    UNKNOWN = 0
    YES_OR_NO = 11
