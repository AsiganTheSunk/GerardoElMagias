#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
import constants.globals

# Skill Imports
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells


class Medusa(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, level, attack_power, attack_rating, magic_power, max_hp, max_mp, sound_master):
        EnemyUnit.__init__(self, 'Medusa', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.sound_master = sound_master
        self.animation_set = None
        self.animation_callbacks = None

        self.ultimate_strikes = 1
        self.fury_status = True
        self.action_counter = 1

    def set_animations(self, animation_set, animation_callbacks):
        self.animation_set = animation_set
        self.animation_callbacks = animation_callbacks

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_earth_shock_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(40):
            constants.globals.action_cooldown = -40
            self.cast_earth_shock(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('earth_shock_spell')
            return True

    def action(self, target, text_sprite):

        if self.action_counter % 2:
            self.use_attack(target, text_sprite)

        else:
            if self.current_mp > 40:
                self.use_earth_shock_spell([target], text_sprite)
            else:
                self.use_attack(target, text_sprite)

        self.action_counter += 1