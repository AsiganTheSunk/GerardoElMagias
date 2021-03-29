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
    def __init__(self, x, y, level, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master):
        EnemyUnit.__init__(self, x, y, 'Lizard', level, strength, dexterity, magic)
        MeleeSpells.__init__(self)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'Lizard', animation_master.get_unit_animation_set('Lizard'))

        self.ultimate_strikes = 1
        self.fury_status = True

    def attack(self, target, text_sprite):
        self.melee_attack_animation()
        self.cast_attack(self, target, text_sprite)
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

    def action(self, target, text_sprite):
        if self.has_enough_fury(40):
            if self.ultimate_strikes < 3:
                self.attack(target, text_sprite)
                self.ultimate_strikes += 1
                constants.globals.action_cooldown = 70
            else:
                self.attack(target, text_sprite)
                self.ultimate_strikes = 1
                self.current_fury = 0
        else:
            self.attack(target, text_sprite)
