#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.text.damage_text import DamageText


# Init: Damage Text
damage_text = DamageText()


class MixedConsumable:
    def __init__(self, name, consumable_items, consume_sound):
        self.name = name
        self.consumable_items = consumable_items
        self.consume_sound = consume_sound

    def consume(self, caster, text_sprite):
        for consumable_item in self.consumable_items:
            consumable_item.consume(caster, text_sprite, True)
        self.consume_sound.play()
