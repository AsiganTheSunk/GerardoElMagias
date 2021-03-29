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

damage_text = DamageText()


class Demon(EnemyUnit, MeleeSpells, MagicSpells):
    def __init__(self, x, y, level, strength, dexterity, magic, health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'Demon', level, strength, dexterity, magic)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'Demon', animation_master.get_unit_animation_set('Demon'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('Demon')

        self.fury_status = True
        self.animation_set.action = 6

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_heal(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, text_sprite)
            self.sound_master.play_spell_fx_sound('heal_spell')
            return True
        return False

    def use_firestorm(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):
            constants.globals.action_cooldown = -30
            self.cast_firestorm(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('firestorm_spell')
            return True
        return False

    def use_lightning(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(20):
            constants.globals.action_cooldown = -30
            self.cast_lightning(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('lightning_spell')
            return True
        return False

    def action(self, target, text_sprite):
        health_trigger = self.current_hp <= round(self.max_hp * 0.90)
        if health_trigger:
            random_action = randint(1, 4)
            if random_action == 1:
                self.use_attack(target, text_sprite)
            elif random_action == 2:
                if self.use_heal(text_sprite):
                    pass
                else:
                    self.use_attack(target, text_sprite)
            elif random_action == 3:
                if self.use_firestorm([target], text_sprite):
                    pass
                else:
                    self.use_attack(target, text_sprite)
            elif random_action == 4:
                if self.use_lightning([target], text_sprite):
                    pass
                else:
                    self.use_attack(target, text_sprite)
        else:
            self.use_attack(target, text_sprite)
