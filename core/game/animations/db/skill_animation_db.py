#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.animations.animation_resource import AnimationResource
from core.game.animations.constants.skill_animation_type import SkillAnimationType
from core.skills.constants.skill_type import SkillType


SKILL_ANIMATION_SETS = {
    SkillType.FIRE_STORM: [
        AnimationResource(SkillAnimationType.CAST, 6),
    ],

    SkillType.EARTH_SHOCK: [
        AnimationResource(SkillAnimationType.CAST, 9),
    ],

    SkillType.WATER_NOVA: [
        AnimationResource(SkillAnimationType.CAST, 12),
    ],
}
