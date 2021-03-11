from enum import Enum


class SoundType(Enum):
    ATTACK = 'Attack'
    HURT = 'Hurt'
    HIT = 'Hit'
    CRITICAL_HIT = 'CriticalHit'
    DEATH = 'Death'
    BLOCK = 'Block'
    MISS = 'Miss'
    CLICK = 'Click'

