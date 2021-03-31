#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.skills.db.melee import MeleeSpells
from core.skills.db.magic import MagicSpells
from core.units.enemy_unit import EnemyUnit


class SmallDragon(EnemyUnit, MagicSpells, MeleeSpells):
    def __init__(self, level, attack_power, attack_rating, magic_power, max_hp, max_mp, sound_master):
        EnemyUnit.__init__(self, 'SmallDragon', level, attack_power, attack_rating, magic_power, max_hp, max_mp)
        MeleeSpells.__init__(self, sound_master)
        MagicSpells.__init__(self, sound_master)

        self.sound_master = sound_master
        self.animation_set = None
        self.animation_callbacks = None

    def set_animations(self, animation_set, animation_callbacks):
        self.animation_set = animation_set
        self.animation_callbacks = animation_callbacks

    def use_animation(self, animation):
        self.animation_callbacks[animation](self.animation_set)

    def use_attack(self, target, text_sprite):
        self.use_animation('Attack')
        self.cast_attack(self, target, text_sprite)
        return True

    def use_heal(self, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            self.cast_heal(self, self, text_sprite)
            self.sound_master.play_spell_fx_sound('heal_spell')
            return True
        return False

    def use_firestorm(self, target_list, text_sprite):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):
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
                if self.use_heal(text_sprite):
                    pass
                else:
                    self.use_attack(target, text_sprite)
            elif random_action == 3:
                if self.use_firestorm([target], text_sprite):
                    pass
                else:
                    self.use_attack(target, text_sprite)
        else:
            self.use_attack(target, text_sprite)
