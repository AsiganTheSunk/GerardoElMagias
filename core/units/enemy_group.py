from random import randint
from core.units.classes.melee_bandit import Bandit
from enum import Enum
from random import choice
from core.units.classes.bone_wizard import BoneWizard
from core.units.classes.lizard import Lizard
from constants.game_windows import *


class EnemySetGenerator:
    @staticmethod
    def generate_set(group_size, enemy_pool):
        # enemy_pool = [EnemyType.BANDIT]
        tmp = []
        for i in range(group_size):
            tmp.append(choice(enemy_pool))
        return tmp

    def get_enemy_set(self, boss_level, group_size):
        if boss_level <= 2:
            return self.generate_set(group_size, [UnitType.BANDIT, UnitType.BANDIT])
        elif boss_level >= 3:
            return self.generate_set(group_size, [UnitType.BONE_WIZARD, UnitType.BONE_WIZARD])


class UnitType(Enum):
    BANDIT = 'Bandit'
    THE_BOSS = 'The Boss'
    LIZARD = 'Lizard'
    DRAGON = 'Dragon'
    BONE_WIZARD = 'BoneWizard'
    HERO = 'Hero'
    DJINN = 'Djinn'


class EnemyStatsGenerator:
    @staticmethod
    def generate_bandit_stats(level):
        randomlevel = level + randint(0, 2)
        maxhp = randomlevel * 9
        maxmp = randomlevel * 4
        str = 8 + round(randomlevel / 2)
        dex = 6 + round(randomlevel / 2)
        mag = 1 + round(randomlevel / 2)
        return randomlevel, maxhp, maxmp, str, dex, mag

    @staticmethod
    def generate_lizard_stats(level):
        randomlevel = level + randint(0, 2)
        maxhp = randomlevel * 11
        maxmp = randomlevel * 4
        str = 5 + round(randomlevel / 2)
        dex = 1 + round(randomlevel / 2)
        mag = 5 + round(randomlevel / 2)
        return randomlevel, maxhp, maxmp, str, dex, mag

    @staticmethod
    def generate_bone_wizard_stats(level):
        randomlevel = level + randint(0, 3)
        maxhp = randomlevel * 6
        maxmp = randomlevel * 7
        str = 2 + round(randomlevel / 2)
        dex = 0 + round(randomlevel / 2)
        mag = 10 + randomlevel
        return randomlevel, maxhp, maxmp, str, dex, mag


class EnemyPositionsGenerator:
    @staticmethod
    def generate_forest_enemy_positions():
        return [(500, 555), (600, 600), (700, 555), (800, 600)]

    @staticmethod
    def generate_castle_enemy_positions():
        return [(500, 570), (700, 570), (600, 500), (800, 500)]

    def get_enemy_positions(self, boss_level):
        if boss_level <= 2:
            return self.generate_forest_enemy_positions()
        elif boss_level >= 3:
            return self.generate_castle_enemy_positions()


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
            return randint(1, 3)
        elif 7 <= level < 10:
            return randint(1, 4)
        elif 10 <= level < 14:
            return randint(2, 4)
        elif 14 <= level < 18:
            return randint(3, 4)
        elif level >= 18:
            return 4

    @staticmethod
    def get_enemy_healthbar_positions():
        return [
            (480, screen_height - panel_height + 40),
            (480, screen_height - panel_height + 100),
            (700, screen_height - panel_height + 40),
            (700, screen_height - panel_height + 100)
        ]

    def get_enemy (self, enemy_type, level, enemy_pos_x, enemy_pos_y, enemy_healthbar_x, enemy_healthbar_y):
        if enemy_type is UnitType.BANDIT:
            _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_bandit_stats(level)
            return Bandit(enemy_pos_x, enemy_pos_y, enemy_type.value, _randomlevel,  _maxhp, _maxmp, _str, _dex, _mag,
                          enemy_healthbar_x, enemy_healthbar_y, self.animation_master)

        elif enemy_type is UnitType.LIZARD:
            _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_lizard_stats(level)
            return Lizard(enemy_pos_x, enemy_pos_y, enemy_type.value, _randomlevel, _maxhp, _maxmp, _str, _dex, _mag,
                          enemy_healthbar_x, enemy_healthbar_y, self.animation_master)

        elif enemy_type is UnitType.BONE_WIZARD:
            _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_bone_wizard_stats(level)
            return BoneWizard(enemy_pos_x, enemy_pos_y, enemy_type.value, _randomlevel, _maxhp, _maxmp, _str, _dex,
                              _mag, enemy_healthbar_x, enemy_healthbar_y, self.animation_master)

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











