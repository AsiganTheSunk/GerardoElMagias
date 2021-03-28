#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from core.game.text.damage_text import DamageText
from core.items.consumable.constants.recovered_stat_type import RecoveredStatType

# Init: Damage Text
damage_text = DamageText()


class BasicConsumable:
    def __init__(self, name, recovered_stat, base_stat, base_stat_interval, base_stat_multiplier, consume_sound):
        self.name = name
        self.recovered_stat = recovered_stat
        self.base_stat = base_stat
        self.base_stat_interval = base_stat_interval
        self.base_stat_multiplier = base_stat_multiplier
        self.consume_sound = consume_sound

    def resolve_recovered_stat(self, caster):
        final_base_stat_multiplier = 0
        final_base_stat_interval = 0

        if self.base_stat_interval is not None:
            final_base_stat_interval = randint(0, self.base_stat_interval)
        if self.base_stat_multiplier is not None:
            final_base_stat_multiplier = caster.level * self.base_stat_multiplier

        return self.base_stat + final_base_stat_interval + final_base_stat_multiplier

    def resolve_effective_stat(self, caster, final_stat_recovered):
        if self.recovered_stat is RecoveredStatType.MANA:
            return caster.gain_mana(final_stat_recovered)

        elif self.recovered_stat is RecoveredStatType.HEALTH:
            return caster.gain_health(final_stat_recovered)

        elif self.recovered_stat is RecoveredStatType.FURY:
            return caster.gain_fury(final_stat_recovered)
        else:
            return 0

    def consume(self, caster, text_sprite, mixed_consumable=False):
        final_stat_recovered = self.resolve_recovered_stat(caster)
        effective_stat_recovered = self.resolve_effective_stat(caster, final_stat_recovered)
        if not mixed_consumable:
            self.consume_sound.play()
        self.display_recovered_stat(caster, effective_stat_recovered, text_sprite)

    def display_recovered_stat(self, caster, effective_stat_recovered, text_sprite):
        if self.recovered_stat is RecoveredStatType.MANA:
            damage_text.mana(caster, str(effective_stat_recovered), text_sprite)

        elif self.recovered_stat is RecoveredStatType.HEALTH:
            damage_text.heal(caster, str(effective_stat_recovered), text_sprite)

        elif self.recovered_stat is RecoveredStatType.FURY:
            damage_text.fury(caster, str(effective_stat_recovered), text_sprite)
        else:
            damage_text.hit(caster, str(effective_stat_recovered), text_sprite)
