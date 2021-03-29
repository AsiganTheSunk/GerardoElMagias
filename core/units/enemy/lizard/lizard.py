#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
import constants.globals

# Skill Imports
from core.skills.db.melee import MeleeSpells

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet


class Lizard(EnemyUnit, MeleeSpells):
    def __init__(self, x, y, level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                 health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'Lizard', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.sound_master = sound_master
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'Lizard', animation_master.get_unit_animation_set('Lizard'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('Lizard')

        self.ultimate_strikes = 1
        self.fury_status = True

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def action(self, target, text_sprite):
        if self.has_enough_fury(40):
            if self.ultimate_strikes < 3:
                self.use_attack(target, text_sprite)
                self.ultimate_strikes += 1
                constants.globals.action_cooldown = 70
            else:
                self.use_attack(target, text_sprite)
                self.ultimate_strikes = 1
                self.current_fury = 0
        else:
            self.use_attack(target, text_sprite)
