#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.game.battle.combat.constants.combat_type_resolution import CombatTypeResolution


class CombatFormulas:
    @staticmethod
    def critical_hit(base_damage, multiplier=2):
        return base_damage * multiplier

    @staticmethod
    def melee_critical_chance(hit_resolution, attack_rating):
        # print('Critical Hit Chance', (hit_resolution, round(attack_rating / 2)), hit_resolution <= round(attack_rating / 2))
        return hit_resolution <= round(attack_rating / 2)

    @staticmethod
    def spell_critical_chance(hit_resolution, magic_power):
        return hit_resolution <= round(magic_power / 2)

    @staticmethod
    def melee_hit_chance(hit_resolution, attack_rating):
        # print('Hit Chance', (hit_resolution, 85 + round(attack_rating / 5)), hit_resolution < 85 + round(attack_rating / 5))
        return hit_resolution < 85 + round(attack_rating / 5)

    @staticmethod
    def melee_block_chance(block_chance=5):
        block_resolution = randint(1, 100)
        # print('Block Chance', (block_resolution, block_chance), block_resolution <= block_chance)
        return block_resolution <= block_chance

    @staticmethod
    def hit_resolution():
        # Calculate Hit Chance: Based on Random Integer
        return randint(1, 100)

    def melee_attack_resolution(self, caster, output_damage, hit_resolution):
        # print()
        # print('//////////' * 8)
        if self.melee_hit_chance(hit_resolution, caster.attack_rating):
            if not self.melee_block_chance():
                if self.melee_critical_chance(hit_resolution, caster.attack_rating):
                    return self.critical_hit(output_damage), CombatTypeResolution.CRITICAL_HIT
                return output_damage, CombatTypeResolution.HIT
            return 0, CombatTypeResolution.BLOCKED
        return 0, CombatTypeResolution.MISS

    def spell_attack_resolution(self, caster, output_damage, hit_resolution):
        # Calculate Basic Damage & Critical Hit
        if self.spell_critical_chance(hit_resolution, caster.magic_power):
            return self.critical_hit(output_damage), CombatTypeResolution.CRITICAL_HIT
        return output_damage, CombatTypeResolution.HIT

    def fixed_damage_attack_resolution(self, output_damage):
        return output_damage, CombatTypeResolution.HIT
