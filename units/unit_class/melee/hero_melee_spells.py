from units.unit_class.melee.melee_figher import MeleeFighter
from floating_text.damage_text import DamageText
from random import randint

# Init: Damage Text
damage_text = DamageText()


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

                damage_text.hit(caster, str(output_damage) + output_message, damage_text_group)

                if target_unit.current_hp < 1:
                    target_unit.death()

        return target_list

    def cast_ultimate(self, caster, target_list, damage_text_group):

        # Todo: init proper position 200x, 500y
        damage_text.cast(caster, "Senda de los 7 Golpes", damage_text_group)
        return self.cast_multi_strike_attack(caster, 7, target_list, damage_text_group)
