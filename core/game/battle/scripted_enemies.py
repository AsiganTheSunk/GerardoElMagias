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
        BanditChief(650, 475, "BanditChief", 10, 190, 0, 17, 3, 0, 680, (screen_height - panel_height + 40), animation_master),
        Djinn(750, 400, "Djinn", 14, 214, 30, 0, 0, 10, 680, (screen_height - panel_height + 40), animation_master),
        SmallDragon(730, 435, "SmallDragon", 18, 244, 50, 18, 7, 12, 680, (screen_height - panel_height + 40), animation_master),
        Dragon(800, 350, "Dragon", 22, 325, 62, 20, 8, 22, 680, (screen_height - panel_height + 40), animation_master),
        Demon(800, 365, "Demon", 26, 335, 50, 31, 12, 18, 680, (screen_height - panel_height + 40), animation_master),
        Demon(600, 365, "Demon", 30, 514, 100, 41, 25, 25, 680, (screen_height - panel_height + 40), animation_master)
    ]
    return bosses[boss_level]



#tmp.append(Bandit(500, 555, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))
#tmp.append(Bandit(550, 610, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))