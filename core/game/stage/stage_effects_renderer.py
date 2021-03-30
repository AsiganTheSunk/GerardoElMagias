#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.skills.effects_db.fire_skill_effect import FireSkillEffect
from core.skills.effects_db.earth_skill_effect import EarthShockSkillEffect
from core.skills.effects_db.water_nova_skill_effect import WaterNovaSkillEffect
from core.skills.effects_db.lightnning_skills_effect import LightningSkillEffect


class StageEffectsRenderer:
    def __init__(self, animation_master):
        self.animation_master = animation_master
        self.animation_effects = []

    def add_effect(self, target_list, spell):
        if spell == 'firestorm':
            for target in target_list:
                firestorm_effect = FireSkillEffect(target, self.animation_master)
                self.animation_effects.append(firestorm_effect)

        if spell == 'earth_shock':
            for target in target_list:
                earth_effect = EarthShockSkillEffect(target, self.animation_master)
                self.animation_effects.append(earth_effect)

        if spell == 'water_nova':
            for target in target_list:
                magic_nova_effect = WaterNovaSkillEffect(target, self.animation_master)
                self.animation_effects.append(magic_nova_effect)

        if spell == 'lightning':
            for target in target_list:
                magic_nova_effect = LightningSkillEffect(target, self.animation_master)
                self.animation_effects.append(magic_nova_effect)

    def update_effects(self):
        if self.animation_effects:
            for animation_effect_index, animation_effect in enumerate(self.animation_effects):
                if animation_effect.target_skill_set_effect.update():
                    self.animation_effects.pop(animation_effect_index)
                animation_effect.target_skill_set_effect.draw()
