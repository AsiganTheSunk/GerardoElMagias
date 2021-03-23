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
        BanditChief(500, 555, "BanditChief", 10, 190, 0, 17, 3, 0, 490, (screen_height - panel_height + 40), animation_master),
        Djinn(550, 500, "Djinn", 14, 214, 30, 0, 0, 10, 490, (screen_height - panel_height + 40), animation_master),
        SmallDragon(630, 510, "SmallDragon", 18, 244, 50, 18, 7, 12, 490, (screen_height - panel_height + 40), animation_master),
        Dragon(600, 425, "Dragon", 22, 325, 62, 20, 8, 22, 490, (screen_height - panel_height + 40), animation_master),
        Demon(500, 440, "Demon", 26, 335, 50, 31, 12, 18, 490, (screen_height - panel_height + 40), animation_master),
        Demon(500, 555, "Demon", 30, 514, 100, 41, 25, 25, 490, (screen_height - panel_height + 40), animation_master)
    ]
    return bosses[boss_level]



#tmp.append(Bandit(500, 555, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))
#tmp.append(Bandit(550, 610, "Bandit", 2, 43, 50, 7, 1, 10, 490, (screen_height - panel_height + 100)))