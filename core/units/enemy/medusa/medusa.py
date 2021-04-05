#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
import constants.globals

# Skill Imports
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet


class Medusa(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                 health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'Medusa', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.sound_master = sound_master
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'Medusa', animation_master.get_unit_animation_set('Medusa'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('Medusa')

        self.ultimate_strikes = 1
        self.fury_status = True
        self.action_counter = 1

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