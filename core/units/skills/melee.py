from random import randint

# Combat Imports
from core.units.combat.combat_formulas import CombatFormulas
from core.units.combat.combat_resolver import CombatResolver


class MeleeSpells(CombatFormulas, CombatResolver):
    def __init__(self):
        CombatResolver.__init__(self)
        CombatFormulas.__init__(self)

    def cast_multi_attack(self, caster, target_list):
        pass

    def cast_aoe_attack(self, caster, target_list):
        pass

    def cast_attack(self, caster, target, damage_text_group):
        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 6)
        output_damage = (caster.strength * 1) + base_damage

        input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
        self.resolve_attack(target, input_damage, input_type, damage_text_group)

    def cast_strong_attack(self, caster, target, damage_text_group):
        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 0)
        output_damage = (caster.strength * 3) + base_damage

        input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
        self.resolve_attack(target, input_damage, input_type, damage_text_group)



