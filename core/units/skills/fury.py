from core.units.spells.melee_skills import MeleeFighter
from core.text.damage_text import DamageText
from random import randint
from core.units.unit_mechanic.utils import get_alive_targets

# Init: Damage Text
damage_text = DamageText()


class FurySpells(MeleeFighter):
    def cast_path_of_the_seven_strikes(self, caster, attack_number, target_list, damage_text_group,
                                       action_cooldown, action_wait_time, current_fighter, ultimate_status):
        return self.cast_multi_strike_attack(caster, attack_number, 7, target_list, damage_text_group,
                                             action_cooldown, action_wait_time, current_fighter, ultimate_status)


