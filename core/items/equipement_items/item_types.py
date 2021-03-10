from core.items.equipement_items.item_categories import *


class Shield:
    def __init__(self, name, item_lvl, block_chance):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.SHIELD

        # Shield: Basic Item Attributes
        self.block_chance = block_chance


class MeleeWeapon:
    def __init__(self, name, weapon_subclass, item_lvl, minimum_damage, maximum_damage):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.WEAPON

        # Melee Weapon: Basic Item Attributes
        self.weapon_subclass = weapon_subclass
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage


class Armor:
    def __init__(self, name, item_lvl, armor):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.ARMOR

        # Armor: Basic Item Attributes
        self.armor = armor


class Amulet:
    def __init__(self, name, item_lvl):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.AMULET

        # Amulet: Basic Item Attributes


class Ring:
    def __init__(self, name, item_lvl):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.AMULET

        # Ring: Basic Item Attributes

