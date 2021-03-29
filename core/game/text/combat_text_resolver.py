#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.text.damage_text import DamageText
from core.game.battle.combat.constants.combat_type_resolution import CombatTypeResolution

# Init: Damage Text
damage_text = DamageText()


class CombatTextResolver:
    @staticmethod
    def resolve(target, output_damage, output_type, text_sprite):
        if output_type is CombatTypeResolution.BLOCKED:
            damage_text.block(target, output_damage, text_sprite)
        elif output_type is CombatTypeResolution.MISS:
            damage_text.miss(target, output_damage, text_sprite)
        elif output_type is CombatTypeResolution.CRITICAL_HIT:
            damage_text.critical_hit(target, output_damage, text_sprite)
        elif output_type is CombatTypeResolution.HIT:
            damage_text.hit(target, output_damage, text_sprite)
