#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.affix.constants.affix_attribute_type import AffixAttributeType
from core.items.equipement.constants.equipement_item_type import EquipmentItemType


class GeneratedItem:
    def __init__(self, base_item, item_type, item_rarity, item_prefix_list, item_suffix_list):
        self.base_item = base_item
        self.item_type = item_type
        self.item_rarity = item_rarity
        self.item_prefix_list = item_prefix_list
        self.item_suffix_list = item_suffix_list
        self.item_slot_type = self.base_item.item_slot_type

        # Basic Attribute Resource: Fury, Health, Mana
        self.max_fury = 0
        self.max_hp = 0
        self.max_mp = 0

        # Basic Attribute Stats: Strength, Dexterity, Magic, Intellect
        self.strength = 0
        self.dexterity = 0
        self.magic = 0

        self.unpack_prefix_stats()
        self.unpack_suffix_stats()

    def __str__(self):
        return f'{self.unpack_item_data()}' \
               f'Item Rarity: {self.item_rarity.value}\n' \
               f'Item Type: {self.item_type.value}\n' \
               f'{self.get_prefix_str_stats()}' \
               f'{self.get_suffix_str_stats()}' \
               f'Strength: {self.strength} \n' \
               f'Dexterity: {self.dexterity} \n' \
               f'Magic Power: {self.magic} \n' \
               f'Max Health: {self.max_hp} \n' \
               f'Max Mana: {self.max_mp} \n' \
               f'Max Fury: {self.max_fury} \n' \


    def get_item_name(self):
        composed_item_name = ''
        composed_item_name += self.base_item.name + ' '
        if self.item_prefix_list:
            for index, prefix_item in enumerate(self.item_prefix_list):
                composed_item_name += f'{prefix_item.name} '

        if self.item_suffix_list:
            for index, suffix_item in enumerate(self.item_suffix_list):
                composed_item_name += f'{suffix_item.name} '

        return composed_item_name

    def set_stats(self, attribute_type, attribute_value):
        if attribute_type == AffixAttributeType.STRENGTH.value:
            self.strength = self.strength + attribute_value
        elif attribute_type == AffixAttributeType.DEXTERITY.value:
            self.dexterity = self.dexterity + attribute_value
        elif attribute_type == AffixAttributeType.MAGIC_POWER.value:
            self.magic = self.magic + attribute_value
        elif attribute_type == AffixAttributeType.HEALTH.value:
            self.max_hp = self.max_hp + attribute_value
        elif attribute_type == AffixAttributeType.MANA.value:
            self.max_mp = self.max_mp + attribute_value
        elif attribute_type == AffixAttributeType.FURY.value:
            self.max_fury = self.max_fury + attribute_value

    def get_prefix_str_stats(self):
        unpack_prefix = ''
        if self.item_prefix_list:
            for index, prefix_item in enumerate(self.item_prefix_list):
                unpack_prefix += f'Prefix [{index}]: {prefix_item.name}, {prefix_item.attribute_type.value}, {prefix_item.attribute_value}\n'
            return unpack_prefix
        return unpack_prefix

    def get_suffix_str_stats(self):
        unpack_suffix = ''
        if self.item_suffix_list:
            for index, suffix_item in enumerate(self.item_suffix_list):
                unpack_suffix += f'Suffix [{index}]: {suffix_item.name}, {suffix_item.attribute_type.value}, {suffix_item.attribute_value}\n'
            return unpack_suffix
        return unpack_suffix

    def unpack_prefix_stats(self):
        if self.item_prefix_list:
            for index, prefix_item in enumerate(self.item_prefix_list):
                self.set_stats(prefix_item.attribute_type.value, prefix_item.attribute_value)

    def unpack_suffix_stats(self):
        if self.item_suffix_list:
            for index, suffix_item in enumerate(self.item_suffix_list):
                self.set_stats(suffix_item.attribute_type.value, suffix_item.attribute_value)

    def unpack_item_data(self):
        if self.item_type == EquipmentItemType.ARMOR:
            return f'Base Item: {self.base_item.name}, {self.base_item.armor}, {self.base_item.item_slot_type}\n'
        if self.item_type == EquipmentItemType.WEAPON:
            return f'Base Item: {self.base_item.name}, {self.base_item.weapon_subclass}, ' \
                   f'{self.base_item.minimum_damage}, {self.base_item.maximum_damage}, {self.base_item.item_slot_type}\n'
        if self.item_type == EquipmentItemType.SHIELD:
            return f'Base Item: {self.base_item.name}, {self.base_item.block_chance}, {self.base_item.item_slot_type}\n'
        if self.item_type == EquipmentItemType.RING:
            return f'Base Item: {self.base_item.name}, {self.base_item.item_slot_type}\n'
        if self.item_type == EquipmentItemType.AMULET:
            return f'Base Item: {self.base_item.name}, {self.base_item.item_slot_type}\n'
