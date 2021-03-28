#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.skills.basic_skill_effect import BasicSkillEffect
from core.game.animations.sets.skill_animation_set import SkillAnimationSet


class FireSkillEffect(BasicSkillEffect):
    def __init__(self, target, animation_master):
        BasicSkillEffect.__init__(self, target)

        self.animation_master = animation_master
        # Experimental Skill Animation
        target_x, target_y = target.animation_set.rect.center
        self.skill_set = SkillAnimationSet(self.animation_master.surface,
                                           target_x, target_y, 'Firestorm',
                                           self.animation_master.get_skill_resource_animation_set('Firestorm'))

