#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

# Combat Imports
from core.game.battle.combat.combat_formulas import CombatFormulas
from core.game.battle.combat.combat_resolver import CombatResolver
from core.game.text.damage_text import DamageText
from core.game.text.combat_text_resolver import CombatTextResolver

# Init: Damage Text
combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


class MeleeSpells(CombatFormulas, CombatResolver):
    def __init__(self, sound_master):
        CombatFormulas.__init__(self)
        CombatResolver.__init__(self, sound_master)

    def cast_attack(self, caster, target, text_sprite, multi_strke=False):
        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 6)

        output_damage = (caster.attack_power * 1) + base_damage

        input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
        self.resolve_attack(caster, target, input_damage, input_type, text_sprite, multi_strke)

    def cast_strong_attack(self, caster, target, text_sprite):
        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 0)
        output_damage = (caster.attack_power * 3) + base_damage

        input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
        self.resolve_attack(caster, target, input_damage, input_type, text_sprite)

    def cast_power_of_two_attack(self, target, text_sprite, exponent):
        output_damage = 2 ** exponent
        input_damage, input_type = self.fixed_damage_attack_resolution(output_damage)
        self.resolve_fixed_damage_attack(target, input_damage, input_type, text_sprite)

        damage_text.cast(self, "Power Of Two: 2^" + str(exponent), text_sprite, 0, -30)




