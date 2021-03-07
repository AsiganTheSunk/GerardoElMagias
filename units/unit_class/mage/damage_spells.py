from random import randint
from units.unit_class.mage.mage_fighter import MageFighter
from constants.basic_colors import *
from floating_text.combat_text import CombatText
from floating_text.damagetext import DamageText


class DamageSpells(MageFighter):
    def cast_aoe_spell(self, caster, base_damage, base_multiplier, target_list, damage_text_group):
        for count, target_unit in enumerate(target_list):
            output_damage, output_message, output_color = \
                self.cast_spell(caster.magic, caster.intellect, base_damage, base_multiplier)

            floating_text = CombatText(target_unit.unit_animation.rect.centerx, target_unit.unit_animation.rect.y,
                                       str(output_damage) + output_message, output_color, 'move_up')
            damage_text_group.add(floating_text.combat_text())

            if target_unit.alive:
                target_unit.current_hp -= output_damage
                target_unit.hurt()

                if target_unit.current_hp < 1:
                    target_unit.death()

        return target_list

    def cast_firestorm(self, caster, target_list, damage_text_group):
        # Basic Spell Attributes
        base_damage = randint(0, 20)
        base_multiplier = 3

        alive_enemy = []
        for enemy_unit in target_list:
            if enemy_unit.alive:
                alive_enemy.append(enemy_unit)

        if len(alive_enemy) > 0:
            floating_text = CombatText(200, 500, " Firestorm! ", RED_COLOR, 'move_up')
            damage_text_group.add(floating_text.cast_text())

            return self.cast_aoe_spell(caster, base_damage, base_multiplier, alive_enemy, damage_text_group)
        return target_list

    def cast_lightning(self, caster, target_list, damage_text_group):
        # Basic Spell Attributes
        base_damage = randint(0, 10)
        base_multiplier = 2

        alive_enemy = []
        for enemy_unit in target_list:
            if enemy_unit.alive:
                alive_enemy.append(enemy_unit)

        if len(alive_enemy) > 0:
            floating_text = CombatText(200, 500, " Lightning Bolt! ", YELLOW_COLOR, 'move_up')
            damage_text_group.add(floating_text.cast_text())

            return self.cast_aoe_spell(caster, base_damage, base_multiplier, target_list, damage_text_group)
        return target_list
