#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
from core.game.text.damage_text import DamageText

# Skill Imports
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells

# Animation Imports
from core.game.animations.sets.unit_animation_set import UnitAnimationSet
from random import randint
import constants.globals
from constants.game_sound import error_sound

damage_text = DamageText()


class Demon(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, level, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master):
        EnemyUnit.__init__(self, x, y, 'Demon', level, strength, dexterity, magic)
        MeleeSpells.__init__(self)
        MagicSpells.__init__(self)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'Demon', animation_master.get_unit_resource_animation_set('Demon'))

        self.fury_status = True
        self.animation_set.action = 6

    def attack(self, target, text_sprite):
        self.melee_attack_animation()
        self.cast_attack(self, target, text_sprite)
        return True

    def use_heal(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, text_sprite)
            return True
        return False

    def use_firestorm(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):
            constants.globals.action_cooldown = -30
            self.cast_firestorm(self, target_list, text_sprite)
            return True
        return False

    def use_lightning(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(20):
            constants.globals.action_cooldown = -30
            self.cast_lightning(self, target_list, text_sprite)
            return True
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

    def materialize_animation(self):
        # Activates: Miss Animation
        self.animation_set.action = 6
        self.animation_set.reset_frame_index()

    def no_action_error(self, name, text_sprite):
        damage_text.warning(self, f' No {name} !', text_sprite)
        error_sound.play()

    def action(self, target, text_sprite):
        health_trigger = self.current_hp <= round(self.max_hp * 0.90)
        if health_trigger:
            random_action = randint(1, 4)
            if random_action == 1:
                self.attack(target, text_sprite)
            elif random_action == 2:
                if self.use_heal(text_sprite):
                    pass
                else:
                    self.attack(target, text_sprite)
            elif random_action == 3:
                if self.use_firestorm([target], text_sprite):
                    pass
                else:
                    self.attack(target, text_sprite)
            elif random_action == 4:
                if self.use_lightning([target], text_sprite):
                    pass
                else:
                    self.attack(target, text_sprite)
        else:
            self.attack(target, text_sprite)
