#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.units.enemy.bandit.bandit import Bandit
from core.units.enemy.bone.bone_wizard import BoneWizard
from core.units.enemy.lizard.lizard import Lizard
from core.units.constants.unit_type import UnitType
from core.game.battle.enemy.set_generator import EnemySetGenerator
from core.game.battle.enemy.stats_generator import EnemyStatsGenerator
from core.game.battle.enemy.position_generator import EnemyPositionsGenerator
from core.units.enemy.bandit.bandit_chief import BanditChief
from core.units.enemy.dragon.small_dragon import SmallDragon
from core.units.enemy.dragon.dragon import Dragon
from core.units.enemy.djinn.djinn import Djinn
from core.units.enemy.demon.demon import Demon


class EnemyGroupGenerator(EnemyStatsGenerator, EnemyPositionsGenerator, EnemySetGenerator):
    def __init__(self, animation_master, sound_master, game_attributes):
        EnemyStatsGenerator.__init__(self)
        EnemyPositionsGenerator.__init__(self)
        EnemySetGenerator.__init__(self)

        self.animation_master = animation_master
        self.sound_master = sound_master
        self.game_attributes = game_attributes

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
            return randint(3,4)

    def get_enemy_healthbar_positions(self):
        return [
            (680, self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
            (680, self.game_attributes.screen_height - self.game_attributes.panel_height + 100),
            (900, self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
            (900, self.game_attributes.screen_height - self.game_attributes.panel_height + 100)
        ]

    def get_enemy(self, enemy_type, level, enemy_pos_x, enemy_pos_y, enemy_healthbar_x, enemy_healthbar_y):
        if enemy_type is UnitType.BANDIT:
            random_level, attack_power, attack_rating, magic_power, max_hp, max_mp = self.generate_bandit_stats(level)
            return Bandit(enemy_pos_x, enemy_pos_y, random_level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                          enemy_healthbar_x, enemy_healthbar_y, self.animation_master, self.sound_master)

        elif enemy_type is UnitType.LIZARD:
            random_level, attack_power, attack_rating, magic_power, max_hp, max_mp = self.generate_lizard_stats(level)
            return Lizard(enemy_pos_x, enemy_pos_y, random_level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                          enemy_healthbar_x, enemy_healthbar_y, self.animation_master, self.sound_master)

        elif enemy_type is UnitType.BONE_WIZARD:
            random_level, attack_power, attack_rating, magic_power, max_hp, max_mp = self.generate_bone_wizard_stats(level)
            return BoneWizard(enemy_pos_x, enemy_pos_y, random_level, attack_power, attack_rating, magic_power, max_hp, max_mp,
                              enemy_healthbar_x, enemy_healthbar_y, self.animation_master, self.sound_master)

    def generate_enemy(self, level, boss_level):
        enemy_group = []
        group_size = self.generate_group_size(level)
        enemy_set = self.get_enemy_set(boss_level, group_size)
        enemy_positions = self.get_enemy_positions(boss_level)
        enemy_healthbar_positions = self.get_enemy_healthbar_positions()
        for index in range(group_size):
            enemy_pos_x, enemy_pos_y = enemy_positions[index]
            enemy_healthbar_x, enemy_healthbar_y = enemy_healthbar_positions[index]
            current_enemy = self.get_enemy(enemy_set[index], level, enemy_pos_x, enemy_pos_y, enemy_healthbar_x, enemy_healthbar_y)
            enemy_group.append(current_enemy)
        return enemy_group

    def scripted_enemy(self, boss_level, animation_master, sound_master):
        bosses = [
            None,
            BanditChief(650, 475, 10, 17, 10, 0, 214, 0,
                        680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                        animation_master, sound_master),
            Djinn(750, 400, 14, 0, 25, 20, 278, 40,
                  680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                  animation_master, sound_master),
            SmallDragon(730, 438, 18, 18, 7, 12, 332, 50,
                        680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                        animation_master, sound_master),
            Dragon(800, 352, 22, 20, 8, 22, 400, 70,
                   680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                   animation_master, sound_master),
            Demon(800, 365, 26, 31, 12, 18, 480, 50,
                  680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                  animation_master, sound_master),
            Demon(600, 365, 30, 41, 25, 25, 666, 80,
                  680, (self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                  animation_master, sound_master),
        ]
        return bosses[boss_level]
