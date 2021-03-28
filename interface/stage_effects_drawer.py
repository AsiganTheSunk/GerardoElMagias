from core.units.skill_effects import FireSkillEffect
from core.units.skill_effects import EarthSkillEffect
from core.units.skill_effects import MagicNovaSkillEffect

class StageEffectsDrawer:
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

        if spell == 'magicnova':
            for target in target_list:
                magicnova_effect = MagicNovaSkillEffect(target, self.animation_master)
                self.animation_effects.append(magicnova_effect)

    def update_effects(self):
        if self.animation_effects:
            for animation_effect_index, animation_effect in enumerate(self.animation_effects):
                if animation_effect.skill_set.update():
                    self.animation_effects.pop(animation_effect_index)
                animation_effect.skill_set.draw()