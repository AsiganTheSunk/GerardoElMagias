#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.equipement.constants.equipement_item_type import EquipmentItemType


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
