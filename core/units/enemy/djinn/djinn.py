#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar

# Skill Imports
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet
from random import randint
import constants.globals


class Djinn(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, level, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'Djinn', level, strength, dexterity, magic)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.sound_master = sound_master
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'Djinn', animation_master.get_unit_animation_set('Djinn'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('Djinn')

        self.fury_status = True
        self.power_of_two_exponent = 1
        self.animation_set.action = 6
        self.action_counter = 1

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def power_of_two_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_power_of_two_attack(target, text_sprite, self.power_of_two_exponent)
        self.power_of_two_exponent += 1
        return True

    def use_heal(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, text_sprite)
            self.sound_master.play_spell_fx_sound('heal_spell')
            return True
        return False

    def action(self, target, text_sprite):
        health_trigger = self.current_hp <= round(self.max_hp * 0.70)
        if self.action_counter % 2:
            self.attack(target, text_sprite)
        else:
            if health_trigger:
                random_action = randint(1, 2)
                if random_action == 1:
                    if self.current_mp >= 12:
                        self.use_heal(text_sprite)
                    else:
                        self.power_of_two_attack(target, text_sprite)
                if random_action == 2:
                    self.power_of_two_attack(target, text_sprite)

            else:
                self.power_of_two_attack(target, text_sprite)
        self.action_counter += 1
