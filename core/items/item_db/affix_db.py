from core.items.affix_system.affix_type import Affix
from core.items.affix_system.affix_category import *
from core.items.equipement_items.item_categories import *



PREFIX_ATTRIBUTE_POOL = [
    # Strength Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Hercúleo', 1, AttributeType.STRENGTH, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('Titánico', 10, AttributeType.STRENGTH, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('Colosal', 20, AttributeType.STRENGTH, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),



    # Magic Power Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Brillante', 1, AttributeType.MAGIC_POWER, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('Reluciente', 10, AttributeType.MAGIC_POWER, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('Resplandeciente', 20, AttributeType.MAGIC_POWER, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # Block Chance Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Resistente ', 1, AttributeType.BLOCK_CHANCE, 1, 4,
          [EquipmentItemType.SHIELD]),
    Affix('Reforzado', 10, AttributeType.BLOCK_CHANCE, 5, 8,
          [EquipmentItemType.SHIELD]),
    Affix('Reforjado', 20, AttributeType.BLOCK_CHANCE, 9, 12,
          [EquipmentItemType.SHIELD]),


    # Weapon Damage Prefix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Mortal ', 1, AttributeType.MAXIMUM_WEAPON_DAMAGE, 1, 4,
          [EquipmentItemType.WEAPON]),
    Affix('Fatal', 10, AttributeType.MAXIMUM_WEAPON_DAMAGE, 5, 8,
          [EquipmentItemType.WEAPON]),
    Affix('Letal', 20, AttributeType.MAXIMUM_WEAPON_DAMAGE, 9, 12,
          [EquipmentItemType.WEAPON]),


    # %ManaLeech Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Langosta', 1, AttributeType.MANA_LEECH, 2, 5,
          [EquipmentItemType.WEAPON]),
    Affix('de Lamprea', 10, AttributeType.MANA_LEECH, 6, 10,
          [EquipmentItemType.WEAPON]),
    Affix('de Manáfago', 20, AttributeType.MANA_LEECH, 11, 15,
          [EquipmentItemType.WEAPON]),
]



SUFFIX_ATTRIBUTE_POOL = [
    # Dexterity Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Macaco', 1, AttributeType.DEXTERITY, 1, 3,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('de Mono', 10, AttributeType.DEXTERITY, 4, 6,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('de Huron', 20, AttributeType.DEXTERITY, 7, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # Health Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Vida', 1, AttributeType.HEALTH, 5, 15,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('de Roble', 10, AttributeType.HEALTH, 16, 30,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('de Savia', 20, AttributeType.HEALTH, 31, 50,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # Mana Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Mago', 1, AttributeType.MANA, 5, 10,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('de Brujo', 10, AttributeType.MANA, 11, 25,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),
    Affix('de Archimago', 20, AttributeType.MANA, 26, 40,
          [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD, EquipmentItemType.RING, EquipmentItemType.AMULET]),


    # %LifeLeech Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('de Murciélago', 1, AttributeType.LIFE_LEECH, 5, 12,
          [EquipmentItemType.WEAPON]),
    Affix('de Vampiro', 10, AttributeType.LIFE_LEECH, 12, 25,
          [EquipmentItemType.WEAPON]),
    Affix('de Nosferatu', 20, AttributeType.LIFE_LEECH, 25, 40,
          [EquipmentItemType.WEAPON]),


    # Armor Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Resistente', 1, AttributeType.ARMOR, 2, 6,
          [EquipmentItemType.ARMOR]),
    Affix('Reforzada', 10, AttributeType.ARMOR, 7, 11,
          [EquipmentItemType.ARMOR]),
    Affix('Reforjada', 20, AttributeType.ARMOR, 12, 18,
          [EquipmentItemType.ARMOR]),


    # Ultimate: Increase maximun hits Suffix: Name, Item Level, Attribute Type, Minimum Attribute, Maximum Attribute, Allowed Item Type
    Affix('Enfático', 1, AttributeType.MAX_ULTIMATE_STRIKES, 1, 1,
          [EquipmentItemType.AMULET]),
    Affix('Insistente', 10, AttributeType.MAX_ULTIMATE_STRIKES, 2, 2,
          [EquipmentItemType.AMULET]),
    Affix('Persistente', 20, AttributeType.MAX_ULTIMATE_STRIKES, 3, 3,
          [EquipmentItemType.AMULET]),
]
