"""Contains enumerations for SolidWorks options.
"""

from enum import Enum


class OpenDocOptions(Enum):
    LIGHTWEIGHT = 32
    RAPID_DRAFT = 8
    READ_ONLY = 2
    SILENT = 1
    LARGE_DESIGN_REVIEW = 4


class SummInfoField(Enum):
    AUTHOR = 2
    COMMENT = 4
    CREATE_DATE = 6
    CREATE_DATE2 = 8
    KEYWORDS = 3
    SAVE_DATE = 7
    SAVE_DATE2 = 9
    SAVED_BY = 5
    SUBJECT = 1
    TITLE = 0


class StandardViews(Enum):
    BACK = 2
    BOTTOM = 6
    DIMETRIC = 9
    FRONT = 1
    ISOMETRIC = 7
    LEFT = 3
    RIGHT = 4
    TOP = 5
    TRIMETRIC = 8


class SaveAsOptions(Enum):
    AVOID_REBUILD_ON_SAVE = 8
    COPY = 2
    DETACHED_DRAWING = 128
    IGNORE_BIOGRAPHY = 256
    OVERRIDE_SAVE_EMODEL = 32
    SAVE_REFERENCED = 4
    SILENT = 1
    UPDATE_INACTIVE_VIEWS = 16


class CustomPropertyAddOption(Enum):
    DELETE_AND_ADD = 1
    ONLY_IF_NEW = 0
    REPLACE_VALUE = 2
