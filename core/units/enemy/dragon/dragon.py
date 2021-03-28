#!/usr/bin/env python
# -*- coding: utf-8 -*-

import constants.globals
from random import randint

from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells
from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
from core.units.player.resources.stash import Stash

from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class Dragon(EnemyUnit, MagicSpells, MeleeSpells):
    def __init__(self, x, y, level, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master):
        EnemyUnit.__init__(self, x, y, 'Dragon', level, strength, dexterity, magic)
        MeleeSpells.__init__(self)
        MagicSpells.__init__(self)
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.stash = Stash(healing_potions=round(self.level / 5), mana_potions=0, gold=0)

        self.animation_set = UnitAnimationSet(animation_master.surface, x, y,
                                              'Dragon', animation_master.get_unit_resource_animation_set('Dragon'))

    def attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_attack(self, target, damage_text_group)
        return True

    def use_heal(self, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False

    def use_firestorm(self, target_list, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):
            constants.globals.action_cooldown = -30
            self.cast_firestorm(self, target_list, damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False

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

    def action(self, target, damage_text_group):
        health_trigger = self.current_hp <= round(self.max_hp * 0.70)
        if health_trigger:
            i = randint(1, 3)
            if i == 1:
                self.attack(target, damage_text_group)
            elif i == 2:
                if self.current_mp >= 12:
                    self.use_heal(damage_text_group)
                else:
                    self.attack(target, damage_text_group)
            elif i == 3:
                if self.current_mp >= 15:
                    self.use_firestorm([target], damage_text_group)
                else:
                    self.attack(target, damage_text_group)
        else:
            self.attack(target, damage_text_group)

