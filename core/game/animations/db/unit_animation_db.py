#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.animations.animation_resource import AnimationResource
from core.game.animations.constants.unit_animation_type import UnitAnimationType
from core.units.constants.unit_type import UnitType


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

    UnitType.BANDIT_CHIEF: [
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


    UnitType.SMALLDRAGON: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
        AnimationResource(UnitAnimationType.IDLE, 8),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 8),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 9),
        AnimationResource(UnitAnimationType.MISS, 5)
    ],

    UnitType.BONE_WIZARD: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Materialize, 7: ShadowBolt
        AnimationResource(UnitAnimationType.IDLE, 5),
        AnimationResource(UnitAnimationType.DEATH, 10),
        AnimationResource(UnitAnimationType.ATTACK, 7),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 5),
        AnimationResource(UnitAnimationType.MISS, 5),
        AnimationResource(UnitAnimationType.MATERIALIZE, 10),
        AnimationResource(UnitAnimationType.SHADOWBOLT, 11)
    ],

    UnitType.DJINN: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Materialize
        AnimationResource(UnitAnimationType.IDLE, 3),
        AnimationResource(UnitAnimationType.DEATH, 6),
        AnimationResource(UnitAnimationType.ATTACK, 4),
        AnimationResource(UnitAnimationType.HURT, 4),
        AnimationResource(UnitAnimationType.BLOCK, 4),
        AnimationResource(UnitAnimationType.MISS, 8),
        AnimationResource(UnitAnimationType.MATERIALIZE, 5)
    ],

    UnitType.DEMON: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Materialize
        AnimationResource(UnitAnimationType.IDLE, 4),
        AnimationResource(UnitAnimationType.DEATH, 6),
        AnimationResource(UnitAnimationType.ATTACK, 4),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 3),
        AnimationResource(UnitAnimationType.MISS, 3),
        AnimationResource(UnitAnimationType.MATERIALIZE, 4)
    ],

    UnitType.DRAGON: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Materialize
        AnimationResource(UnitAnimationType.IDLE, 4),
        AnimationResource(UnitAnimationType.DEATH, 5),
        AnimationResource(UnitAnimationType.ATTACK, 4),
        AnimationResource(UnitAnimationType.HURT, 2),
        AnimationResource(UnitAnimationType.BLOCK, 3),
        AnimationResource(UnitAnimationType.MISS, 3),
        AnimationResource(UnitAnimationType.MATERIALIZE, 4)
    ],

    UnitType.MEDUSA: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss, 6: Materialize
        AnimationResource(UnitAnimationType.IDLE, 3),
        AnimationResource(UnitAnimationType.DEATH, 6),
        AnimationResource(UnitAnimationType.ATTACK, 6),
        AnimationResource(UnitAnimationType.HURT, 3),
        AnimationResource(UnitAnimationType.BLOCK, 4),
        AnimationResource(UnitAnimationType.MISS, 4),
    ]
}
