#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells
from core.units.enemy_unit import EnemyUnit
from core.units.resources.health_bar import HealthBar
from core.game.animations.sets.unit_animation_set import UnitAnimationSet


class SmallDragon(EnemyUnit, MagicSpells, MeleeSpells):
    def __init__(self, x, y, level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                 health_bar_x, health_bar_y, animation_master, sound_master):
        EnemyUnit.__init__(self, x, y, 'SmallDragon', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.sound_master = sound_master
        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y,
                             'SmallDragon', animation_master.get_unit_animation_set('SmallDragon'))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks('SmallDragon')

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_heal(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(25):
            self.cast_heal(self, self, text_sprite)
            self.sound_master.play_spell_fx_sound('heal_spell')
            return True
        return False

    def use_firestorm(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(32):
            self.cast_firestorm(self, target_list, text_sprite)
            self.sound_master.play_spell_fx_sound('firestorm_spell')
            return True
        return False

    def action(self, target, text_sprite):
        health_trigger = self.current_hp <= round(self.max_hp * 0.60)
        if health_trigger:
            random_action = randint(1, 3)

            if random_action == 1:
                self.use_attack(target, text_sprite)

            elif random_action == 2:
                if self.current_mp >= 25:
                    self.use_heal(text_sprite)
                else:
                    self.use_attack(target, text_sprite)

            elif random_action == 3:
                if self.current_mp >= 32:
                    self.use_firestorm([target], text_sprite)
                else:
                    self.use_attack(target, text_sprite)

        else:
            self.use_attack(target, text_sprite)
