#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.basic_unit import BasicUnit


class EnemyUnit(BasicUnit):
    def __init__(self, x, y, name, level, strength, dexterity, magic):
        BasicUnit.__init__(self, x, y, name, level, strength, dexterity, magic)
        self.looted_status = False

    def is_looted(self):
        return self.looted_status

    def update_looted_status(self):
        self.looted_status = True
