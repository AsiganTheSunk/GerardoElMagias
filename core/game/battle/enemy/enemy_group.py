#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.units.enemy.bandit.bandit import Bandit
from units.enemy.bone.bone_wizard import BoneWizard
from core.units.enemy.lizard.lizard import Lizard
from constants.game_windows import *
from units.constants.unit_type import UnitType
from game.battle.enemy import EnemySetGenerator
from game.battle.enemy import EnemyStatsGenerator
from game.battle.enemy import EnemyPositionsGenerator


class EnemyGroup(EnemyStatsGenerator, EnemyPositionsGenerator, EnemySetGenerator):
    def __init__(self, animation_master):
        self.animation_master = animation_master
        EnemyStatsGenerator.__init__(self)
        EnemyPositionsGenerator.__init__(self)
        EnemySetGenerator.__init__(self)

    @staticmethod
    def generate_group_size(level):
        if level < 4:
           return randint(1, 2)
        elif 4 <= level < 7:
            return randint(2, 3)
        elif 7 <= level < 10:
            return randint(1, 3)
        elif 10 <= level < 14:
            return randint(2, 4)
        elif 14 <= level < 18:
            return randint(2, 4)
        elif level >= 18:
            return randint(3,4)

    @staticmethod
    def get_enemy_healthbar_positions():
        return [
            (680, screen_height - panel_height + 40),
            (680, screen_height - panel_height + 100),
            (900, screen_height - panel_height + 40),
            (900, screen_height - panel_height + 100)
        ]

    def get_enemy(self, enemy_type, level, enemy_pos_x, enemy_pos_y, enemy_healthbar_x, enemy_healthbar_y):
        if enemy_type is UnitType.BANDIT:
            randomlevel, str, dex, mag, max_hp, max_mp = self.generate_bandit_stats(level)
            return self.create_enemy(Bandit(enemy_pos_x, enemy_pos_y, randomlevel, str, dex, mag,
                                            enemy_healthbar_x, enemy_healthbar_y, self.animation_master), max_hp, max_mp)

        elif enemy_type is UnitType.LIZARD:
            randomlevel, str, dex, mag, max_hp, max_mp = self.generate_lizard_stats(level)
            return self.create_enemy(Lizard(enemy_pos_x, enemy_pos_y, randomlevel, str, dex, mag,
                                            enemy_healthbar_x, enemy_healthbar_y, self.animation_master), max_hp, max_mp)

        elif enemy_type is UnitType.BONE_WIZARD:
            randomlevel, str, dex, mag, max_hp, max_mp = self.generate_bone_wizard_stats(level)
            return self.create_enemy(BoneWizard(enemy_pos_x, enemy_pos_y, randomlevel, str, dex, mag,
                                                enemy_healthbar_x, enemy_healthbar_y, self.animation_master), max_hp, max_mp)

    @staticmethod
    def create_enemy(enemy, max_hp, max_mp):
        enemy.set_max_hp(max_hp)
        enemy.set_max_mp(max_mp)
        return enemy

    def generate_enemy(self, level, boss_level):
        enemy_group = []
        group_size = self.generate_group_size(level)
        enemy_set = self.get_enemy_set(boss_level, group_size)
        enemy_positions = self.get_enemy_positions(boss_level)
        enemy_healthbar_positions = self.get_enemy_healthbar_positions()
        for index in range(group_size):
            enemy_pos_x, enemy_pos_y = enemy_positions[index]
            enemy_healthbar_x, enemy_healthbar_y = enemy_healthbar_positions[index]
            current_enemy = self.get_enemy(enemy_set[index], level, enemy_pos_x, enemy_pos_y, enemy_healthbar_x, enemy_healthbar_y)
            enemy_group.append(current_enemy)

        return enemy_group
