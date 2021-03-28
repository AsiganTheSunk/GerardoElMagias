#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.equipement.constants.equipement_item_type import EquipmentItemType


class Amulet:
    def __init__(self, name, item_lvl, item_slot_type):
        self.name = name
        self.item_lvl = item_lvl
        self.item_type = EquipmentItemType.AMULET
        self.item_slot_type = item_slot_type
