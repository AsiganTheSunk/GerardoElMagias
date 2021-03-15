from core.items.equipement_items.item_categories import *
from core.items.equipement_items.item_types import *


ITEM_POOL = {
    # Shield Attributes: Name, Shield Type, Shield Sub Type, Block Chance, Item Level
    # Required: to have at least 1 lvl item, otherwise it fails to level <= item_level
    EquipmentItemType.SHIELD: [
        Shield('Rodela', 1, 20, EquipmentSlotType.OFF_HAND),
        Shield('Defensor', 7, 25, EquipmentSlotType.OFF_HAND),
        Shield('Aegis', 13, 30, EquipmentSlotType.OFF_HAND),
        Shield('Guardian', 17, 35, EquipmentSlotType.OFF_HAND),
        Shield("Escudo forjado en el infierno", 25, 45, EquipmentSlotType.OFF_HAND)
    ],

    # Armor Attributes: Name, Armor Type, Armor Sub Type, Defense, Item Level
    # Required: to have at least 1 lvl item, otherwise it fails to level <= item_level
    EquipmentItemType.ARMOR: [
        Armor('Harapos', 1, 1, EquipmentSlotType.BODY),
        Armor('Armadura de cuero', 4, 5, EquipmentSlotType.BODY),
        Armor('Coraza', 8, 10, EquipmentSlotType.BODY),
        Armor('Cota de malla', 12, 15, EquipmentSlotType.BODY),
        Armor('Piel de balrog', 16, 20, EquipmentSlotType.BODY),
        Armor('Armadura forjada en el infierno', 25, 30, EquipmentSlotType.BODY)
    ],

    # Weapon Attributes: Name, Weapon Type, Weapon Sub Type, Item Level, Minimum Damage, Maximum Damage
    # Required: to have at least 1 lvl item, otherwise it fails to level <= item_level
    EquipmentItemType.WEAPON: [
        MeleeWeapon('Puñal', 'Espada', 1, 2, 1, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Daga", "Espada", 1, 1, 4, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Espada corta", "Espada", 3, 2, 5, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Lanza", "Lanza", 3, 1, 6, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Espada larga", "Espada", 5, 3, 6, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Pica", "Lanza", 5, 2, 7, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Hacha", "Hacha", 8, 3, 8, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Espada bastarda", "Espada", 10, 6, 9, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Hacha doble", "Hacha", 10, 3, 10, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Látigo", "Látigo", 12, 1, 15, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Alabarda", "Lanza", 12, 5, 11, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Gladius", "Espada", 14,  8, 12, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Partisana", "Lanza", 14, 5, 1, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Mandoble", "Espada", 16, 9, 13, EquipmentSlotType.DUAL_HAND),
        MeleeWeapon("Decapitador", "Hacha", 16, 6, 15, EquipmentSlotType.MAIN_HAND),
        MeleeWeapon("Espada forjada en el infierno", "Espada", 25, 12, 18, EquipmentSlotType.MAIN_HAND)
    ],

    # Amulet Attributes: Name
    EquipmentItemType.AMULET: [
        Amulet("Amulet", 1, EquipmentSlotType.AMULET)
    ],

    # Ring Attributes: Name
    EquipmentItemType.RING: [
        Ring("Ring", 1, EquipmentSlotType.RING)
    ]
}
