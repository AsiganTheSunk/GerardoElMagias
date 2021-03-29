#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.resources.mana_bar import ManaBar
from core.units.player.resources.stash import Stash
from core.skills.db.magic import MagicSpells
from core.skills.db.melee import MeleeSpells
from core.skills.db.fury import FurySpells
from core.units.resources.fury_bar import FuryBar
from core.game.mechanics.experience import ExperienceMaster
from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText
import constants.globals
from core.game.mechanics.loot import LootPool
from core.units.player_unit import PlayerUnit
from core.units.resources.health_bar import HealthBar
from random import randint

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet

# Consumable Items
from core.items.consumable.db.consumable_db import HEALTH_POTION, MANA_POTION
import constants.globals

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class HeroPlayer(PlayerUnit, MeleeSpells, MagicSpells, FurySpells, UnitAnimationSet):
    def __init__(self, x, y, level, strength, dexterity, magic, vitality, resilience, luck, health_bar_x, health_bar_y, mana_bar_x, mana_bar_y, fury_bar_x, fury_bar_y, animation_master, sound_master):
        PlayerUnit.__init__(self, x, y, "Hero", level, strength, dexterity, magic, vitality, resilience, luck)
        FurySpells.__init__(self, sound_master)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y, 'Hero',
                             animation_master.get_unit_animation_set('Hero'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('Hero')

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.mana_bar = ManaBar(mana_bar_x, mana_bar_y, self.current_mp, self.max_mp)
        self.fury_bar = FuryBar(fury_bar_x, fury_bar_y, self.current_fury, self.max_fury)
        self.stash = Stash()

        self.experience_system = ExperienceMaster()

        self.experience_to_gain = 0
        self.previous_exp = 0

        self.current_fury = 0
        self.experience = 0
        self.exp_level_break = 5
        self.fury_status = True
        self.experience_status = True

        self.loot_pool = LootPool(self.sound_master)

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def get_loot(self, target, text_sprite):
        self.loot_pool.loot(self, target, text_sprite)

    def attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_ultimate(self, target_list, text_sprite):
        self.cast_path_of_the_seven_strikes(self, target_list, text_sprite)
        return True

    def use_whirlwind(self, target_list, text_sprite):
        self.use_animation('Attack')
        self.cast_whirlwind(self, target_list, text_sprite)
        return True

    def use_heal_spell(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, text_sprite)
            self.sound_master.play_spell_fx_sound('heal_spell')
            return True
        self.no_action_error('Mana', text_sprite)
        return False

    def use_firestorm_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(20):
            constants.globals.action_cooldown = -30
            self.experience_system.aoe_experience_helper(self, target_list, self.cast_firestorm, text_sprite)
            self.sound_master.play_spell_fx_sound('firestorm_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_lightning_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(16):
            constants.globals.action_cooldown = -30
            self.experience_system.aoe_experience_helper(self, target_list, self.cast_lightning, text_sprite)
            self.sound_master.play_spell_fx_sound('lightning_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_earth_shock_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(14):
            constants.globals.action_cooldown = -40
            self.experience_system.aoe_experience_helper(self, target_list, self.cast_earth_shock, text_sprite)
            self.sound_master.play_spell_fx_sound('earth_shock_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_water_nova_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(18):
            constants.globals.action_cooldown = -50
            self.experience_system.aoe_experience_helper(self, target_list, self.cast_water_nova, text_sprite)
            self.sound_master.play_spell_fx_sound('earth_shock_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_healing_potion(self, text_sprite):
        if self.stash.consume_healing_potion():
            constants.globals.action_cooldown = 0
            HEALTH_POTION.consume(self, text_sprite)
            self.sound_master.play_item_fx_sound('health_potion')
            return True

        self.no_action_error(HEALTH_POTION.name, text_sprite)
        return False

    def use_mana_potion(self, text_sprite):
        if self.stash.consume_mana_potion():
            constants.globals.action_cooldown = 0
            MANA_POTION.consume(self, text_sprite)
            self.sound_master.play_item_fx_sound('health_potion')
            return True

        self.no_action_error(MANA_POTION.name, text_sprite)
        return False

    def no_action_error(self, name, text_sprite):
        damage_text.warning(self, f' No {name} !', text_sprite)
        self.sound_master.play_item_fx_sound('error')

    def gain_experience(self):
        self.experience = self.experience + self.experience_to_gain
        self.experience_to_gain = 0
        if self.experience >= self.exp_level_break:
            self.level_up()

    def level_up(self):
        strength_raise = randint(2, 3)
        dexterity_raise = randint(1, 2)
        magic_raise = randint(1, 3)
        vitality_raise = randint(2, 4)
        resilience_raise = randint(1, 2)
        luck_raise = randint(1, 2)

        self.level_up_stats(strength_raise, dexterity_raise, magic_raise, vitality_raise, resilience_raise, luck_raise)

        self.previous_exp = self.experience
        self.experience = self.previous_exp - self.exp_level_break

        self.exp_level_break = round(self.exp_level_break * 1.3)

        self.level += 1
