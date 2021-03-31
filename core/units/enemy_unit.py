#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.units.basic_unit import BasicUnit
from core.units.basic_enemy_unit import BasicEnemyUnit


class EnemyUnit(BasicUnit, BasicEnemyUnit):
    def __init__(self, name, level, attack_power, attack_rating, magic_power, max_hp, max_mp):
        BasicUnit.__init__(self)
        BasicEnemyUnit.__init__(self, 0, 0, name, level, attack_power, attack_rating, magic_power)

        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mp = max_mp
        self.current_mp = self.max_mp

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
