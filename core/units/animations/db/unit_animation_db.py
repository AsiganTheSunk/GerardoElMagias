from units.animations.constants.animation_resource import AnimationResource
from units.animations.constants.unit_animation_type import AnimationType
from enum import Enum


class UnitType(Enum):
    BANDIT = 'Bandit'
    THE_BOSS = 'The Boss'
    LIZARD = 'Lizard'
    DRAGON = 'Dragon'
    BONE_WIZARD = 'BoneWizard'
    HERO = 'Hero'
    DJINN = 'Djinn'


UNIT_ANIMATION_SETS = {
    UnitType.BANDIT: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(AnimationType.IDLE, 8),
        AnimationResource(AnimationType.DEATH, 10),
        AnimationResource(AnimationType.ATTACK, 8),
        AnimationResource(AnimationType.HURT, 3),
        AnimationResource(AnimationType.BLOCK, 9),
        AnimationResource(AnimationType.MISS, 5)
    ],

    UnitType.THE_BOSS: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(AnimationType.IDLE, 8),
        AnimationResource(AnimationType.DEATH, 10),
        AnimationResource(AnimationType.ATTACK, 8),
        AnimationResource(AnimationType.HURT, 3),
        AnimationResource(AnimationType.BLOCK, 9),
        AnimationResource(AnimationType.MISS, 5)
    ],

    UnitType.HERO: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(AnimationType.IDLE, 8),
        AnimationResource(AnimationType.DEATH, 10),
        AnimationResource(AnimationType.ATTACK, 8),
        AnimationResource(AnimationType.HURT, 3),
        AnimationResource(AnimationType.BLOCK, 9),
        AnimationResource(AnimationType.MISS, 5)
    ],

    UnitType.LIZARD: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(AnimationType.IDLE, 6),
        AnimationResource(AnimationType.DEATH, 6),
        AnimationResource(AnimationType.ATTACK, 5),
        AnimationResource(AnimationType.HURT, 4),
        AnimationResource(AnimationType.BLOCK, 4),
        AnimationResource(AnimationType.MISS, 4)
    ],


    UnitType.DRAGON: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(AnimationType.IDLE, 8),
        AnimationResource(AnimationType.DEATH, 10),
        AnimationResource(AnimationType.ATTACK, 8),
        AnimationResource(AnimationType.HURT, 3),
        AnimationResource(AnimationType.BLOCK, 9),
        AnimationResource(AnimationType.MISS, 5)
    ],

    UnitType.BONE_WIZARD: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Shadowbolt
        AnimationResource(AnimationType.IDLE, 5),
        AnimationResource(AnimationType.DEATH, 10),
        AnimationResource(AnimationType.ATTACK, 7),
        AnimationResource(AnimationType.HURT, 3),
        AnimationResource(AnimationType.BLOCK, 5),
        AnimationResource(AnimationType.MISS, 5),
        AnimationResource(AnimationType.SHADOWBOLT, 11)
    ],

    UnitType.DJINN: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Shadowbolt
        AnimationResource(AnimationType.IDLE, 3),
        AnimationResource(AnimationType.DEATH, 6),
        AnimationResource(AnimationType.ATTACK, 4),
        AnimationResource(AnimationType.HURT, 4),
        AnimationResource(AnimationType.BLOCK, 4),
        AnimationResource(AnimationType.MISS, 4)
    ]
}
