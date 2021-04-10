#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from random import randint
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells


class BoneWizard(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, level, attack_power, attack_rating, magic_power, max_hp, max_mp, sound_master):
        EnemyUnit.__init__(self, 'BoneWizard', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.sound_master = sound_master
        self.animation_set = None
        self.animation_callbacks = None

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

    def use_shadow_bolt(self, target, text_sprite):
        if self.reduce_mana(20):
            self.use_animation('ShadowBolt')
            self.cast_shadow_bolt(self, target, text_sprite)
            return True
        return False

    def action(self, target, text_sprite):
        random_action = randint(1, 2)

        if random_action == 1:
            self.use_shadow_bolt(target, text_sprite)

        if random_action == 2:
            self.use_attack(target, text_sprite)
