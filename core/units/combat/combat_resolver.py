from core.units.combat.combat_type_resolution import CombatTypeResolution

import constants.globals

from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class CombatResolver:
    @staticmethod
    def resolve_attack(target, input_damage, input_type, damage_text_group):
        constants.globals.action_cooldown = 0
        constants.globals.current_fighter += 1

        # Activates Block Animation & Sound on the current Target
        if input_type is CombatTypeResolution.BLOCKED:
            target.block()
            target.block_sound.play()

        # Activates Miss Animation & Sound on the current Target
        elif input_type in CombatTypeResolution.MISS:
            target.miss()
            target.miss_sound.play()

        # Activates Hurt/Death Animation and Sound on the current Target
        else:
            # Activates Critical Hit Sound
            if input_type in CombatTypeResolution.CRITICAL_HIT:
                target.critical_hit_animation()
                target.critical_hit_sound.play()

            else:
                target.hit_animation()
                target.hit_sound.play()

            if input_damage != 0:
                # Updates current Target Health
                target.reduce_health(input_damage)

                if target.has_fury():
                    # Updates current Target Fury
                    target.gain_fury(input_damage)
                    # target.gain_fury_animation()
                    # target.gain_fury_sound.play()

                # Activates Hurt Animation: Target
                target.hurt_animation()
                target.hurt_sound.play()
                # hit_cut_sound.play()

                # TODO Activates hurt sound
                # Evaluate Death: Target
                if target.is_dead():
                    target.death()
                    target.death_animation()

        combat_text_resolver.resolve(target, input_damage,  input_type, damage_text_group)

    def resolve_aoe_attack(self, target_list, input_damage_list, input_damage_type_list, damage_text_group):
        for index, target in enumerate(target_list):
            if target.alive:
                self.resolve_attack(target, input_damage_list[index], input_damage_type_list[index], damage_text_group)
            else:
                pass

    #
    #     def cast_multi_strike_attack(self, caster, number_of_strikes, multi_strike, target_list, damage_text_group,
    #                                  action_cooldown, action_wait_time, current_fighter, ultimate_status):
    #
    # def resolve_multi_attack(self, caster, target_list, input_damage_list, input_damage_type):
    #
    #     alive_enemy = get_alive_targets(target_list)
    #     if number_of_strikes < multi_strike:
    #         if action_cooldown >= action_wait_time:
    #             if len(alive_enemy) > 0:
    #                 enemy_index = randint(0, len(alive_enemy) - 1)
    #                 target_unit = alive_enemy[enemy_index]
    #                 caster.attack(target_unit, damage_text_group)
    #                 number_of_strikes += 1
    #
    #                 # Animation will be accelerated
    #                 action_cooldown = 55
    #     else:
    #         number_of_strikes = 0
    #         ultimate_status = False
    #         current_fighter += 1
    #         # Action Delay: Next Enemy Action will be delayed after the ultimate cast
    #         action_cooldown = -25
    #
    #     return number_of_strikes, current_fighter, action_cooldown, ultimate_status