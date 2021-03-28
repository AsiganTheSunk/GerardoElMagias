#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.skills.effects_db.fire_skill_effect import FireSkillEffect
from core.skills.effects_db.earth_skill_effect import EarthSkillEffect
from core.skills.effects_db.magic_nova_skill_effect import MagicNovaSkillEffect


class StageEffectsRenderer:
    def __init__(self, animation_master):
        self.animation_master = animation_master
        self.animation_effects = []

    def add_effect(self, target_list, spell):
        if spell == 'firestorm':
            for target in target_list:
                fire_storm_effect = FireSkillEffect(target, self.animation_master)
                self.animation_effects.append(fire_storm_effect)

        if spell == 'earth':
            for target in target_list:
                earth_effect = EarthSkillEffect(target, self.animation_master)
                self.animation_effects.append(earth_effect)

        if spell == 'magic_nova':
            for target in target_list:
                magic_nova_effect = MagicNovaSkillEffect(target, self.animation_master)
                self.animation_effects.append(magic_nova_effect)

    def update_effects(self):
        if self.animation_effects:
            for animation_effect_index, animation_effect in enumerate(self.animation_effects):
                if animation_effect.target_skill_set_effect.update():
                    self.animation_effects.pop(animation_effect_index)
                animation_effect.target_skill_set_effect.draw()