from core.units.classes.melee_bandit import Bandit
from core.units.classes.melee_boss import Boss
from core.units.classes.dragon import Dragon
from core.units.classes.lizard import Lizard
from core.units.classes.djinn import Djinn
from constants.game_windows import *


def scripted_enemy(boss_level, animation_master):
    bosses = [
        None,
        Boss(500, 555, "The Boss", 10, 190, 50, 17, 3, 10, 490, (screen_height - panel_height + 40), animation_master),
        Djinn(500, 575, "Djinn", 14, 214, 50, 20, 5, 11, 490, (screen_height - panel_height + 40), animation_master),
        Dragon(500, 555, "Dragon", 18, 244, 50, 24, 7, 12, 490, (screen_height - panel_height + 40), animation_master),
        Lizard(500, 555, "Lizard", 22, 287, 50, 28, 9, 13, 490, (screen_height - panel_height + 40), animation_master),
        Boss(500, 555, "The Boss", 26, 305, 50, 31, 11, 14, 490, (screen_height - panel_height + 40), animation_master),
        Boss(500, 555, "The Boss", 30, 514, 50, 40, 15, 15, 490, (screen_height - panel_height + 40), animation_master)
    ]
    return bosses[boss_level]



#tmp.append(Bandit(500, 555, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))
#tmp.append(Bandit(550, 610, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))