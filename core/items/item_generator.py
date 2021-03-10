from random import randint, choice, sample

from core.items.equipement_items.item_categories import *
from core.items.equipement_items.item_types import *
from core.items.affix_system.affix_type import *
from core.items.affix_system.affix_category import *

from core.items.item_db.base_item_db import *
from core.items.item_db.affix_db import *
from core.items.generated_item import GeneratedItem

class ItemGenerator:
    @staticmethod
    def roll_item_type():
        return choice(list(EquipmentItemType))

    @staticmethod
    def roll_unique(normalized_magic_find):
        return randint(1, 100) < 3 * normalized_magic_find

    @staticmethod
    def roll_rare(normalized_magic_find):
        return randint(1, 100) < 8 * normalized_magic_find

    @staticmethod
    def roll_magical(normalized_magic_find):
        return randint(1, 100) < 20 * normalized_magic_find

    @staticmethod
    def normalize_magic_find(magic_find):
        return 1 + (magic_find / 100)

    def get_rarity(self, magic_find):
        normalized_magic_find = self.normalize_magic_find(magic_find)

        if self.roll_unique(normalized_magic_find):
            return ItemRarity.UNIQUE
        if self.roll_rare(normalized_magic_find):
            return ItemRarity.RARE
        if self.roll_magical(normalized_magic_find):
            return ItemRarity.MAGICAL
        return ItemRarity.COMMON

    @staticmethod
    def get_base_item(item_type, item_level, base_item_pool):
        drop_item_pool = []
        for base_item in base_item_pool[item_type]:
            if base_item.item_lvl <= item_level:
                drop_item_pool.append(base_item)
        return choice(list(drop_item_pool))

    @staticmethod
    def get_base_prefix_suffix_number(item_rarity):
        if item_rarity is ItemRarity.COMMON:
            return 0, 0
        if item_rarity is ItemRarity.MAGICAL:
            return 1, 1
        if item_rarity is ItemRarity.RARE:
            return 2, 2
        if item_rarity is ItemRarity.UNIQUE:
            return 0, 0

    def get_item(self, item_level, item_pool, magic_find):
        equipment_item_type = self.roll_item_type()
        equipment_rarity_type = self.get_rarity(magic_find)
        equipment_base_item = self.get_base_item(equipment_item_type, item_level, item_pool)
        equipment_prefix_list, equipment_suffix_list = self.get_affixes(item_level, equipment_item_type, equipment_rarity_type)
        return GeneratedItem(equipment_base_item, equipment_item_type, equipment_rarity_type, equipment_prefix_list, equipment_suffix_list)

    def get_affixes(self, item_level, item_type, item_rarity):
        equipment_prefix_number, equipment_suffix_number = self.get_base_prefix_suffix_number(item_rarity)
        equipment_prefix_list = self.get_prefix(item_level, item_type, equipment_prefix_number)
        equipment_suffix_list = self.get_suffix(item_level, item_type, equipment_suffix_number)
        return equipment_prefix_list, equipment_suffix_list

    @staticmethod
    def get_suffix(item_level, item_type, equipment_suffix_number):
        equipment_suffix_list = []
        final_equipment_suffix_list = []

        if equipment_suffix_number > 0:
            for index in range(equipment_suffix_number):
                for suffix_item in SUFFIX_ATTRIBUTE_POOL:
                    if (suffix_item.item_level <= item_level) and (item_type in suffix_item.allowed_item_type):
                        equipment_suffix_list.append(suffix_item)

                # print(equipment_suffix_list, item_level, item_type, equipment_suffix_number)
                final_equipment_suffix_list.append(choice(equipment_suffix_list))
        return final_equipment_suffix_list

    @staticmethod
    def get_prefix(item_level, item_type, equipment_prefix_number):
        equipment_prefix_list = []
        final_equipment_prefix_list = []

        if equipment_prefix_number > 0:
            for index in range(equipment_prefix_number):
                for prefix_item in PREFIX_ATTRIBUTE_POOL:
                    if (prefix_item.item_level <= item_level) and (item_type in prefix_item.allowed_item_type):
                        equipment_prefix_list.append(prefix_item)
                final_equipment_prefix_list.append(choice(equipment_prefix_list))
        return final_equipment_prefix_list


level = randint(1, 30)
base_mf = 0


item_generator = ItemGenerator()
dropped_item = item_generator.get_item(level, ITEM_POOL, base_mf)
print(dropped_item)
