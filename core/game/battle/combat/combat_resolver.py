#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.battle.combat.constants.combat_type_resolution import CombatTypeResolution
import constants.globals
from core.game.battle.combat.combat_utils import get_alive_targets
from random import randint
from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class CombatResolver:
    def __init__(self, sound_master):
        self.sound_master = sound_master

    def resolve_attack(self, caster, target, input_damage, input_type, text_sprite, multi_strike=False):
        if not multi_strike:
            constants.globals.action_cooldown = 0

        # Activates Block Animation & Sound on the current Target
        if input_type is CombatTypeResolution.BLOCKED:
            target.use_animation('Block')
            self.sound_master.play_unit_fx_sound('block')

        # Activates Miss Animation & Sound on the current Target
        elif input_type is CombatTypeResolution.MISS:
            target.use_animation('Miss')
            self.sound_master.play_unit_fx_sound('miss')

        # Activates Hurt/Death Animation and Sound on the current Target
        else:
            if input_damage != 0:
                target.use_animation('Hurt')

                # Activates Critical Hit Sound
                if input_type is CombatTypeResolution.CRITICAL_HIT:
                    self.sound_master.play_unit_fx_sound('critical_hit')
                else:
                    self.sound_master.play_unit_fx_sound('hit_cut')

                # Updates current Target Health
                target.reduce_health(input_damage)

                if target.has_fury():
                    # Updates current Target Fury
                    target.gain_fury(input_damage)
                    if target.has_enough_fury(50) or target.has_enough_fury():
                        self.sound_master.play_unit_fx_sound('ultimate_up')

                # TODO Activates hurt sound
                # Evaluate Death: Target
                if target.is_dead():
                    target.death()
                    target.use_animation('Death')
                    constants.globals.clicked = False
                    if caster.has_experience():
                        caster.experience_system.evaluate_kill(caster, target, text_sprite)

        combat_text_resolver.resolve(target, input_damage,  input_type, text_sprite)

    def resolve_aoe_attack(self, caster, target_list, input_damage_list, input_damage_type_list, text_sprite):
        for index, target in enumerate(target_list):
            if target.alive:
                self.resolve_attack(caster, target, input_damage_list[index], input_damage_type_list[index],
                                    text_sprite, True)

    def resolve_multi_attack(self, caster, target_list, multi_strike, text_sprite):
        alive_enemy = get_alive_targets(target_list)

        # TODO: pass de proper wait time instead of 90
        if self.multi_attacks_left >= 0:
            if constants.globals.action_cooldown >= 90:
                if len(alive_enemy) > 0:
                    target = alive_enemy[randint(0, len(alive_enemy) - 1)]
                    caster.melee_attack_animation()
                    caster.cast_attack(self, target, text_sprite, True)

                    self.multi_attacks_left -= 1
                    constants.globals.action_cooldown = 65

        else:
            self.multi_attacks_left = 7
            caster.ultimate_status = False
            # Action Delay: Next Enemy Action will be delayed after the ultimate cast
            constants.globals.action_cooldown = -40

    def resolve_fixed_damage_attack(self, target, input_damage, input_type, text_sprite):
        target.use_animation('Hurt')
        self.sound_master.play_unit_fx_sound('hit_cut')

        target.reduce_health(input_damage)

        if target.has_fury():
            target.gain_fury(input_damage)
            if target.has_enough_fury(50) or target.has_enough_fury():
                self.sound_master.play_unit_fx_sound('ultimate_up')

        if target.is_dead():
            target.death()
            target.use_animation('Death')
            constants.globals.clicked = False

        combat_text_resolver.resolve(target, input_damage,  input_type, text_sprite)