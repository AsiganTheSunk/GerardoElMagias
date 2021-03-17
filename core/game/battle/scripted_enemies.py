from core.units.classes.melee_bandit import Bandit
from core.units.classes.melee_boss import Boss
from core.units.classes.dragon import Dragon
from core.units.classes.lizard import Lizard
from core.units.classes.djinn import Djinn
from constants.game_windows import *
from core.units.enemy_group import EnemyGroup
enemy_group = EnemyGroup()

def scripted_enemy(boss_level):
    bosses = [
        None,
        Boss(500, 555, "The Boss", 10, 190, 50, 17, 3, 10, 490, (screen_height - bottom_panel + 40)),
        Dragon(500, 575, "Dragon", 14, 214, 50, 20, 5, 11, 490, (screen_height - bottom_panel + 40)),
        Dragon(500, 555, "Dragon", 18, 244, 50, 24, 7, 12, 490, (screen_height - bottom_panel + 40)),
        Boss(500, 555, "The Boss", 22, 287, 50, 28, 9, 13, 490, (screen_height - bottom_panel + 40)),
        Boss(500, 555, "The Boss", 26, 305, 50, 31, 11, 14, 490, (screen_height - bottom_panel + 40)),
        Boss(500, 555, "The Boss", 30, 514, 50, 40, 15, 15, 490, (screen_height - bottom_panel + 40))
    ]
    return bosses[boss_level]
