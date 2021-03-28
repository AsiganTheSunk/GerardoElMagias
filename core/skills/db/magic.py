#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.game.battle.combat.combat_formulas import CombatFormulas
from core.game.battle.combat.combat_resolver import CombatResolver
from core.game.battle.combat.combat_utils import get_alive_targets
from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText

# Init: Damage Text
combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


class MagicSpells(CombatFormulas, CombatResolver):
    def __init__(self):
        CombatResolver.__init__(self)
        CombatFormulas.__init__(self)

    @staticmethod
    def cast_heal(caster, target, damage_text_group):
        # Display Header Cast
        # Todo: Init proper 150x, 400y
        damage_text.cast(caster, "Heal", damage_text_group, 0, -30)

        base_heal = 1 + randint(0, 10) + (caster.magic * 4)
        if target.max_hp - target.current_hp > base_heal:
            heal_amount = base_heal
        else:
            heal_amount = target.max_hp - target.current_hp
        target.current_hp += heal_amount

        damage_text.heal(caster, str(heal_amount), damage_text_group)

    def cast_firestorm(self, caster, target_list, damage_text_group):
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, " Fire Storm! ", damage_text_group, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = randint(0, 5)
                output_damage = (caster.magic * 2) + base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            # print(input_damage_list, input_type_list)
            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, damage_text_group)

    def cast_lightning(self, caster, target_list, damage_text_group):
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, " Lightning Bolt! ", damage_text_group, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = randint(1, 55)
                output_damage = base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, damage_text_group)

    def cast_earth_shock(self, caster, target_list, damage_text_group):
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, " Earth Shock! ", damage_text_group, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = 10
                output_damage = (caster.magic * 1) + base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, damage_text_group)

    def cast_water_nova(self, caster, target_list, damage_text_group):
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, " Water Nova! ", damage_text_group, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = 3
                output_damage = (caster.magic * 1) + base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, damage_text_group)

    def cast_shadow_bolt(self, caster, target, damage_text_group):
        # Display Header Cast
        damage_text.cast(caster, " Shadow Bolt! ", damage_text_group, 0, -30)

        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 3)
        output_damage = caster.magic + base_damage

        input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
        self.resolve_attack(caster, target, input_damage, input_type, damage_text_group)
