#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.animations.animation_resource import AnimationResource
from core.game.animations.constants.skill_animation_type import SkillAnimationType
from enum import Enum


class SkillType(Enum):
    FIRESTORM = 'Firestorm'


SKILL_ANIMATION_SETS = {
    SkillType.FIRESTORM: [
        AnimationResource(SkillAnimationType.CAST, 6),
    ],

    SkillType.EARTH: [
        AnimationResource(SkillAnimationType.CAST, 9),
    ],

    SkillType.MAGICNOVA: [
        AnimationResource(SkillAnimationType.CAST, 12),
    ],
}