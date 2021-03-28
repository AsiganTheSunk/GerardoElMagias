#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.skills.basic_skill_effect import BasicSkillEffect
from core.game.animations.sets.skill_animation_set import SkillAnimationSet


class EarthSkillEffect(BasicSkillEffect):
    def __init__(self, target, animation_master):
        BasicSkillEffect.__init__(self, target)

        self.animation_master = animation_master
        # Establish Target Center
        target_x, target_y = self.target_center
        if self.caster_center is not None:
            caster_x, caster_y = self.caster_center

        self.skill_set = SkillAnimationSet(self.animation_master.surface,
                                           target_x, target_y, 'Earth',
                                           self.animation_master.get_skill_resource_animation_set('Earth'))