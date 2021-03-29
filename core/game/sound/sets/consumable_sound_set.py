#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ConsumableSounds:
    def __init__(self, sounds):
        self.consume_health_potion = sounds['fx']['items']['health_potion']
        self.consume_mana_potion = sounds['fx']['items']['health_potion']
        self.consume_drink = sounds['fx']['items']['drink']
        self.consume_food = sounds['fx']['items']['eat']