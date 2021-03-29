#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


class EnemyStatsGenerator:
    @staticmethod
    def generate_bandit_stats(level):
        random_level = level + randint(0, 2)
        strength = 3 + round(random_level / 2)
        dexterity = 6 + random_level
        magic = 0
        max_hp = 10 + random_level * 7
        max_mp = 0

        return random_level, strength, dexterity, magic, max_hp, max_mp

    @staticmethod
    def generate_bone_wizard_stats(level):
        random_level = level + randint(0, 3)
        strength = round(random_level / 2)
        dexterity = 1 + random_level
        magic = 10 + random_level
        max_hp = 30 + random_level * 4
        max_mp = 25 + random_level * 5

        return random_level, strength, dexterity, magic, max_hp, max_mp

    @staticmethod
    def generate_lizard_stats(level):
        random_level = level + randint(0, 3)
        strength = 4 + round(random_level / 2)
        dexterity = 8 + random_level
        magic = 0
        max_hp = 50 + random_level * 7
        max_mp = 0

        return random_level, strength, dexterity, magic, max_hp, max_mp
