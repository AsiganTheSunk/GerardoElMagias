#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.game.battle.combat.combat_formulas import CombatFormulas
from core.game.battle.combat.combat_resolver import CombatResolver
from core.game.battle.combat.combat_utils import get_alive_targets
from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText
import constants.globals

# Init: Damage Text
combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


class MagicSpells(CombatFormulas, CombatResolver):
    def __init__(self, sound_master):
        self.sound_master = sound_master
        CombatFormulas.__init__(self)
        CombatResolver.__init__(self, sound_master)

    @staticmethod
    def cast_heal(caster, target, text_sprite):
        constants.globals.action_cooldown = -30
        # Display Header Cast
        # Todo: Init proper 150x, 400y
        damage_text.cast(caster, "Heal", text_sprite, 0, -30)

        base_heal = 1 + randint(0, 10) + (caster.magic_power * 4)
        if target.max_hp - target.current_hp > base_heal:
            heal_amount = base_heal
        else:
            heal_amount = target.max_hp - target.current_hp
        target.current_hp += heal_amount

        damage_text.heal(caster, str(heal_amount), text_sprite)

    def cast_firestorm(self, caster, target_list, text_sprite):
        constants.globals.action_cooldown = -30
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, "Firestorm!", text_sprite, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = randint(0, 5)
                output_damage = (caster.magic_power * 2) + base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            # print(input_damage_list, input_type_list)
            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, text_sprite)

    def cast_lightning(self, caster, target_list, text_sprite):
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, "Lightning Bolt!", text_sprite, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = randint(1, 55)
                output_damage = base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, text_sprite)

    def cast_earth_shock(self, caster, target_list, text_sprite):
        constants.globals.action_cooldown = -30
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, "Earth Shock!", text_sprite, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = 10
                output_damage = (caster.magic_power * 1) + base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, text_sprite)

    def cast_water_nova(self, caster, target_list, text_sprite):
        constants.globals.action_cooldown = -30
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            # Display Header Cast
            damage_text.cast(caster, "Water Nova!", text_sprite, 0, -30)

            input_damage_list = []
            input_type_list = []
            for _ in target_list:
                # Basic Spell Attributes: minimum, maximum, multiplier
                base_damage = 3
                output_damage = (caster.magic_power * 1) + base_damage

                input_damage, input_type = self.spell_attack_resolution(caster, output_damage, self.hit_resolution())
                input_damage_list.append(input_damage)
                input_type_list.append(input_type)

            self.resolve_aoe_attack(caster, target_list, input_damage_list, input_type_list, text_sprite)

    def cast_shadow_bolt(self, caster, target, text_sprite):
        constants.globals.action_cooldown = -30
        # Display Header Cast
        damage_text.cast(caster, "Shadow Bolt!", text_sprite, 0, -30)

        # Calculate Basic Damage: Based on Strength
        base_damage = randint(0, 3)
        output_damage = caster.magic_power + base_damage

        input_damage, input_type = self.melee_attack_resolution(caster, output_damage, self.hit_resolution())
        self.resolve_attack(caster, target, input_damage, input_type, text_sprite)
