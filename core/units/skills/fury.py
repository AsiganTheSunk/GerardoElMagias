# Combat Imports
from core.units.combat.combat_formulas import CombatFormulas
from core.units.combat.combat_resolver import CombatResolver
from core.units.combat.utils import get_alive_targets
from core.text.damage_text import DamageText

from random import randint
import constants.globals

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
            damage_text.cast(self, "Senda de los 7 Golpes", damage_text_group)

        return self.resolve_multi_attack(caster, target_list, multi_strike, damage_text_group)
