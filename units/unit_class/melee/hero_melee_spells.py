from units.unit_class.melee.melee_figher import MeleeFighter
from floating_text.damage_text import DamageText
from random import randint

# Init: Damage Text
damage_text = DamageText()


class HeroMeleeSpells(MeleeFighter):
    def cast_multi_strike_attack(self, caster, number_of_strikes, multi_strike, target_list, damage_text_group,
                                 action_cooldown, action_wait_time, current_fighter, ultimate_status):
        alive_enemy = []
        for enemy_unit in target_list:
            if enemy_unit.alive:
                alive_enemy.append(enemy_unit)

        if number_of_strikes < multi_strike:
            if action_cooldown >= action_wait_time:
                if len(alive_enemy) > 0:
                    enemy_index = randint(0, len(alive_enemy) - 1)
                    target_unit = alive_enemy[enemy_index]
                    caster.attack(target_unit, damage_text_group)
                    number_of_strikes += 1

                    # Animation will be accelerated
                    action_cooldown = 55
        else:
            attack_number = 0
            ultimate_status = False
            current_fighter += 1
            # Action Delay: Next Enemy Action will be dealayed after the ultimate cast
            action_cooldown = -25

        return number_of_strikes, current_fighter, action_cooldown, ultimate_status

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

    def cast_path_of_the_seven_strikes(self, caster, attack_number, target_list, damage_text_group,
                                       action_cooldown, action_wait_time, current_fighter, ultimate_status):
        return self.cast_multi_strike_attack(caster, attack_number, 7, target_list, damage_text_group,
                                             action_cooldown, action_wait_time, current_fighter, ultimate_status)


