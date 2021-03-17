from enum import Enum


class UnitAnimationType(Enum):
    IDLE = 'Idle'
    ATTACK = 'Attack'
    HURT = 'Hurt'
    DEATH = 'Death'
    BLOCK = 'Block'
    MISS = 'Miss'
    SHADOWBOLT = "Shadowbolt"
    MATERIALIZE = "Materialize"


class SkillAnimationType(Enum):
    PRE_CAST = 'PreCast'
    CAST = 'Cast'
    POST_CAST = 'PostCast'
