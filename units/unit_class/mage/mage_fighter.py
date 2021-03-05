from random import randint
from constants.basic_colors import *


class MageFighter:
    HIT = ' Hit! '
    CRITICAL_HIT = ' Critical Hit! '
    RESIST = ' Resist! '

    @staticmethod
    def critical_hit(base_damage, multiplier=2):
        return base_damage * multiplier

    @staticmethod
    def critical_chance(hit_chance, intellect):
        if hit_chance < intellect:
            return True
        return False

    @staticmethod
    def miss_chance(hit_chance, dexterity):
        if hit_chance > (80 + dexterity):
            return True
        return False

    @staticmethod
    def hit_chance():
        return randint(0, 99)

    def cast_spell(self, magic, intellect, base_damage, multiplier):
        # Calculate Basic Damage: Based on Magic
        base_damage = (magic * multiplier) + base_damage

        # Calculate Hit Change: Based on Random Integer
        hit_chance = self.hit_chance()

        # Calculate Miss, Basic Damage & Critical Hit
        if not self.miss_chance(hit_chance, intellect):
            if self.critical_chance(hit_chance, intellect):
                return self.critical_hit(base_damage), self.CRITICAL_HIT, RED_COLOR
            return base_damage, self.HIT, RED_COLOR
        return 0, self.RESIST, WHITE_COLOR
