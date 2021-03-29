#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
from core.game.text.damage_text import DamageText

# Text Import
from random import randint

# Skill Imports
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet

damage_text = DamageText()


class BoneWizard(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, level, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master):
        EnemyUnit.__init__(self, x, y, 'BoneWizard', level, strength, dexterity, magic)
        MeleeSpells.__init__(self)
        MagicSpells.__init__(self)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'BoneWizard', animation_master.get_unit_animation_set('BoneWizard'))

        self.animation_set.action = 6

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

    def materialize_animation(self):
        # Activates: Materialize Animation
        self.animation_set.action = 6
        self.animation_set.reset_frame_index()

    def shadow_bolt_animation(self):
        # Activates: Shadowbolt Animation
        self.animation_set.action = 7
        self.animation_set.reset_frame_index()

    def use_shadow_bolt(self, target, text_sprite):
        if self.reduce_mana(10):
            self.shadow_bolt_animation()
            damage_text.cast(self, "Shadow Bolt!", text_sprite, 0, -30)
            self.cast_shadow_bolt(self, target, text_sprite)
            return True
        return False

    def action(self, target, text_sprite):
        random_action = randint(1, 2)
        if random_action == 1:
            if self.use_shadow_bolt(target, text_sprite):
                pass
            else:
                self.attack(target, text_sprite)
        if random_action == 2:
            self.attack(target, text_sprite)
