#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.skills.db.melee import MeleeSpells
from core.units.enemy_unit import EnemyUnit
from core.units.player.resources.stash import Stash
from core.game.text.damage_text import DamageText
from core.items.consumable.db.consumable_db import HEALTH_POTION
import constants.globals

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()


class BanditChief(EnemyUnit, MeleeSpells):
    def __init__(self, level, attack_power, attack_rating, magic_power, max_hp, max_mp, sound_master):
        EnemyUnit.__init__(self, 'BanditChief', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)

        self.animation_set = None
        self.animation_callbacks = None
        self.stash = Stash(healing_potions=round(self.level / 5), mana_potions=0, gold=0)

    def set_animations(self, animation_set, animation_callbacks):
        self.animation_set = animation_set
        self.animation_callbacks = animation_callbacks

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_healing_potion(self, text_sprite):
        constants.globals.action_cooldown = 0
        if self.stash.consume_healing_potion():
            HEALTH_POTION.consume(self, text_sprite)
            self.sound_master.play_item_fx_sound('health_potion')
            return True

        damage_text.warning(self, 'No Healing Potions', text_sprite)
        return False

    def action(self, target, text_sprite):
        health_trigger = self.current_hp <= round(self.max_hp * 0.4)
        if self.stash.has_healing_potion() and health_trigger:
            self.use_healing_potion(text_sprite)
        elif not self.stash.has_healing_potion() and self.has_tried_to_consume_health_potion() and health_trigger:
            self.use_healing_potion(text_sprite)
            self.update_try_to_consume_health_potion()
        else:
            self.use_attack(target, text_sprite)
