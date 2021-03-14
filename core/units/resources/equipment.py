from core.items.equipement_items.item_categories import *


class EquipmentSet:
    def __init__(self):
        self.equiped_items = [
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
            {EquipmentSlotType.RING_0: None},
            {EquipmentSlotType.RING_1: None},
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
            return  EquipmentSlotType.GLOVES
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
        elif item.item_slot_type is EquipmentSlotType.AMULET:
            return 14

    def get_item_from_slot(self, slot_index):
        return self.equiped_items[slot_index][self.get_type_from_index(slot_index)]

    def set_item_slot(self, item, slot_index=None):
        if item is None:
            return False
        elif slot_index is None:
            self.equiped_items[self.get_index_from_type(item)].update({item.item_slot_type: item})
            return True
        else:
            self.equiped_items[slot_index].update({self.get_type_from_index(slot_index): item})
            return True

    def reset_slot(self, slot_index):
        return self.equiped_items[slot_index].update({self.get_type_from_index(slot_index): None})

    def is_empty_slot(self, item, slot_index=None):
        if  item is not None and slot_index is None:
            return self.equiped_items[self.get_index_from_type(item)][item.item_slot_type] is None
        else:
            return self.equiped_items[slot_index][self.get_type_from_index(slot_index)] is None

    def dual_un_equipment(self, item, backpack):
        if not self.is_empty_slot(None, 14):
            backpack.add_item(item)
            self.reset_slot(14)

        backpack.remove_item(item)
        self.set_item_slot(item)

    def dual_equipment(self, item, backpack):
        if self.equiped_items[9][EquipmentSlotType.MAIN_HAND] is not None:
            previous_item = self.get_item_from_slot(9)
            backpack.add_item(previous_item)

        if self.equiped_items[10][EquipmentSlotType.OFF_HAND] is not None:
            previous_item = self.get_item_from_slot(10)
            backpack.add_item(previous_item)

        backpack.remove_item(item)
        self.set_item_slot(item, 14)

    def ring_equipment(self, item, backpack, slot_index=None):
        if slot_index is None:
            if self.equiped_items[11][EquipmentSlotType.RING] is None \
                    and self.equiped_items[12][EquipmentSlotType.RING] is None:
                backpack.remove_item(item)
                self.set_item_slot(item, 11)

            elif self.equiped_items[11][EquipmentSlotType.RING] is not None and \
                    self.equiped_items[12][EquipmentSlotType.RING] is None:
                backpack.remove_item(item)
                self.set_item_slot(item, 12)
            else:
                previous_item = self.get_item_from_slot(11)
                backpack.add_item(previous_item)
                backpack.remove_item(item)
                self.set_item_slot(item, 11)

        else:
            backpack.remove_item(item)
            backpack.add_item(item, slot_index)
            self.set_item_slot(item, slot_index)

    def equip(self, item, backpack, slot_index=None):
        if item is None:
            return False

        elif not self.is_empty_slot(item) and slot_index is None:
            # State: If Ring is Detected
            if item.item_slot_type is EquipmentSlotType.RING:
                self.ring_equipment(item, backpack, slot_index)

            # State: If Dual is Detected and Main Hand or Off Hand is not empty
            elif item.item_slot_type is EquipmentSlotType.MAIN_HAND or item.item_slot_type is EquipmentSlotType.OFF_HAND:
                self.dual_un_equipment(item, backpack)

            elif item.item_slot_type is EquipmentSlotType.DUAL_HAND:
                self.dual_equipment(item, backpack)

            else:
                previous_item = self.get_item_from_slot(self.get_index_from_type(item.item_slot_type))
                backpack.add_item(previous_item)
                self.set_item_slot(item)

        else:
            pass
            # previous_item = self.get_item_from_slot(item, slot_index)
            # backpack.add_item(previous_item)
            # backpack.remove_item(item)
            # self.set_item_slot(item, slot_index)
            # return True

            # elif self.is_empty_slot(item):
            # backpack.remove_item(item)
            # self.set_slot(item)
            # return True
    #
    # def un_equip(self, item, backpack, slot_index=None):
    #     if item is None and slot_index is None:
    #         return False
    #     if slot_index is None:
    #         if not self.is_empty_slot(item):
    #             backpack.add_item(item)
    #             self.reset_slot(item)
    #             return True
    #         else:
    #             return False
    #     else:
    #         backpack.add_item(item)
    #         self.reset_slot(item, slot_index)
    #         return True

    def list_equipment(self):
        for index, item in enumerate(self.equiped_items):
            print(f'slot: {index}', item)

    def gather_bonus(self):
        pass

    def get_stats(self):
        pass

    def get_skill_modifiers(self):
        pass

