#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


class EnemyStatsGenerator:
    @staticmethod
    def generate_bandit_stats(level):
        randomlevel = level + randint(0, 2)
        str = 3 + round(randomlevel / 2)
        dex = 6 + randomlevel
        max_hp = 10 + randomlevel*7
        max_mp = 0
        mag = 0

        return randomlevel, str, dex, mag, max_hp, max_mp

    @staticmethod
    def generate_bone_wizard_stats(level):
        randomlevel = level + randint(0, 3)
        str = round(randomlevel / 2)
        dex = 1 + randomlevel
        max_hp = 30 + randomlevel * 4
        max_mp = 25 + randomlevel * 5
        mag = 10 + randomlevel

        return randomlevel, str, dex, mag, max_hp, max_mp

    @staticmethod
    def generate_lizard_stats(level):
        randomlevel = level + randint(0, 3)
        str = 4 + round(randomlevel / 2)
        dex = 8 + randomlevel
        max_hp = 50 + randomlevel * 7
        max_mp = 0
        mag = 0

        return randomlevel, str, dex, mag, max_hp, max_mp
