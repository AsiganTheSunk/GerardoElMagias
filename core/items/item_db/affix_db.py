from core.items.affix_system.affix_type import Affix
from core.items.affix_system.affix_category import *
from core.items.equipement_items.item_categories import *

PREFIX_ATTRIBUTE_POOL = [
    # Strength Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Cruel', 1, AttributeType.STRENGTH, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
    Affix('Bestial', 10, AttributeType.STRENGTH, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
    Affix('Mortal', 20, AttributeType.STRENGTH, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),

    # Magic Power Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Brillante', 1, AttributeType.MAGIC_POWER, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('Reluciente', 10, AttributeType.MAGIC_POWER, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('Resplandeciente', 20, AttributeType.MAGIC_POWER, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
]

SUFFIX_ATTRIBUTE_POOL = [
    # Dexterity Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('del Macaco', 1, AttributeType.DEXTERITY, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
    Affix('del Mono', 10, AttributeType.DEXTERITY, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
    Affix('del Huron', 20, AttributeType.DEXTERITY, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),

    # Health Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Vida', 1, AttributeType.HEALTH, 5, 15,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('del Titan', 10, AttributeType.HEALTH, 16, 30,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('del Matusalén', 20, AttributeType.HEALTH, 31, 50,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),

    # Mana Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Mago', 1, AttributeType.MANA, 5, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
    Affix('de Brujo', 10, AttributeType.MANA, 11, 25,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
    Affix('de Merlín', 20, AttributeType.MANA, 26, 40,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD]),
]
