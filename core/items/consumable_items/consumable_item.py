from random import randint
from enum import Enum
from core.text.damage_text import DamageText

# Init: Damage Text
damage_text = DamageText()


class RecoveredStat(Enum):
    MANA = 'Mana'
    FURY = 'Fury'
    HEALTH = 'Health'


class MixedConsumableItem:
    def __init__(self, name, consumable_items, consume_sound):
        self.name = name
        self.consumable_items = consumable_items
        self.consume_sound = consume_sound

    def consume(self, caster, text_sprite):
        for consumable_item in self.consumable_items:
            consumable_item.consume(caster, text_sprite, True)
        self.consume_sound.play()


class ConsumableItem:
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
        if self.recovered_stat is RecoveredStat.MANA:
            return caster.gain_mana(final_stat_recovered)

        elif self.recovered_stat is RecoveredStat.HEALTH:
            return caster.gain_health(final_stat_recovered)

        elif self.recovered_stat is RecoveredStat.FURY:
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
        if self.recovered_stat is RecoveredStat.MANA:
            damage_text.mana(caster, str(effective_stat_recovered), text_sprite)

        elif self.recovered_stat is RecoveredStat.HEALTH:
            damage_text.heal(caster, str(effective_stat_recovered), text_sprite)

        elif self.recovered_stat is RecoveredStat.FURY:
            damage_text.fury(caster, str(effective_stat_recovered), text_sprite)
        else:
            damage_text.hit(caster, str(effective_stat_recovered), text_sprite)
