#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.units.enemy.bandit.bandit import Bandit
from core.units.enemy.bone.bone_wizard import BoneWizard
from core.units.enemy.lizard.lizard import Lizard
from core.units.constants.unit_type import UnitType
from core.game.battle.enemy.set_generator import EnemySetGenerator
from core.game.battle.enemy.stats_generator import EnemyStatsGenerator
# from core.game.battle.enemy.position_generator import EnemyPositionsGenerator
from core.units.enemy.bandit.bandit_chief import BanditChief
from core.units.enemy.dragon.small_dragon import SmallDragon
from core.units.enemy.dragon.dragon import Dragon
from core.units.enemy.djinn.djinn import Djinn
from core.units.enemy.demon.demon import Demon
from core.units.enemy.medusa.medusa import Medusa


class EnemyGroupGenerator(EnemyStatsGenerator, EnemySetGenerator):
    def __init__(self, sound_master):
        EnemyStatsGenerator.__init__(self)
        EnemySetGenerator.__init__(self)

        self.sound_master = sound_master

    @staticmethod
    def generate_group_size(level):
        if level < 4:
            return randint(1, 2)
        elif 4 <= level < 7:
            return randint(2, 3)
        elif 7 <= level < 10:
            return randint(1, 3)
        elif 10 <= level < 14:
            return randint(2, 4)
        elif 14 <= level < 18:
            return randint(2, 4)
        elif level >= 18:
            return randint(3, 4)

    def get_enemy(self, enemy_type, level):
        if enemy_type is UnitType.BANDIT:
            random_level, attack_power, attack_rating, magic_power, max_hp, max_mp = self.generate_bandit_stats(level)
            return Bandit(random_level, attack_power, attack_rating, magic_power, max_hp, max_mp, self.sound_master)

        elif enemy_type is UnitType.LIZARD:
            random_level, attack_power, attack_rating, magic_power, max_hp, max_mp = self.generate_lizard_stats(level)
            return Lizard(random_level, attack_power, attack_rating, magic_power, max_hp, max_mp, self.sound_master)

        elif enemy_type is UnitType.BONE_WIZARD:
            random_level, attack_power, attack_rating, magic_power, max_hp, max_mp = self.generate_bone_wizard_stats(level)
            return BoneWizard(random_level, attack_power, attack_rating, magic_power, max_hp, max_mp, self.sound_master)

    def generate_enemy(self, level, boss_level):
        enemy_group = []
        group_size = self.generate_group_size(level)
        enemy_set = self.get_enemy_set(boss_level, group_size)
        for index in range(group_size):
            current_enemy = self.get_enemy(enemy_set[index], level)
            enemy_group.append(current_enemy)
        return enemy_group

    def scripted_enemy(self, boss_level, sound_master):
        bosses = [
            None,
            BanditChief(650, 475, 10, 17, 10, 0, 214, 0,
                        680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                        animation_master, sound_master),
            Djinn(750, 400, 14, 0, 25, 20, 278, 50,
                  680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                  animation_master, sound_master),
            SmallDragon(730, 438, 18, 18, 7, 12, 332, 64,
                        680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                        animation_master, sound_master),
            Dragon(800, 352, 22, 20, 8, 22, 400, 96,
                   680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                   animation_master, sound_master),
            Medusa(800, 365, 26, 31, 12, 18, 480, 80,
                  680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                  animation_master, sound_master),
            Demon(600, 365, 30, 41, 25, 25, 666, 120,
                  680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                  animation_master, sound_master),
            BanditChief(10, 17, 10, 0, 214, 0, sound_master),
            Djinn(14, 0, 25, 20, 278, 40, sound_master),
            SmallDragon(18, 18, 7, 12, 332, 50, sound_master),
            Dragon(22, 20, 8, 22, 400, 70, sound_master),
            Demon(26, 31, 12, 18, 480, 50, sound_master),
            Demon(30, 41, 25, 25, 666, 80, sound_master),
        ]
        return bosses[boss_level]
