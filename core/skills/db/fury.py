#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Combat Imports
from core.game.battle.combat.combat_formulas import CombatFormulas
from core.game.battle.combat.combat_resolver import CombatResolver
from core.game.battle.combat.combat_utils import get_alive_targets
from core.game.text.damage_text import DamageText

# Init: Damage Text
damage_text = DamageText()


class FurySpells(CombatFormulas, CombatResolver):
    def __init__(self):
        CombatFormulas.__init__(self)
        CombatResolver.__init__(self)

    def cast_path_of_the_seven_strikes(self, caster, target_list, text_sprite):
        multi_strike = 7
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0 and self.multi_attacks_left == 7:
            damage_text.cast(self, "Path Of The 7 Strikes", text_sprite, 0, -30)

        return self.resolve_multi_attack(caster, target_list, multi_strike, text_sprite)

    def cast_whirlwind(self, caster, target_list, text_sprite):
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            damage_text.cast(caster, "Whirlwind", text_sprite, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                output_damage = round(caster.strength * 1.5)
                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, text_sprite)


