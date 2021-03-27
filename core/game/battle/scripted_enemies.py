#!/usr/bin/env python
# -*- coding: utf-8 -*-

from units.enemy.bandit.bandit_chief import BanditChief
from units.enemy.dragon.small_dragon import SmallDragon
from core.units.enemy.dragon import Dragon
from core.units.enemy.djinn import Djinn
from core.units.enemy.demon import Demon
from constants.game_windows import screen_height, panel_height


def create_enemy(enemy, max_hp, max_mp):
    enemy.set_max_hp(max_hp)
    enemy.set_max_mp(max_mp)
    return enemy


def scripted_enemy(boss_level, animation_master):
    bosses = [
        None,
        create_enemy(BanditChief(650, 475, 10, 17, 10, 0,
                                 680, (screen_height - panel_height + 40), animation_master), 214, 0),
        create_enemy(Djinn(750, 400, 14, 0, 25, 20,
                           680, (screen_height - panel_height + 40), animation_master), 278, 40),
        create_enemy(SmallDragon(730, 438, 18, 18, 7, 12,
                                 680, (screen_height - panel_height + 40), animation_master), 332, 50),
        create_enemy(Dragon(800, 352, 22, 20, 8, 22,
                            680, (screen_height - panel_height + 40), animation_master), 400, 70),
        create_enemy(Demon(800, 365, 26, 31, 12, 18,
                           680, (screen_height - panel_height + 40), animation_master), 480, 50),
        create_enemy(Demon(600, 365, 30, 41, 25, 25,
                           680, (screen_height - panel_height + 40), animation_master), 666, 80),
    ]
    return bosses[boss_level]
