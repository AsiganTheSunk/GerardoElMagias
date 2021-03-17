from core.units.basic_unit import BasicUnit
from core.units.resources.health_bar import HealthBar

# Skill Imports
from core.units.skills.melee import MeleeSpells
from core.units.skills.magic import MagicSpells

# Animation Imports
from core.units.animations.sets.unit_animation_set import UnitAnimationSet

from random import randint
import constants.globals


class Djinn(BasicUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        MeleeSpells.__init__(self)
        MagicSpells.__init__(self)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        # Bandit Loot
        self.looted_status = False
        self.animation_set = UnitAnimationSet(animation_master.surface, x, y, name, animation_master.get_unit_resource_animation_set('Djinn'))
        self.current_fury = 1
        self.fury_status = True
        self.power_of_two_exponent = 0
        self.animation_set.action = 6


    def is_looted(self):
        return self.looted_status

    def update_looted_status(self):
        self.looted_status = True

    def attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_attack(self, target, damage_text_group)
        return True

    def power_of_two_attack(self, target, damage_text_group):
        exponent = self.power_of_two_exponent
        self.cast_power_of_two_attack(target, damage_text_group, exponent)
        self.power_of_two_exponent += 1

    def use_heal(self, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, damage_text_group)
            return True

    def death_animation(self):
        # Activates: Death Animation
        self.animation_set.action = 1
        self.animation_set.reset_frame_index()

    def melee_attack_animation(self):
        # Activates: Melee Attack Animation
        self.animation_set.action = 2
        self.animation_set.reset_frame_index()

    def hurt_animation(self):
        # Activates: Hurt Animation
        self.animation_set.action = 3
        self.animation_set.reset_frame_index()

    def block_animation(self):
        # Activates: Block Animation
        self.animation_set.action = 4
        self.animation_set.reset_frame_index()

    def miss_animation(self):
        # Activates: Miss Animation
        self.animation_set.action = 5
        self.animation_set.reset_frame_index()



    def action(self, target, damage_text_group):
        health_trigger = self.current_hp <= round(self.max_hp * 0.7)
        if health_trigger:
            i = randint(1, 2)
            if i == 1:
                self.use_heal(damage_text_group)
            if i == 2:
                self.power_of_two_attack(target, damage_text_group)

        else:
            self.power_of_two_attack(target, damage_text_group)