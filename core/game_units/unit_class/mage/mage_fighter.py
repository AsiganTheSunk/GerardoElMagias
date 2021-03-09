from random import randint


class MageFighter:
    HIT = ' Hit ! '
    CRITICAL_HIT = ' Critical Hit ! '
    RESIST = ' Resist ! '

    @staticmethod
    def critical_hit(base_damage, multiplier=2):
        return base_damage * multiplier

    @staticmethod
    def critical_chance(hit_chance, magic):
        if hit_chance < round(magic/2):
            return True
        return False

    @staticmethod
    def hit_chance():
        return randint(0, 99)

    def cast_spell(self, magic, base_damage, multiplier):
        # Calculate Basic Damage: Based on Magic
        base_damage = (magic * multiplier) + base_damage

        # Calculate Hit Change: Based on Random Integer
        hit_chance = self.hit_chance()

        # Calculate Miss, Basic Damage & Critical Hit
        if self.critical_chance(hit_chance, magic):
            return self.critical_hit(base_damage), self.CRITICAL_HIT
        return base_damage, self.HIT