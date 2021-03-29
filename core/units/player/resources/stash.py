#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stash:
    def __init__(self, healing_potions=2, mana_potions=1, gold=0):
        self.healing_potions = healing_potions
        self.mana_potions = mana_potions
        self.gold = gold

    def has_healing_potion(self):
        return self.healing_potions > 0

    def has_mana_potion(self):
        return self.mana_potions > 0

    def has_enough_gold(self, gold_value):
        return self.gold >= gold_value

    def add_gold(self, gold_value):
        self.gold += gold_value

    def add_healing_potion(self, number_of_potions):
        self.healing_potions += number_of_potions

    def add_mana_potion(self, number_of_potions):
        self.mana_potions += number_of_potions

    def consume_healing_potion(self):
        if self.has_healing_potion():
            self.healing_potions -= 1
            return True
        return False

    def consume_mana_potion(self):
        if self.has_mana_potion():
            self.mana_potions -= 1
            return True
        return False

    def consume_gold(self, gold_value):
        if self.has_enough_gold(gold_value):
            self.gold -= gold_value
            return True
        return False
