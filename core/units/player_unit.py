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
        self.max_hp = self.vitality * 3
        self.current_hp = self.max_hp
        self.max_mp = self.magic * 2 + self.resilience
        self.current_mp = self.max_mp

        # Basic Unit Status
        self.experience_status = True
        self.ultimate_status = False
        self.whirlwind_status = False
        self.multi_attacks_left = 7

