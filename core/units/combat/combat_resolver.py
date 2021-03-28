#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.combat.combat_type_resolution import CombatTypeResolution

import constants.globals

from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()

from core.units.combat.utils import get_alive_targets
from constants.sound import *
from random import randint


class CombatResolver:
    @staticmethod
    def resolve_attack(caster, target, input_damage, input_type, damage_text_group, multi_strike=False):
        if not multi_strike:
            constants.globals.action_cooldown = 0

        # Activates Block Animation & Sound on the current Target
        if input_type is CombatTypeResolution.BLOCKED:
            target.block_animation()
            block_sound.play()
            # target.block_sound.play()

        # Activates Miss Animation & Sound on the current Target
        elif input_type is CombatTypeResolution.MISS:
            target.miss_animation()
            miss_sound.play()
            # target.miss_sound.play()

        # Activates Hurt/Death Animation and Sound on the current Target
        else:
            if input_damage != 0:
                target.hurt_animation()

                # Activates Critical Hit Sound
                if input_type is CombatTypeResolution.CRITICAL_HIT:
                    critical_hit_sound.play()
                    # target.critical_hit_sound.play()
                else:
                    hit_cut_sound.play()

                # Updates current Target Health
                target.reduce_health(input_damage)

                if target.has_fury():
                    # Updates current Target Fury
                    target.gain_fury(input_damage)
                    # target.gain_fury_animation()
                    # target.gain_fury_sound.play()

                # TODO Activates hurt sound
                # Evaluate Death: Target
                if target.is_dead():
                    target.death()
                    target.death_animation()
                    constants.globals.clicked = False
                    if caster.has_experience():
                        caster.experience_system.evaluate_kill(caster, target, damage_text_group)

        combat_text_resolver.resolve(target, input_damage,  input_type, damage_text_group)

    def resolve_aoe_attack(self, caster, target_list, input_damage_list, input_damage_type_list, damage_text_group):
        for index, target in enumerate(target_list):
            print(index, target.name, len(target_list))
            if target.alive:
                self.resolve_attack(caster, target, input_damage_list[index], input_damage_type_list[index], damage_text_group, True)
            else:
                pass

    def resolve_multi_attack(self, caster, target_list, multi_strike, damage_text_group):
        alive_enemy = get_alive_targets(target_list)

        # TODO: pass de proper wait time instead of 90
        if self.multi_attacks_left >= 0:
            if constants.globals.action_cooldown >= 90:
                if len(alive_enemy) > 0:
                    target = alive_enemy[randint(0, len(alive_enemy) - 1)]
                    caster.melee_attack_animation()
                    caster.cast_attack(self, target, damage_text_group, True)

                    self.multi_attacks_left -= 1
                    constants.globals.action_cooldown = 65

        else:
            self.multi_attacks_left = 7
            caster.ultimate_status = False
            # Action Delay: Next Enemy Action will be delayed after the ultimate cast
            constants.globals.action_cooldown = -40

    def resolve_fixed_damage_attack(self, target, input_damage, input_type, damage_text_group):
        target.hurt_animation()
        hit_cut_sound.play()

        target.reduce_health(input_damage)

        if target.has_fury():
            target.gain_fury(input_damage)

        if target.is_dead():
            target.death()
            target.death_animation()
            constants.globals.clicked = False

        combat_text_resolver.resolve(target, input_damage,  input_type, damage_text_group)