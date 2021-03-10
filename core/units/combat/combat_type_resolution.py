from enum import Enum


class CombatTypeResolution(Enum):
    HIT = 'Hit'
    CRITICAL_HIT = 'Critical Hit'
    MISS = 'Miss'
    BLOCKED = 'Blocked'
    RESIST = 'Resist'
    ABSORBED = 'Absorbed'
