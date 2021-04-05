#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
from random import randint
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells
from core.game.animations.sets.unit_animation_set import UnitAnimationSet


class BoneWizard(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                 health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'BoneWizard', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.sound_master = sound_master
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'BoneWizard', animation_master.get_unit_animation_set('BoneWizard'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('BoneWizard')

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
