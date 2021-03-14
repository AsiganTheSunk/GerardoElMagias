from core.items.equipement_items.item_categories import *


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

    @staticmethod
    def get_index_from_type(item):
        if item.item_slot_type is EquipmentSlotType.HEAD:
            return 0
        elif item.item_slot_type is EquipmentSlotType.SHOULDERS:
            return 1
        elif item.item_slot_type is EquipmentSlotType.CAPE:
            return 2
        elif item.item_slot_type is EquipmentSlotType.GLOVES:
            return 3
        elif item.item_slot_type is EquipmentSlotType.BRACERS:
            return 4
        elif item.item_slot_type is EquipmentSlotType.BODY:
            return 5
        elif item.item_slot_type is EquipmentSlotType.PANTS:
            return 6
        elif item.item_slot_type is EquipmentSlotType.FEET:
            return 7
        elif item.item_slot_type is EquipmentSlotType.BELT:
            return 8
        elif item.item_slot_type is EquipmentSlotType.MAIN_HAND:
            return 9
        elif item.item_slot_type is EquipmentSlotType.OFF_HAND:
            return 10
        elif item.item_slot_type is EquipmentSlotType.RING:
            return 11
        elif item.item_slot_type is EquipmentSlotType.RING:
            # This is never going to run, in the current state of the equipment set
            pass
        elif item.item_slot_type is EquipmentSlotType.AMULET:
            return 13
        elif item.item_slot_type is EquipmentSlotType.DUAL_HAND:
            return 14

    def get_item_from_slot(self, slot_index):
        return self.equipped_items[slot_index][self.get_type_from_index(slot_index)]

    def set_item_slot(self, item, slot_index=None):
        if item is None:
            return False
        elif slot_index is None:
            self.equipped_items[self.get_index_from_type(item)].update({item.item_slot_type: item})
            return True
        else:
            self.equipped_items[slot_index].update({self.get_type_from_index(slot_index): item})
            return True

    def reset_slot(self, slot_index):
        return self.equipped_items[slot_index].update({self.get_type_from_index(slot_index): None})

    def is_empty_slot(self, item, slot_index=None):
        if slot_index is None:
            return self.equipped_items[self.get_index_from_type(item)][item.item_slot_type] is None
        else:
            return self.equipped_items[slot_index][self.get_type_from_index(slot_index)] is None

    def resolve_off_hand_main_hand_equipment_conflicts(self, item, backpack):
        if not self.is_empty_slot(None, 14):
            previous_item = self.get_item_from_slot(14)
            backpack.add_item(previous_item)
            self.reset_slot(14)

        backpack.remove_item(item)
        self.set_item_slot(item)
        return True

    def resolve_dual_equipment_conflicts(self, item, backpack):
        if self.equipped_items[9][EquipmentSlotType.MAIN_HAND] is not None:
            previous_item = self.get_item_from_slot(9)
            backpack.add_item(previous_item)
            self.reset_slot(9)

        if self.equipped_items[10][EquipmentSlotType.OFF_HAND] is not None:
            previous_item = self.get_item_from_slot(10)
            backpack.add_item(previous_item)
            self.reset_slot(10)

        backpack.remove_item(item)
        self.set_item_slot(item)
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
        if item.item_slot_type is EquipmentSlotType.RING:
            return self.resolve_ring_equipment_conflicts(item, backpack)

        elif item.item_slot_type is EquipmentSlotType.RING and slot_index is not None:
            previous_item = self.get_item_from_slot(slot_index)
            backpack.add_item(previous_item)
            backpack.remove_item(item)
            self.set_item_slot(item)
            return True

        # ItemSlotType: If Dual is Detected and Main Hand or Off Hand is not empty
        elif item.item_slot_type is EquipmentSlotType.MAIN_HAND or item.item_slot_type is EquipmentSlotType.OFF_HAND:
            return self.resolve_off_hand_main_hand_equipment_conflicts(item, backpack)

        # ItemSlotType: If Main Hand or Off Hand abd Dual is Detected
        elif item.item_slot_type is EquipmentSlotType.DUAL_HAND:
            return self.resolve_dual_equipment_conflicts(item, backpack)

        else:
            # ItemSlotType: Other Items
            previous_item = self.get_item_from_slot(self.get_index_from_type(item))
            backpack.add_item(previous_item)
            backpack.remove_item(item)
            self.set_item_slot(item)
            return True

    def equip(self, item, backpack, slot_index=None):
        if item is not None:
            # Not Empty Slot and SlotIndex is None
            if not self.is_empty_slot(item) and slot_index is None:
                self.resolve_equipment_conflicts(item, backpack)
                return True

            # Not Empty Slot and Slot Index is not None
            elif not self.is_empty_slot(item) and slot_index is not None:
                self.resolve_equipment_conflicts(item, backpack, slot_index)
                return True

            # Empty Slot and Slot Index is not None
            elif self.is_empty_slot(item) and slot_index is not None:
                backpack.remove_item(item)
                self.set_item_slot(item, slot_index)
                return True

            # Empty Slot and Slot Index is None
            elif self.is_empty_slot(item) and slot_index is None:
                if item.item_slot_type is EquipmentSlotType.MAIN_HAND or \
                        item.item_slot_type is EquipmentSlotType.OFF_HAND or \
                        item.item_slot_type is EquipmentSlotType.RING or \
                        item.item_slot_type is EquipmentSlotType.DUAL_HAND:
                    self.resolve_equipment_conflicts(item, backpack)
                    return True

                else:
                    backpack.remove_item(item)
                    self.set_item_slot(item)
                    return True
        return False

    def un_equip(self, backpack, slot_index):
        if self.is_empty_slot(None, slot_index):
            return False
        elif not self.is_empty_slot(None, slot_index):
            previous_item = self.get_item_from_slot(slot_index)
            backpack.add_item(previous_item)
            self.reset_slot(slot_index)
            return True

    def list_equipment(self):
        for index, item in enumerate(self.equipped_items):
            print(f'slot: {index}', item)

    def gather_bonus(self):
        pass

    def get_stats(self):
        pass

    def get_skill_modifiers(self):
        pass
