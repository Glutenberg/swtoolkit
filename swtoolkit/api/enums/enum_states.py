from enum import Enum


class ComponentSuppressionState(Enum):
    FULLY_LIGHTWEIGHT = 4  # Recursive
    FULLY_RESOLVED = 2  # Recursive
    INTERNAL_ID_MISMATCH = 5
    LIGHTWEIGHT = 1
    RESOLVED = 3
    SUPPRESSED = 0
