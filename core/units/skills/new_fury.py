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
        input_damage_list = []
        input_type_list = []

        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 6)
        output_damage = (caster.strength * 1) + base_damage

        if len(alive_enemy) > 0 and constants.globals.number_of_strikes:
            damage_text.cast(self, "Senda de los 7 Golpes", damage_text_group)

            for _ in range(multi_strike):
                input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            print(input_damage_list)
            print(input_type_list)

        return self.resolve_multi_attack(caster, target_list, multi_strike, input_damage_list, input_type_list, damage_text_group)


