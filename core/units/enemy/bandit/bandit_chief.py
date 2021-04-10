#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.skills.db.melee import MeleeSpells
from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
from core.units.player.resources.stash import Stash
from core.game.text.damage_text import DamageText
from core.items.consumable.db.consumable_db import HEALTH_POTION

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet
import constants.globals

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()


class BanditChief(EnemyUnit, MeleeSpells):
    def __init__(self, x, y, level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                 health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'BanditChief', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'BanditChief', animation_master.get_unit_animation_set('BanditChief'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('BanditChief')

        self.stash = Stash(healing_potions=round(self.level / 5), mana_potions=0, gold=0)

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
        if health_trigger and self.stash.has_healing_potion():
            self.use_healing_potion(text_sprite)
        elif not self.stash.has_healing_potion() and self.has_tried_to_consume_health_potion() and health_trigger:
            self.use_healing_potion(text_sprite)
            self.update_try_to_consume_health_potion()
        else:
            self.use_attack(target, text_sprite)
