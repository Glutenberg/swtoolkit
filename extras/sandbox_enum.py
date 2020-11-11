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


class OpenDocOptions(Enum):
    LIGHTWEIGHT = 32
    RAPID_DRAFT = 8
    READ_ONLY = 2
    SILENT = 1
    LARGE_DESIGN_REVIEW = 4


def convert_to_const(string: str):
    return string.upper().replace(" ", "_")
