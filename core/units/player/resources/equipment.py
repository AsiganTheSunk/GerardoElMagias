#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.equipement_items.item_categories import *
from core.items.generated_item import GeneratedItem


class EquipmentSet:
    def __init__(self):
        self.equipped_items = [
            {EquipmentSlotType.HEAD: None},
            {EquipmentSlotType.SHOULDERS: None},
            {EquipmentSlotType.CAPE: None},
            {EquipmentSlotType.GLOVES: None},
            {EquipmentSlotType.BRACERS: None},
            {EquipmentSlotType.BODY: None},
            {EquipmentSlotType.PANTS: None},
            {EquipmentSlotType.FEET: None},
            {EquipmentSlotType.BELT: None},
            {EquipmentSlotType.MAIN_HAND: None},
            {EquipmentSlotType.OFF_HAND: None},
            {EquipmentSlotType.RING: None},
            {EquipmentSlotType.RING: None},
            {EquipmentSlotType.AMULET: None},
            {EquipmentSlotType.DUAL_HAND: None},
        ]

    @staticmethod
    def get_type_from_index(slot_index):
        if slot_index == 0:
            return EquipmentSlotType.HEAD
        elif slot_index == 1:
            return EquipmentSlotType.SHOULDERS
        elif slot_index == 2:
            return EquipmentSlotType.CAPE
        elif slot_index == 3:
            return EquipmentSlotType.GLOVES
        elif slot_index == 4:
            return EquipmentSlotType.BRACERS
        elif slot_index == 5:
            return EquipmentSlotType.BODY
        elif slot_index == 6:
            return EquipmentSlotType.PANTS
        elif slot_index == 7:
            return EquipmentSlotType.FEET
        elif slot_index == 8:
            return EquipmentSlotType.BELT
        elif slot_index == 9:
            return EquipmentSlotType.MAIN_HAND
        elif slot_index == 10:
            return EquipmentSlotType.OFF_HAND
        elif slot_index == 11:
            return EquipmentSlotType.RING
        elif slot_index == 12:
            return EquipmentSlotType.RING
        elif slot_index == 13:
            return EquipmentSlotType.AMULET
        elif slot_index == 14:
            return EquipmentSlotType.DUAL_HAND

    def get_item_from_slot(self, slot_index):
        return self.equipped_items[slot_index][self.get_type_from_index(slot_index)]

    def set_item_slot(self, item, slot_index):
        if item is None or slot_index is None:
            return False
        self.equipped_items[slot_index].update({self.get_type_from_index(slot_index): item})
        return True

    def reset_slot(self, slot_index):
        return self.equipped_items[slot_index].update({self.get_type_from_index(slot_index): None})

    def is_empty_slot(self, slot_index):
        return self.equipped_items[slot_index][self.get_type_from_index(slot_index)] is None

    def resolve_off_hand_main_hand_equipment_conflicts(self, item, backpack, slot_index):
        if not self.is_empty_slot(14):
            previous_item = self.get_item_from_slot(14)
            backpack.add_item(previous_item)
            self.reset_slot(14)

        backpack.remove_item(item)
        self.set_item_slot(item, slot_index)
        return True

    def resolve_dual_equipment_conflicts(self, item, backpack, slot_index):
        if self.equipped_items[9][EquipmentSlotType.MAIN_HAND] is not None:
            previous_item = self.get_item_from_slot(9)
            backpack.add_item(previous_item)
            self.reset_slot(9)

        if self.equipped_items[10][EquipmentSlotType.OFF_HAND] is not None:
            previous_item = self.get_item_from_slot(10)
            backpack.add_item(previous_item)
            self.reset_slot(10)

        backpack.remove_item(item)
        self.set_item_slot(item, slot_index)
        return True

    def resolve_ring_equipment_conflicts(self, item, backpack):
        if self.equipped_items[11][EquipmentSlotType.RING] is None \
                and self.equipped_items[12][EquipmentSlotType.RING] is None:
            backpack.remove_item(item)
            self.set_item_slot(item, 11)
            return True

        elif self.equipped_items[11][EquipmentSlotType.RING] is not None and \
                self.equipped_items[12][EquipmentSlotType.RING] is None:
            backpack.remove_item(item)
            self.set_item_slot(item, 12)
            return True

        else:
            previous_item = self.get_item_from_slot(11)
            backpack.add_item(previous_item)
            backpack.remove_item(item)
            self.set_item_slot(item, 11)
            return True

    def resolve_equipment_conflicts(self, item, backpack, slot_index=None):
        # ItemSlotType: If Ring is Detected
        if item.item_slot_type is EquipmentSlotType.RING and slot_index is None:
            return self.resolve_ring_equipment_conflicts(item, backpack)

        elif item.item_slot_type is EquipmentSlotType.RING:
            previous_item = self.get_item_from_slot(slot_index)
            backpack.add_item(previous_item)
            backpack.remove_item(item)
            self.set_item_slot(item, slot_index)
            return True

        # ItemSlotType: If Dual is Detected and Main Hand or Off Hand is not empty
        elif item.item_slot_type is EquipmentSlotType.MAIN_HAND or item.item_slot_type is EquipmentSlotType.OFF_HAND:
            return self.resolve_off_hand_main_hand_equipment_conflicts(item, backpack, slot_index)

        # ItemSlotType: If Main Hand or Off Hand abd Dual is Detected
        elif item.item_slot_type is EquipmentSlotType.DUAL_HAND:
            return self.resolve_dual_equipment_conflicts(item, backpack, slot_index)

        else:
            # ItemSlotType: Other Items
            previous_item = self.get_item_from_slot(slot_index)
            backpack.add_item(previous_item)
            backpack.remove_item(item)
            self.set_item_slot(item, slot_index)
            return True

    def equip(self, item, backpack, slot_index):
        if item is None or slot_index is None:
            return False
        else:
            # Not Empty Slot
            if not self.is_empty_slot(slot_index):
                self.resolve_equipment_conflicts(item, backpack, slot_index)
                return True

            # Empty Slot
            elif self.is_empty_slot(slot_index):
                if item.item_slot_type is EquipmentSlotType.MAIN_HAND or \
                        item.item_slot_type is EquipmentSlotType.OFF_HAND or \
                        item.item_slot_type is EquipmentSlotType.DUAL_HAND:
                    return self.resolve_equipment_conflicts(item, backpack, slot_index)
                else:
                    backpack.remove_item(item)
                    self.set_item_slot(item, slot_index)
                    return True

    def un_equip(self, backpack, slot_index):
        if self.is_empty_slot(slot_index):
            return False
        elif not self.is_empty_slot(slot_index):
            previous_item = self.get_item_from_slot(slot_index)
            backpack.add_item(previous_item)
            self.reset_slot(slot_index)
            return True

    def list_equipment(self):
        for equipment_index, equipment_items in enumerate(self.equipped_items):
            current_equipment_item = equipment_items[self.get_type_from_index(equipment_index)]
            if current_equipment_item is not None:
                print(current_equipment_item)

    def get_stats(self):
        # Basic Attribute Stats: Strength, Dexterity, Magic, Intellect
        total_strength = 0
        total_dexterity = 0
        total_magic = 0

        # Basic Attribute Resource: Fury, Health, Mana
        total_max_fury = 0
        total_max_hp = 0
        total_max_mp = 0

        for equipment_index, equipment_items in enumerate(self.equipped_items):
            current_equipment_item = equipment_items[self.get_type_from_index(equipment_index)]
            if current_equipment_item is not None:
                total_strength += current_equipment_item.strength
                total_dexterity += current_equipment_item.dexterity
                total_magic += current_equipment_item.magic

                total_max_hp += current_equipment_item.max_hp
                total_max_mp += current_equipment_item.max_mp
                total_max_fury += current_equipment_item.max_fury

        return total_strength, total_dexterity, total_magic, total_max_hp, total_max_mp, total_max_fury
