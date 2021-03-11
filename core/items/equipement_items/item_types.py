from core.items.equipement_items.item_categories import *


class Shield:
    def __init__(self, name, item_lvl, block_chance, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.SHIELD
        self.item_slot_type = item_slot_type

        # Shield: Basic Item Attributes
        self.block_chance = block_chance


class MeleeWeapon:
    def __init__(self, name, weapon_subclass, item_lvl, minimum_damage, maximum_damage, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.WEAPON
        self.item_slot_type = item_slot_type

        # Melee Weapon: Basic Item Attributes
        self.weapon_subclass = weapon_subclass
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage


class Armor:
    def __init__(self, name, item_lvl, armor, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.ARMOR
        self.item_slot_type = item_slot_type

        # Armor: Basic Item Attributes
        self.armor = armor


class Amulet:
    def __init__(self, name, item_lvl, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.AMULET
        self.item_slot_type = item_slot_type

        # Amulet: Basic Item Attributes


class Ring:
    def __init__(self, name, item_lvl, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.AMULET
        self.item_slot_type = item_slot_type

        # Ring: Basic Item Attributes
