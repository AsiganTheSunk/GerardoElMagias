#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


class EnemyStatsGenerator:
    @staticmethod
    def generate_bandit_stats(level):
        random_level = level + randint(0, 2)
        attack_power = 3 + round(random_level / 2)
        attack_rating = 6 + random_level
        magic_power = 0
        max_hp = 10 + random_level * 7
        max_mp = 0

        return random_level, attack_power, attack_rating, magic_power, max_hp, max_mp

    @staticmethod
    def generate_bone_wizard_stats(level):
        random_level = level + randint(0, 3)
        attack_power = round(random_level / 2)
        attack_rating = 1 + random_level
        magic_power = 8 + random_level
        max_hp = 30 + random_level * 4
        max_mp = 25 + random_level * 5

        return random_level, attack_power, attack_rating, magic_power, max_hp, max_mp

    @staticmethod
    def generate_lizard_stats(level):
        random_level = level + randint(0, 4)
        attack_power = 4 + round(random_level / 2)
        attack_rating = 8 + random_level
        magic_power = 0
        max_hp = 40 + random_level * 8
        max_mp = 0

        return random_level, attack_power, attack_rating, magic_power, max_hp, max_mp
