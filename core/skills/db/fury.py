#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Combat Imports
from game.battle.combat import CombatFormulas
from game.battle.combat.combat_resolver import CombatResolver
from game.battle.combat import get_alive_targets
from game.text.damage_text import DamageText

# Init: Damage Text
damage_text = DamageText()


class FurySpells(CombatFormulas, CombatResolver):
    def __init__(self):
        CombatFormulas.__init__(self)
        CombatResolver.__init__(self)

    def cast_path_of_the_seven_strikes(self, caster, target_list, damage_text_group):
        multi_strike = 7
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0 and self.multi_attacks_left == 7:
            damage_text.cast(self, "Senda de los 7 Golpes", damage_text_group, 0, -30)

        return self.resolve_multi_attack(caster, target_list, multi_strike, damage_text_group)
