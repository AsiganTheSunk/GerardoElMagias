#!/usr/bin/env python
# -*- coding: utf-8 -*-


class EnemyPositionsGenerator:
    @staticmethod
    def generate_forest_enemy_positions():
        return [(650, 475), (775, 500), (900, 475), (1025, 500)]

    @staticmethod
    def generate_castle_enemy_positions():
        return [(700, 420), (825, 480), (950, 420), (1075, 480)]

    @staticmethod
    def generate_dungeon_enemy_positions():
        return [(700, 370), (825, 450), (950, 370), (1075, 450)]

    def get_enemy_positions(self, boss_level):
        if boss_level > 3:
            return self.generate_dungeon_enemy_positions()
        elif boss_level > 1:
            return self.generate_castle_enemy_positions()
        else:
            return self.generate_forest_enemy_positions()
