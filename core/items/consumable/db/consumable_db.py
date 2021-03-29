#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.consumable.basic_consumable import BasicConsumable
from core.items.consumable.mixed_consumable import MixedConsumable
from core.items.consumable.constants.recovered_stat_type import RecoveredStatType


# Base Potions
HEALTH_POTION = BasicConsumable('Health Potion', RecoveredStatType.HEALTH, 40, 10, 4)
MANA_POTION = BasicConsumable('Mana Potion', RecoveredStatType.MANA, 15, 5, 2)
FURY_POTION = BasicConsumable('Fury Potion', RecoveredStatType.FURY, 20, 5, None)

# Mixed Potions
REJUVENATION_POTION = MixedConsumable('Rejuvenation Potion', [HEALTH_POTION, MANA_POTION])


# Basic Consumables
BREAD = BasicConsumable('Bread', RecoveredStatType.HEALTH, 30, None, None)
DRINK = BasicConsumable('Drink', RecoveredStatType.MANA, 10, None, None)

LARGE_BREAD = BasicConsumable('Large Bread', RecoveredStatType.HEALTH, 60, None, None)
LARGE_DRINK = BasicConsumable('Large Drink', RecoveredStatType.MANA, 20, None, None)
