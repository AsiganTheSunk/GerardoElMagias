#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicEnemyUnit:
    def __init__(self, x, y, name, level, attack_power, attack_rating, magic_power):

        # Basic Unit Coordinates x,y
        self.x = x
        self.y = y

        # Basic Unit Name
        self.name = name

        # Basic Unit Stats
        self.level = level

        # Basic Attribute Stats: AttackRating AttackPower MagicPower
        self.attack_rating = attack_rating
        self.attack_power = attack_power
        self.magic_power = magic_power
