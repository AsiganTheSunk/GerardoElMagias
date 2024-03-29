#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicUnit:
    def __init__(self):
        # Basic Resource Stats: Fury, Mana, Health
        self.max_fury = 100
        self.current_fury = 0
        self.max_hp = 0
        self.current_hp = 0
        self.max_mp = 0
        self.current_mp = 0

        # Basic Unit Status
        self.alive = True
        self.fury_status = False
        self.experience_status = False

        self.next_action = None

    def set_max_hp(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp

    def set_max_mp(self, max_mp):
        self.max_mp = max_mp
        self.current_mp = max_mp

    def reduce_fury(self, input_fury):
        if self.current_fury - input_fury < 0:
            self.current_fury = 0
        else:
            self.current_fury -= input_fury

    def reduce_health(self, input_health):
        if self.current_hp - input_health < 0:
            self.current_hp = 0
        else:
            self.current_hp -= input_health

    def reduce_mana(self, input_mana):
        if self.has_enough_mana(input_mana):
            # Consume Mana: Spell Casting
            self.current_mp -= input_mana
            return True
        return False

    def has_experience(self):
        return self.experience_status

    def has_enough_mana(self, input_mana):
        return self.current_mp >= input_mana

    def has_enough_fury(self, input_fury=100):
        return self.current_fury >= input_fury

    def has_fury(self):
        return self.fury_status

    def reset_fury(self):
        self.current_fury = 0

    def gain_health(self, input_health):
        if self.current_hp + input_health >= self.max_hp:
            gained_health = self.max_hp - self.current_hp
            self.current_hp = self.max_hp
            return gained_health

        self.current_hp += input_health
        return input_health

    def gain_mana(self, input_mana):
        if self.current_mp + input_mana >= self.max_mp:
            gained_mana = self.max_mp - self.current_mp
            self.current_mp = self.max_mp
            return gained_mana

        self.current_mp += input_mana
        return input_mana

    def gain_fury(self, input_damage):
        fury_amount = round(input_damage * 1.5 * 100 / self.max_hp)
        if self.current_fury + fury_amount >= self.max_fury:
            self.current_fury = self.max_fury
            gained_fury = self.max_fury - self.current_fury
            return gained_fury
        else:
            self.current_fury += fury_amount
            return fury_amount

    def is_dead(self):
        return self.current_hp < 1

    def death(self):
        self.current_hp = 0
        self.alive = False

    def run_next_action(self, text_sprite):
        if self.next_action and \
                self.next_action[0] == 'attack':
            target = self.next_action[1]

            self.use_attack(target, text_sprite)
        if self.next_action and \
                self.next_action[0] == 'use' \
                and self.next_action[1] == 'healing_potion':

            self.use_healing_potion(text_sprite)
        if self.next_action and \
                self.next_action[0] == 'use' and \
                self.next_action[1] == 'mana_potion':
            self.use_mana_potion(text_sprite)
