#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.skills.melee import MeleeSpells
from core.units.basic_unit import BasicUnit
from core.units.resources.health_bar import HealthBar
from core.units.resources.stash import Stash
from random import randint
from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText
from constants.sound import *
from core.units.animations.sets.unit_animation_set import UnitAnimationSet
import constants.globals



# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class Bandit(BasicUnit, MeleeSpells):
    def __init__(self, x, y, name, level, strength, dexterity, vitality, magic, resilience, luck, health_bar_x, health_bar_y,
                 animation_master):
        BasicUnit.__init__(self, x, y, name, level, strength, dexterity, vitality, magic, resilience, luck)
        MeleeSpells.__init__(self)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        # Bandit Loot
        self.looted_status = False
        self.animation_set = UnitAnimationSet(animation_master.surface, x, y, name, animation_master.get_unit_resource_animation_set('Bandit'))
        self.stash = Stash(healing_potions=1, mana_potions=0, gold=0)
        self.try_to_consume_health_potion = False

    def is_looted(self):
        return self.looted_status

    def update_looted_status(self):
        self.looted_status = True

    def attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_attack(self, target, damage_text_group)
        return True

    def use_healing_potion(self, damage_text_group):
        constants.globals.action_cooldown = 0
        if self.stash.has_healing_potion():
            # Activates potion sound
            health_potion_sound.play()

            base_health = 40
            health_interval = randint(0, 10)
            base_health_multiplier = (self.level * 4)
            health_recover = base_health + health_interval + base_health_multiplier

            self.stash.consume_healing_potion()
            self.gain_health(health_recover)

            damage_text.heal(self, str(health_recover), damage_text_group)
            return True

        damage_text.warning(self, 'No Healing Potions', damage_text_group)
        return False

    def strong_attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_strong_attack(self, target, damage_text_group)
        return True

    def update_try_to_consume_health_potion(self):
        self.try_to_consume_health_potion = True

    def has_tried_to_consume_health_potion(self):
        return self.try_to_consume_health_potion is False

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
        health_trigger = self.current_hp <= round(self.max_hp * 0.15)
        if self.stash.has_healing_potion() and health_trigger:
            self.use_healing_potion(damage_text_group)
        elif not self.stash.has_healing_potion() and self.has_tried_to_consume_health_potion() and health_trigger:
            self.use_healing_potion(damage_text_group)
            self.update_try_to_consume_health_potion()
        else:
            # Attack
            self.attack(target, damage_text_group)