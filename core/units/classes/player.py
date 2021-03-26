#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.resources.mana_bar import ManaBar
from core.units.resources.stash import Stash

from core.units.skills.magic import MagicSpells
from core.units.skills.melee import MeleeSpells
from core.units.skills.fury import FurySpells

from core.units.resources.fury_bar import FuryBar
from core.units.mechanics.experience import ExperienceSystem

from core.units.combat.utils import get_alive_targets_status
from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText

from constants.sound import *
import constants.globals

from core.units.mechanics.loot import LootPool
from core.units.basic_unit import PlayerUnit
from core.units.resources.health_bar import HealthBar

from random import randint

# Text Import

# Combat Imports
from core.units.combat.combat_formulas import CombatFormulas
from core.units.combat.combat_resolver import CombatResolver

# Animation Imports
from core.units.animations.sets.unit_animation_set import UnitAnimationSet

# Consumable Items
from core.items.item_db.consumable_item_db import HEALTH_POTION, MANA_POTION, REJUVENATION_POTION

import constants.globals

combat_resolver = CombatResolver()
combat_formulas = CombatFormulas()


# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class HeroPlayer(PlayerUnit, MeleeSpells, MagicSpells, FurySpells, UnitAnimationSet):
    def __init__(self, x, y, name, level, strength, dexterity, magic, vitality, resilience, luck, health_bar_x, health_bar_y, mana_bar_x, mana_bar_y, fury_bar_x, fury_bar_y, animation_master):
        PlayerUnit.__init__(self, x, y, name, level, strength, dexterity, magic, vitality, resilience, luck)
        FurySpells.__init__(self)
        MeleeSpells.__init__(self)
        MagicSpells.__init__(self)

        self.animation_set = UnitAnimationSet(animation_master.surface, x, y, name, animation_master.get_unit_resource_animation_set('Hero'))

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.mana_bar = ManaBar(mana_bar_x, mana_bar_y, self.current_mp, self.max_mp)
        self.fury_bar = FuryBar(fury_bar_x, fury_bar_y, self.current_fury, self.max_fury)
        self.stash = Stash()

        self.experience_system = ExperienceSystem()

        self.experience_to_gain = 0

        self.current_fury = 0
        self.experience = 0
        self.exp_level_break = 5
        self.fury_status = True
        self.experience_status = True

        self.loot_pool = LootPool()

    def attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_attack(self, target, damage_text_group)
        return True

    def loot(self, target, damage_text_group):
        self.loot_pool.loot(self, target, damage_text_group)

    def use_ultimate(self, target_list, damage_text_group):
        self.cast_path_of_the_seven_strikes(self, target_list, damage_text_group)
        return True

    def use_heal(self, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, damage_text_group)
            return True

        self.no_action_error('Mana', damage_text_group)
        return False

    def use_firestorm(self, target_list, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):
            constants.globals.action_cooldown = -30
            # Pre Save State for Enemy List: target_list
            pre_target_list = get_alive_targets_status(target_list)

            # Retrieve State for Enemy List: target_list
            self.cast_firestorm(self, target_list, damage_text_group)

            # Post Save State for Enemy List: target_list
            pos_target_list = get_alive_targets_status(target_list)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list,
                                                       damage_text_group)
            return True

        self.no_action_error('Mana', damage_text_group)
        return False

    def use_lightning(self, target_list, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(20):
            constants.globals.action_cooldown = -30
            # Save State for Enemy List: target_list
            pre_target_list = get_alive_targets_status(target_list)

            self.cast_lightning(self, target_list, damage_text_group)
            # Retrieve State for Enemy List: target_list
            pos_target_list = get_alive_targets_status(target_list)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list,
                                                       damage_text_group)
            return True

        self.no_action_error('Mana', damage_text_group)
        return False

    def use_healing_potion(self, damage_text_group):
        if self.stash.has_healing_potion():
            constants.globals.action_cooldown = 0

            self.stash.consume_healing_potion()
            HEALTH_POTION.consume(self, damage_text_group)
            return True

        self.no_action_error(HEALTH_POTION.name, damage_text_group)
        return False

    def use_mana_potion(self, damage_text_group):
        if self.stash.has_mana_potion():
            constants.globals.action_cooldown = 0

            self.stash.consume_mana_potion()
            MANA_POTION.consume(self, damage_text_group)
            return True

        self.no_action_error(MANA_POTION.name, damage_text_group)
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

    def no_action_error(self, name, text_sprite):
        damage_text.warning(self, f' No {name} !', text_sprite)
        error_sound.play()

    def gain_experience(self):
        self.experience = self.experience + self.experience_to_gain
        self.experience_to_gain = 0
        if self.experience >= self.exp_level_break:
            self.level_up()


    def level_up(self):
        strength_raise = randint(2, 3)
        dexterity_raise = randint(1, 2)
        magic_raise = randint(1, 3)
        vitality_raise = randint(2, 3)
        resilience_raise = randint(2, 3)
        luck_raise = randint(2, 3)

        self.level_up_stats(strength_raise, dexterity_raise, magic_raise, vitality_raise, resilience_raise, luck_raise)

        self.exp_level_break = round(self.exp_level_break * 1.6)
        self.level += 1
