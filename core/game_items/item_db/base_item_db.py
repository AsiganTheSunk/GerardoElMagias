from core.game_items.equipement_items.item_categories import *
from core.game_items.equipement_items.item_types import *

ITEM_POOL = {
    # Shield Attributes: Name, Shield Type, Shield Sub Type, Block Chance, Item Level
    # Required: to have at least 1 lvl item, otherwise it fails to level <= item_level
    EquipmentItemType.SHIELD: [
        Shield('Rodela', 1, 20),
        Shield('Defensor', 7, 25),
        Shield('Aegis', 13, 30),
        Shield('Guardian', 17, 35),
        Shield("Escudo forjado en el infierno", 25, 45)
    ],

    # Armor Attributes: Name, Armor Type, Armor Sub Type, Defense, Item Level
    # Required: to have at least 1 lvl item, otherwise it fails to level <= item_level
    EquipmentItemType.ARMOR: [
        Armor('Harapos', 1, 1),
        Armor('Armadura de cuero', 4, 5),
        Armor('Coraza', 8, 10),
        Armor('Cota de malla', 12, 15),
        Armor('Piel de balrog', 16, 20),
        Armor('Armadura forjada en el infierno', 25, 30)
    ],

    # Weapon Attributes: Name, Weapon Type, Weapon Sub Type, Item Level, Minimum Damage, Maximum Damage
    # Required: to have at least 1 lvl item, otherwise it fails to level <= item_level
    EquipmentItemType.WEAPON: [
        MeleeWeapon('Puñal', 'Espada', 1, 2, 1),
        MeleeWeapon("Daga", "Espada", 1, 1, 4),
        MeleeWeapon("Espada corta", "Espada", 3, 2, 5),
        MeleeWeapon("Lanza", "Lanza", 3, 1, 6),
        MeleeWeapon("Espada larga", "Espada", 5, 3, 6),
        MeleeWeapon("Pica", "Lanza", 5, 2, 7),
        MeleeWeapon("Hacha", "Hacha", 8, 3, 8),
        MeleeWeapon("Espada bastarda", "Espada", 10, 6, 9),
        MeleeWeapon("Hacha doble", "Hacha", 10, 3, 10),
        MeleeWeapon("Látigo", "Látigo", 12, 1, 15),
        MeleeWeapon("Alabarda", "Lanza", 12, 5, 11),
        MeleeWeapon("Gladius", "Espada", 14,  8, 12),
        MeleeWeapon("Partisana", "Lanza", 14, 5, 14),
        MeleeWeapon("Mandoble", "Espada", 16, 9, 13),
        MeleeWeapon("Decapitador", "Hacha", 16, 6, 15),
        MeleeWeapon("Espada forjada en el infierno", "Espada", 25, 12, 18)
    ],

    # Amulet Attributes: Name
    EquipmentItemType.AMULET: [
        Amulet("Amulet", 1)
    ],

    # Ring Attributes: Name
    EquipmentItemType.RING: [
        Ring("Ring", 1)
    ]
}
