"""Contains enumerations for SolidWorks Results."""

from enum import Enum


class CustomInfoAddResult(Enum):
    ADDED_OR_CHANGED = 0
    GENERIC_FAIL = 1
    MISMATCH_AGAINST_EXISTING_TYPE = 2
    MISMATCH_AGAINSTE_SPECIFIC_TYPE = 3


class CustomInfoDeleteResult(Enum):
    LINKED_PROP = 2
    NOT_PRESENT = 1
    OK = 0


class CustomInfoGetResult(Enum):
    CACHED_VALUE = 0
    NOT_PRESENT = 1
    RESOLVED_VALUE = 2


class CustomInfoSetResult(Enum):
    LINKED_PROP = 3
    NOT_PRESENT = 1
    OK = 0
    TYPE_MISMATCH = 2
