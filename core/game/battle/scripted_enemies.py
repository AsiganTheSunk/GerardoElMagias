from core.units.classes.melee_bandit import Bandit
from core.units.classes.banditchief import BanditChief
from core.units.classes.dragon import Dragon
from core.units.classes.lizard import Lizard
from core.units.classes.djinn import Djinn
from constants.game_windows import *


def scripted_enemy(boss_level, animation_master):
    bosses = [
        None,
        BanditChief(500, 555, "BanditChief", 10, 190, 50, 17, 3, 10, 490, (screen_height - panel_height + 40), animation_master),
        Djinn(550, 500, "Djinn", 14, 214, 50, 20, 5, 11, 490, (screen_height - panel_height + 40), animation_master),
        Dragon(630, 510, "Dragon", 18, 244, 50, 20, 7, 12, 490, (screen_height - panel_height + 40), animation_master),
        Lizard(500, 555, "Lizard", 22, 287, 50, 22, 9, 13, 490, (screen_height - panel_height + 40), animation_master),
        BanditChief(500, 555, "BanditChief", 26, 305, 50, 31, 11, 14, 490, (screen_height - panel_height + 40), animation_master),
        BanditChief(500, 555, "BanditChief", 30, 514, 50, 40, 15, 15, 490, (screen_height - panel_height + 40), animation_master)
    ]
    return bosses[boss_level]



#tmp.append(Bandit(500, 555, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))
#tmp.append(Bandit(550, 610, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))