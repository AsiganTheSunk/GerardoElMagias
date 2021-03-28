#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from core.units.constants.unit_type import UnitType


class EnemySetGenerator:
    @staticmethod
    def generate_set(group_size, enemy_pool):
        # enemy_pool = [EnemyType.BANDIT]
        tmp = []
        for i in range(group_size):
            tmp.append(choice(enemy_pool))
        return tmp

    def get_enemy_set(self, boss_level, group_size):
        if boss_level > 3:
            return self.generate_set(group_size, [UnitType.LIZARD, UnitType.BONE_WIZARD])
        elif boss_level > 1:
            return self.generate_set(group_size, [UnitType.BONE_WIZARD, UnitType.BONE_WIZARD])
        else:
            return self.generate_set(group_size, [UnitType.BANDIT, UnitType.BANDIT])
