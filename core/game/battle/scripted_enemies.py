#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.classes.melee_bandit import Bandit
from core.units.classes.banditchief import BanditChief
from core.units.classes.smalldragon import SmallDragon
from core.units.classes.dragon import Dragon
from core.units.classes.lizard import Lizard
from core.units.classes.djinn import Djinn
from core.units.classes.demon import Demon
from constants.game_windows import *


def scripted_enemy(boss_level, animation_master):
    bosses = [
        None,
        BanditChief(650, 475, "BanditChief", 10, 17, 10, 20, 0, 1, 0, 680, (screen_height - panel_height + 40), animation_master),
        Djinn(750, 400, "Djinn", 14, 0, 25, 10, 20, 1, 0, 680, (screen_height - panel_height + 40), animation_master),
        SmallDragon(730, 438, "SmallDragon", 18, 18, 7, 30, 12, 1, 0, 680, (screen_height - panel_height + 40), animation_master),
        Dragon(800, 352, "Dragon", 22, 20, 8, 30, 22, 680, 1, 0, (screen_height - panel_height + 40), animation_master),
        Demon(800, 365, "Demon", 26, 31, 12, 35, 18, 680, 1, 0, (screen_height - panel_height + 40), animation_master),
        Demon(600, 365, "Demon", 30, 41, 25, 40, 25, 680, 1, 0, (screen_height - panel_height + 40), animation_master)
    ]
    return bosses[boss_level]

#def __init__(self, x, y, name, level, strength, dexterity, vitality, magic, resilience, luck, health_bar_x, health_bar_y,
#                 animation_master):


#tmp.append(Bandit(500, 555, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))
#tmp.append(Bandit(550, 610, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))