#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.equipement.constants.equipement_item_type import EquipmentItemType


class Shield:
    def __init__(self, name, item_lvl, block_chance, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.SHIELD
        self.item_slot_type = item_slot_type

        # Shield: Basic Item Attributes
        self.block_chance = block_chance

