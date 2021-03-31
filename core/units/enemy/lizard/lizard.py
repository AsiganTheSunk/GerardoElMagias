#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
import constants.globals
from core.skills.db.melee import MeleeSpells


class Lizard(EnemyUnit, MeleeSpells):
    def __init__(self, level, attack_power, attack_rating, magic_power, max_hp, max_mp, sound_master):
        EnemyUnit.__init__(self, 'Lizard', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)

        self.sound_master = sound_master
        self.animation_set = None
        self.animation_callbacks = None

        self.ultimate_strikes = 1
        self.fury_status = True

    def set_animations(self, animation_set, animation_callbacks):
        self.animation_set = animation_set
        self.animation_callbacks = animation_callbacks

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
