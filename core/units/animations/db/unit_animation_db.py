from units.animations.constants.animation_resource import AnimationResource
from units.animations.constants.unit_animation_type import UnitAnimationType, SkillAnimationType
from enum import Enum


class UnitType(Enum):
    BANDIT = 'Bandit'
    THE_BOSS = 'The Boss'
    LIZARD = 'Lizard'
    DRAGON = 'Dragon'
    BONE_WIZARD = 'BoneWizard'
    HERO = 'Hero'
    DJINN = 'Djinn'


class SkillType(Enum):
    FIRESTORM = 'Firestorm'


SKILL_ANIMATION_SETS = {
    SkillType.FIRESTORM: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(SkillAnimationType.PRE_CAST, 8),
        AnimationResource(SkillAnimationType.CAST, 10),
        AnimationResource(SkillAnimationType.POST_CAST, 8),
    ],
}

UNIT_ANIMATION_SETS = {
    UnitType.BANDIT: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(UnitAnimationType.IDLE, 8),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 8),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 9),
        AnimationResource(UnitAnimationType.MISS, 5)
    ],

    UnitType.THE_BOSS: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(UnitAnimationType.IDLE, 8),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 8),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 9),
        AnimationResource(UnitAnimationType.MISS, 5)
    ],

    UnitType.HERO: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(UnitAnimationType.IDLE, 8),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 8),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 9),
        AnimationResource(UnitAnimationType.MISS, 5)
    ],

    UnitType.LIZARD: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(UnitAnimationType.IDLE, 6),
        AnimationResource(UnitAnimationType.DEATH, 6),
        AnimationResource(UnitAnimationType.ATTACK, 5),
        AnimationResource(UnitAnimationType.HURT, 4),
        AnimationResource(UnitAnimationType.BLOCK, 4),
        AnimationResource(UnitAnimationType.MISS, 4)
    ],


    UnitType.DRAGON: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(UnitAnimationType.IDLE, 8),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 8),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 9),
        AnimationResource(UnitAnimationType.MISS, 5)
    ],

    UnitType.BONE_WIZARD: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Shadowbolt
        AnimationResource(UnitAnimationType.IDLE, 5),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 7),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 5),
        AnimationResource(UnitAnimationType.MISS, 5),
        AnimationResource(UnitAnimationType.SHADOWBOLT, 11)
    ],

    UnitType.DJINN: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Shadowbolt
        AnimationResource(UnitAnimationType.IDLE, 3),
        AnimationResource(UnitAnimationType.DEATH, 6),
        AnimationResource(UnitAnimationType.ATTACK, 4),
        AnimationResource(UnitAnimationType.HURT, 4),
        AnimationResource(UnitAnimationType.BLOCK, 4),
        AnimationResource(UnitAnimationType.MISS, 4)
    ]
}
