from units.unit_class.melee.melee_figher import MeleeFighter
from constants.basic_colors import *
from floating_text.damage_text import DamageText
from random import randint
from pygame import time

class HeroMeleeSpells(MeleeFighter):
    def cast_multi_strike_attack(self, caster, multi_strike, target_list, damage_text_group):
        """
        This function will multi strike a enemy or group of enemies based on the parameter multi_strike
        :param caster:
        :param multi_strike:
        :param target_list:
        :param damage_text_group:
        :return:
        """


        alive_enemy = []
        for enemy_unit in target_list:
            if enemy_unit.alive:
                alive_enemy.append(enemy_unit)

        for attack_number in range(multi_strike):
            if len(alive_enemy) > 0:
                enemy_index = randint(0, len(alive_enemy) - 1)
                target_unit = alive_enemy[enemy_index]
                caster.attack(target_unit, damage_text_group)
                if target_unit.current_hp < 1:
                    alive_enemy.pop(enemy_index)



    def cast_aoe_attack(self, caster, target_list, damage_text_group):
        for count, target_unit in enumerate(target_list):
            if target_unit.alive:
                output_damage, output_message, output_color = self.cast_attack(caster)

                target_unit.current_hp -= output_damage
                target_unit.hurt()

                damage_text = DamageText(target_unit.unit_animation.rect.centerx, target_unit.unit_animation.rect.y, str(output_damage) + output_message, output_color)
                damage_text_group.add(damage_text)

                if target_unit.current_hp < 1:
                    target_unit.death()

        return target_list

    def cast_ultimate(self, caster, target_list, damage_text_group):
        damage_text = DamageText(200, 500, "Senda de los 7 Golpes", RED_COLOR)
        damage_text_group.add(damage_text)

        return self.cast_multi_strike_attack(caster, 7, target_list, damage_text_group)
