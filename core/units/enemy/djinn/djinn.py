#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells
from random import randint


class Djinn(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, level, attack_power, attack_rating, magic_power, max_hp, max_mp, sound_master):
        EnemyUnit.__init__(self, 'Djinn', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.sound_master = sound_master
        self.animation_set = None
        self.animation_callbacks = None

        self.fury_status = True
        self.power_of_two_exponent = 1
        self.action_counter = 1

    def set_animations(self, animation_set, animation_callbacks):
        self.animation_set = animation_set
        self.animation_callbacks = animation_callbacks
        self.animation_set.action = 6

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_power_of_two_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_power_of_two_attack(target, text_sprite, self.power_of_two_exponent)
        self.power_of_two_exponent += 1
        return True

    def use_heal(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(25):
            self.cast_heal(self, self, text_sprite)
            self.sound_master.play_spell_fx_sound('heal_spell')
            return True
        return False

    def action(self, target, text_sprite):
        health_trigger = self.current_hp <= round(self.max_hp * 0.70)
        if self.action_counter % 2:
            self.use_attack(target, text_sprite)
        else:
            if health_trigger:
                random_action = randint(1, 2)
                if random_action == 1:
                    if self.current_mp >= 25:
                        self.use_heal(text_sprite)
                    else:
                        self.use_power_of_two_attack(target, text_sprite)
                if random_action == 2:
                    self.use_power_of_two_attack(target, text_sprite)

            else:
                self.use_power_of_two_attack(target, text_sprite)
        self.action_counter += 1
