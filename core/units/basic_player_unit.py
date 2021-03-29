#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicPlayerUnit:
    def __init__(self, x, y, name, level, strength, dexterity, magic, vitality, resilience, luck):

        # Basic Unit Coordinates x,y
        self.x = x
        self.y = y

        # Basic Unit Name
        self.name = name

        # Basic Unit Stats
        self.level = level

        # Basic Attribute Stats: Strength, Dexterity, Vitality, Magic, Resilience, Luck
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic

        self.vitality = vitality
        self.resilience = resilience
        self.luck = luck

