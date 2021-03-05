from constants.game_windows import *
from random import randint
from units.unit_type.bandit.bandit_melee_figher import Bandit


class EnemyGroup:
    def __init__(self):
        self.FST_COLUMN = 480
        self.SND_COLUMN = 700

    @staticmethod
    def generate_enemy_stats(level):
        randomlevel = level + randint(0, 2)
        maxhp = randomlevel * 12
        maxmp = randomlevel * 5
        str = 8 + randomlevel
        dex = 7 + randomlevel
        mag = 5 + randomlevel
        return randomlevel, maxhp, maxmp, str, dex, mag

    def generate_enemy(self, level):
        group_size = 0
        if level < 4:
            group_size = randint(1, 2)
        elif 4 <= level < 7:
            group_size = randint(1, 3)
        elif 7 <= level < 10:
            group_size = randint(1, 4)
        elif 10 <= level < 14:
            group_size = randint(2, 4)
        elif 14 <= level < 18:
            group_size = randint(3, 4)
        elif level >= 18:
            group_size = 4

        tmp = []
        ENEMY_POS_0 = [self.FST_COLUMN, screen_height - bottom_panel + 40]
        ENEMY_POS_1 = [self.FST_COLUMN, screen_height - bottom_panel + 100]
        ENEMY_POS_2 = [self.SND_COLUMN, screen_height - bottom_panel + 40]
        ENEMY_POS_3 = [self.SND_COLUMN, screen_height - bottom_panel + 100]

        for index in range(group_size):
            if index == 0:
                _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_enemy_stats(level)
                tmp.append(Bandit(500, 555, f"Enemy", _randomlevel,  _maxhp, _maxmp, _str, _dex, _mag, ENEMY_POS_0[0], ENEMY_POS_0[1]))
            elif index == 1:
                _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_enemy_stats(level)
                tmp.append(Bandit(600, 600, f"Enemy", _randomlevel, _maxhp, _maxmp, _str, _dex, _mag, ENEMY_POS_1[0], ENEMY_POS_1[1]))
            elif index == 2:
                _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_enemy_stats(level)
                tmp.append(Bandit(700, 555, f"Enemy", _randomlevel, _maxhp, _maxmp, _str, _dex, _mag, ENEMY_POS_2[0], ENEMY_POS_2[1]))
            elif index == 3:
                _randomlevel, _maxhp, _maxmp, _str, _dex, _mag = self.generate_enemy_stats(level)
                tmp.append(Bandit(800, 600, f"Enemy", _randomlevel, _maxhp, _maxmp, _str, _dex, _mag, ENEMY_POS_3[0], ENEMY_POS_3[1]))

        return tmp
