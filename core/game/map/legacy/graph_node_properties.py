#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicNodeProperties:
    def __init__(self, level, number_of_battles=None, boss_battle_index=None, enemy_types=None, boss_types=None):
        self.level = level
        self.number_of_battles = self.generate_number_of_battles(number_of_battles)
        self.boss_battle_index = boss_battle_index
        self.number_of_bosses = len(boss_battle_index)
        self.enemy_types = enemy_types
        self.boss_types = boss_types
        self.complete_status = False

    def generate_number_of_battles(self, number_of_battles):
        if number_of_battles is None:
            return self.random_number_of_battles()
        return number_of_battles

    def random_number_of_battles(self):
        return 1

    def random_boss_battle_index(self):
        return 1

    def complete_stage_node(self):
        self.complete_status = True

    def get_full_path(self):
        full_path_list = []
        for battle_index in range(self.number_of_battles):
            if battle_index in self.boss_battle_index:
                full_path_list.append(True)
            else:
                full_path_list.append(False)
        return full_path_list