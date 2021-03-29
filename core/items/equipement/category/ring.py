#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.equipement.constants.equipement_item_type import EquipmentItemType


class Ring:
    def __init__(self, name, item_lvl, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.RING
        self.item_slot_type = item_slot_type

        # Ring: Basic Item Attributes
