#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.affix.basic_affix import BasicAffix
from core.items.affix.constants.affix_attribute_type import AffixAttributeType
from core.items.equipement.constants.equipement_item_type import EquipmentItemType


PREFIX_ATTRIBUTE_POOL = [
    # Strength Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('Hercúleo', 1, AffixAttributeType.STRENGTH, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('Titánico', 10, AffixAttributeType.STRENGTH, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('Colosal', 20, AffixAttributeType.STRENGTH, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),



    # Magic Power Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('Brillante', 1, AffixAttributeType.MAGIC_POWER, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('Reluciente', 10, AffixAttributeType.MAGIC_POWER, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('Resplandeciente', 20, AffixAttributeType.MAGIC_POWER, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # Block Chance Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('Resistente ', 1, AffixAttributeType.BLOCK_CHANCE, 1, 4,
          [EquipmentItemType.SHIELD]),
    BasicAffix('Reforzado', 10, AffixAttributeType.BLOCK_CHANCE, 5, 8,
          [EquipmentItemType.SHIELD]),
    BasicAffix('Reforjado', 20, AffixAttributeType.BLOCK_CHANCE, 9, 12,
          [EquipmentItemType.SHIELD]),


    # Weapon Damage Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('Mortal ', 1, AffixAttributeType.MAXIMUM_WEAPON_DAMAGE, 1, 4,
          [EquipmentItemType.WEAPON]),
    BasicAffix('Fatal', 10, AffixAttributeType.MAXIMUM_WEAPON_DAMAGE, 5, 8,
          [EquipmentItemType.WEAPON]),
    BasicAffix('Letal', 20, AffixAttributeType.MAXIMUM_WEAPON_DAMAGE, 9, 12,
          [EquipmentItemType.WEAPON]),


    # %ManaLeech Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('de Langosta', 1, AffixAttributeType.MANA_LEECH, 2, 5,
          [EquipmentItemType.WEAPON]),
    BasicAffix('de Lamprea', 10, AffixAttributeType.MANA_LEECH, 6, 10,
          [EquipmentItemType.WEAPON]),
    BasicAffix('de Manáfago', 20, AffixAttributeType.MANA_LEECH, 11, 15,
          [EquipmentItemType.WEAPON]),
]



SUFFIX_ATTRIBUTE_POOL = [
    # Dexterity Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('de Macaco', 1, AffixAttributeType.DEXTERITY, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('de Mono', 10, AffixAttributeType.DEXTERITY, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('de Huron', 20, AffixAttributeType.DEXTERITY, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # Health Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('de Vida', 1, AffixAttributeType.HEALTH, 5, 15,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('de Roble', 10, AffixAttributeType.HEALTH, 16, 30,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('de Savia', 20, AffixAttributeType.HEALTH, 31, 50,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # Mana Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('de Mago', 1, AffixAttributeType.MANA, 5, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('de Brujo', 10, AffixAttributeType.MANA, 11, 25,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    BasicAffix('de Archimago', 20, AffixAttributeType.MANA, 26, 40,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # %LifeLeech Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('de Murciélago', 1, AffixAttributeType.LIFE_LEECH, 5, 12,
          [EquipmentItemType.WEAPON]),
    BasicAffix('de Vampiro', 10, AffixAttributeType.LIFE_LEECH, 12, 25,
          [EquipmentItemType.WEAPON]),
    BasicAffix('de Nosferatu', 20, AffixAttributeType.LIFE_LEECH, 25, 40,
          [EquipmentItemType.WEAPON]),


    # Armor Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('Resistente', 1, AffixAttributeType.ARMOR, 2, 6,
          [EquipmentItemType.ARMOR]),
    BasicAffix('Reforzada', 10, AffixAttributeType.ARMOR, 7, 11,
          [EquipmentItemType.ARMOR]),
    BasicAffix('Reforjada', 20, AffixAttributeType.ARMOR, 12, 18,
          [EquipmentItemType.ARMOR]),


    # Ultimate: Increase maximun hits Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    BasicAffix('Enfático', 1, AffixAttributeType.MAX_ULTIMATE_STRIKES, 1, 1,
          [EquipmentItemType.AMULET]),
    BasicAffix('Insistente', 10, AffixAttributeType.MAX_ULTIMATE_STRIKES, 2, 2,
          [EquipmentItemType.AMULET]),
    BasicAffix('Persistente', 20, AffixAttributeType.MAX_ULTIMATE_STRIKES, 3, 3,
          [EquipmentItemType.AMULET]),
]
