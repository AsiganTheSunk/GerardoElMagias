from core.items.equipement_items.item_types import *
from core.units.resources.backpack import BackPack


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
            {EquipmentSlotType.RING: None},
            {EquipmentSlotType.RING: None},
            {EquipmentSlotType.AMULET: None},
            {EquipmentSlotType.DUAL: None},
        ]

    def get_slot(self, item, slot_index=None):
        if slot_index is None:
            return self.equiped_items[self.get_index_from_type(item)][item.item_slot_type]
        return self.equiped_items[slot_index][item.item_slot_type]

    def set_slot(self, item, slot_index=None):
        if slot_index is None:
            return self.equiped_items[self.get_index_from_type(item)].update({item.item_slot_type: item})
        return self.equiped_items[slot_index].update({item.item_slot_type: item})

    def reset_slot(self, item, slot_index=None):
        if slot_index is None:
            return self.equiped_items[self.get_index_from_type(item)].update({item.item_slot_type: None})
        return self.equiped_items[slot_index].update({item.item_slot_type: None})

    def get_index_from_type(self, item):
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
        # elif item.item_slot_type is EquipmentSlotType.RING:
        #     return 12
        elif item.item_slot_type is EquipmentSlotType.AMULET:
            return 13
        elif item.item_slot_type is EquipmentSlotType.AMULET:
            return 14

    def is_empty(self, item):
        return self.equiped_items[self.get_index_from_type(item)][item.item_slot_type] is None

    def dual_equipment(self, item, backpack):
        if self.equiped_items[9][EquipmentSlotType.MAIN_HAND] is not None:
            previous_item = self.get_slot(item, 9)
            backpack.add_item(previous_item)

        if self.equiped_items[10][EquipmentSlotType.OFF_HAND] is not None:
            previous_item = self.get_slot(item, 10)
            backpack.add_item(previous_item)

        backpack.remove_item(item)
        self.set_slot(item)

    def ring_equipment(self, item, backpack, slot_index=None):
        if slot_index is None:
            if self.equiped_items[11][EquipmentSlotType.RING] is None \
                    and self.equiped_items[12][EquipmentSlotType.RING] is None:
                backpack.remove_item(item)
                self.set_slot(item, 11)

            elif self.equiped_items[11][EquipmentSlotType.RING] is not None and \
                    self.equiped_items[12][EquipmentSlotType.RING] is None:
                backpack.remove_item(item)
                self.set_slot(item, 12)
            else:
                previous_item = self.get_slot(item, 11)
                backpack.add_item(previous_item)
                backpack.remove_item(item)
                self.set_slot(item, 11)

        else:
            backpack.remove_item(item)
            backpack.add_item(item, slot_index)
            self.set_slot(item, slot_index)

    def equip(self, item, backpack, slot_index=None):
        if slot_index is None:
            if item.item_slot_type is EquipmentSlotType.RING:
                self.ring_equipment(item, backpack, slot_index)

            elif item.item_slot_type is EquipmentSlotType.DUAL:
                self.dual_equipment(item, backpack)

            elif self.is_empty(item):
                backpack.remove_item(item)
                self.set_slot(item)
            elif not self.is_empty(item):
                previous_item = self.get_slot(item)
                backpack.add_item(previous_item)
                self.set_slot(item)
        else:
                previous_item = self.get_slot(item, slot_index)
                backpack.add_item(previous_item)
                backpack.remove_item(item)
                self.set_slot(item, slot_index)

    def unequip(self, item, backpack, slot_index=None):
        if slot_index is None:
            if self.is_empty(item):
                pass
            else:
                backpack.add_item(item)
                self.reset_slot(item)
        else:
            pass

    def list_equipment(self):
        for index, item in enumerate(self.equiped_items):
            print(f'slot: {index}', item)

    def gather_bonus(self):
        pass

    def get_stats(self):
        pass

    def get_skill_modifiers(self):
        pass


from random import randint
from core.items.item_generator import ItemGenerator
from core.items.item_db.base_item_db import ITEM_POOL

level = randint(1, 30)
base_mf = 0

item_generator = ItemGenerator()
dropped_item = item_generator.get_item(level, ITEM_POOL, base_mf)

backpack = BackPack()
backpack.add_item(dropped_item)
backpack.list_items()

equipment_set = EquipmentSet()
equipment_set.list_equipment()
print('---------------'*10)
equipment_set.equip(dropped_item, backpack)
equipment_set.list_equipment()

backpack.list_items()
equipment_set.unequip(dropped_item, backpack)
equipment_set.list_equipment()
backpack.list_items()
