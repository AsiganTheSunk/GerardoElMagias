# Combat Imports
from core.units.combat.combat_formulas import CombatFormulas
from core.units.combat.combat_resolver import CombatResolver

from core.text.damage_text import DamageText

# Init: Damage Text
damage_text = DamageText()


class FurySpells(CombatFormulas, CombatResolver):
    def __init__(self):
        CombatResolver.__init__(self)
        CombatFormulas.__init__(self)

    def cast_path_of_the_seven_strikes(self, caster, attack_number, target_list, damage_text_group,
                                       action_cooldown, action_wait_time, current_fighter, ultimate_status):
        pass
        # return self.cast_multi_strike_attack(caster, attack_number, 7, target_list, damage_text_group,
        #                                      action_cooldown, action_wait_time, current_fighter, ultimate_status)


