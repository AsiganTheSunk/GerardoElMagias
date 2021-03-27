from core.items.consumable_items.consumable_item import ConsumableItem
from core.items.consumable_items.mixed_consumable_item import MixedConsumableItem
from core.items.consumable_items.consumable_item import RecoveredStatType
from constants.sound import health_potion_sound, eat_sound, drink_sound


# Base Potions
HEALTH_POTION = ConsumableItem('Health Potion', RecoveredStatType.HEALTH, 40, 10, 4, health_potion_sound)
MANA_POTION = ConsumableItem('Mana Potion', RecoveredStatType.MANA, 15, 5, 2, health_potion_sound)
FURY_POTION = ConsumableItem('Fury Potion', RecoveredStatType.FURY, 20, 5, None, health_potion_sound)

# Mixed Potions
REJUVENATION_POTION = MixedConsumableItem('Rejuvenation Potion', [HEALTH_POTION, MANA_POTION], health_potion_sound)


# Basic Consumables
BREAD = ConsumableItem('Bread', RecoveredStatType.HEALTH, 30, None, None, eat_sound)
DRINK = ConsumableItem('Drink', RecoveredStatType.MANA, 10, None, None, drink_sound)

LARGE_BREAD = ConsumableItem('Large Bread', RecoveredStatType.HEALTH, 60, None, None, eat_sound)
LARGE_DRINK = ConsumableItem('Large Drink', RecoveredStatType.MANA, 20, None, None, drink_sound)
