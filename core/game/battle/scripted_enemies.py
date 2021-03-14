from core.units.classes.melee_boss import Boss
from core.units.classes.dragon import Dragon
from core.units.classes.lizard import Lizard
from constants.game_windows import *


def scripted_enemy(boss_level):
    tmp = []
    if boss_level == 1:
        tmp.append(Boss(500, 555, "The Boss", 10, 190, 50, 17, 3, 10, 490, (screen_height - panel_height + 40)))
    elif boss_level == 2:
        tmp.append(Dragon(500, 575, "Dragon", 14, 214, 50, 20, 5, 11, 490, (screen_height - panel_height + 40)))
    elif boss_level == 3:
        tmp.append(Dragon(500, 555, "Dragon", 18, 244, 50, 24, 7, 12, 490, (screen_height - panel_height + 40)))
    elif boss_level == 4:
        tmp.append(Boss(500, 555, "The Boss", 22, 287, 50, 28, 9, 13, 490, (screen_height - panel_height + 40)))
    elif boss_level == 5:
        tmp.append(Boss(500, 555, "The Boss", 26, 305, 50, 31, 11, 14, 490, (screen_height - panel_height + 40)))
    elif boss_level == 6:
        tmp.append(Boss(500, 555, "The Boss", 30, 514, 50, 40, 15, 15, 490, (screen_height - panel_height + 40)))
    return tmp

