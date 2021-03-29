#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.basic_unit import BasicUnit


class EnemyUnit(BasicUnit):
    def __init__(self, x, y, name, level, strength, dexterity, magic):
        BasicUnit.__init__(self, x, y, name, level, strength, dexterity, magic)

        self.looted_status = False
        self.try_to_consume_health_potion = False

    def is_looted(self):
        return self.looted_status

    def update_looted_status(self):
        self.looted_status = True

    def update_try_to_consume_health_potion(self):
        self.try_to_consume_health_potion = True

    def has_tried_to_consume_health_potion(self):
        return self.try_to_consume_health_potion is False
