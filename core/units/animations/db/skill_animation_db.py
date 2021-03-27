#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.animations.constants.animation_resource import AnimationResource
from core.units.animations.constants.unit_animation_type import UnitAnimationType, SkillAnimationType
from enum import Enum


class SkillType(Enum):
    FIRESTORM = 'Firestorm'


SKILL_ANIMATION_SETS = {
    SkillType.FIRESTORM: [
        # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss,
        AnimationResource(SkillAnimationType.CAST, 6),
    ],
}