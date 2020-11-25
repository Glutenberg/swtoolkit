from enum import Enum


class ComponentSuppressionState(Enum):
    FULLY_LIGHTWEIGHT = 4  # Recursive
    FULLY_RESOLVED = 2  # Recursive
    INTERNAL_ID_MISMATCH = 5
    LIGHTWEIGHT = 1
    RESOLVED = 3
    SUPPRESSED = 0


class CustomInfoAddResult(Enum):
    ADDED_OR_CHANGED = 0
    GENERIC_FAIL = 1
    MISMATCH_AGAINST_EXISTING_TYPE = 2
    MISMATCH_AGAINSTE_SPECIFIC_TYPE = 3