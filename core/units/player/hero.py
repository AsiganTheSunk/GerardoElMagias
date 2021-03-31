#!/usr/bin/env python
# -*- coding: utf-8 -*-


from core.units.player.resources.stash import Stash
from core.skills.db.magic import MagicSpells
from core.skills.db.melee import MeleeSpells
from core.skills.db.fury import FurySpells
from core.game.mechanics.experience_master import ExperienceMaster
from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText
import constants.globals
from core.game.mechanics.loot_master import LootMaster
from core.units.player_unit import PlayerUnit
from core.units.player.resources.backpack import BackPack


# Consumable Items
from core.items.consumable.db.consumable_db import HEALTH_POTION, MANA_POTION
import constants.globals

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class HeroPlayer(PlayerUnit, ExperienceMaster, MeleeSpells, MagicSpells, FurySpells):
    def __init__(self, level, strength, dexterity, magic, vitality, resilience, luck, sound_master):
        PlayerUnit.__init__(self, "Hero", level, strength, dexterity, magic, vitality, resilience, luck)
        FurySpells.__init__(self, sound_master)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)
        ExperienceMaster.__init__(self, self)

        self.animation_set = None
        self.animation_callbacks = None

        self.fury_status = True
        self.loot_pool = LootMaster(self.sound_master)

        self.stash = Stash()
        self.backpack = BackPack()

    def set_animations(self, animation_set, animation_callbacks):
        self.animation_set = animation_set
        self.animation_callbacks = animation_callbacks

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def get_loot(self, target, text_sprite):
        self.loot_pool.loot(self, target, text_sprite)

    def use_attack(self, target, text_sprite):
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
            self.cast_firestorm(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('firestorm_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_lightning_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(16):
            constants.globals.action_cooldown = -30
            self.cast_lightning(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('lightning_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_earth_shock_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(14):
            constants.globals.action_cooldown = -40
            self.cast_earth_shock(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('earth_shock_spell')
            return True

        self.no_action_error('Mana', text_sprite)
        return False

    def use_water_nova_spell(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(18):
            constants.globals.action_cooldown = -50
            self.cast_water_nova(self, target_list, text_sprite)
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
