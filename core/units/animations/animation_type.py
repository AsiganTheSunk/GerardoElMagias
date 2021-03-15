from enum import Enum


class AnimationType(Enum):
    IDLE = 'Idle'
    ATTACK = 'Attack'
    HURT = 'Hurt'
    DEATH = 'Death'
    BLOCK = 'Block'
    MISS = 'Miss'
    SHADOWBOLT = "Shadowbolt"

