#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.basic_unit import BasicUnit


class PlayerUnit(BasicUnit):
    def __init__(self, x, y, name, level, strength, dexterity, magic, vitality, resilience, luck):
        BasicUnit.__init__(self, x, y, name, level, strength, dexterity, magic)

        self.vitality = vitality
        self.resilience = resilience
        self.luck = luck

        # Basic Resource Stats: Fury, Mana, Health
        self.max_hp = 1000
        # self.max_hp = self.vitality * 3
        self.current_hp = self.max_hp
        self.max_mp = self.magic * 2 + self.resilience
        self.current_mp = self.max_mp

        # Basic Unit Status
        self.ultimate_status = False
        self.whirlwind_status = False
        self.multi_attacks_left = 7

    def level_up_stats(self, strength_raise, dexterity_raise, magic_raise, vitality_raise, resilience_raise, luck_raise):
        self.strength += strength_raise
        self.dexterity += dexterity_raise
        self.magic += magic_raise
        self.vitality += vitality_raise
        self.resilience += resilience_raise
        self.luck += luck_raise

        # calculate max hp and max mp
        self.max_hp = self.vitality * 3
        self.current_hp = self.current_hp + vitality_raise * 3
        self.max_mp = self.magic * 2 + self.resilience
        self.current_mp = self.current_mp + magic_raise * 2 + resilience_raise
