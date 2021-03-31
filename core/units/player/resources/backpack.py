#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BackPack:
    def __init__(self):
        self.max_slots = 20
        self.backpack_list = []

    def add_item(self, item):
        if len(self.backpack_list) > self.max_slots:
            return False
        else:
            self.backpack_list.append(item)
            return True

    def remove_item(self, item):
        for index, tmp_item in enumerate(self.backpack_list):
            if item is tmp_item:
                self.backpack_list.pop(index)
                return True
        return False

    def get_list_item(self):
        return self.backpack_list

    def list_items(self):
        print('=========' * 10)
        if self.backpack_list:
            for index, tmp_item in enumerate(self.backpack_list):
                print(f'Index {index}\n', tmp_item)
                print('=========' * 10)
        else:
            print(f'Index 0\n', 'Empty')
            print('=========' * 10)

    def get_stats(self):
        # Basic Attribute Stats: Strength, Dexterity, Magic, Resilience, Vitality, Luck
        total_strength = 0
        total_dexterity = 0
        total_magic = 0
        total_resilience = 0
        total_vitality = 0
        total_luck = 0

        # Basic Attribute Resource: Fury, Health, Mana
        total_max_fury = 0
        total_max_hp = 0
        total_max_mp = 0

        total_attack_power = 0
        total_attack_rating = 0
        total_magic_power = 0

        print()
        print('///////////' * 8)
        for equipment_index, backpack_item in enumerate(self.backpack_list):
            # current_equipment_item = equipment_items[self.get_type_from_index(equipment_index)]

            print(f' BackPack Index Item: {equipment_index}')
            print(backpack_item)
            print('///////////' * 8)
            total_strength += backpack_item.strength
            total_dexterity += backpack_item.dexterity
            total_magic += backpack_item.magic
            total_vitality += backpack_item.vitality
            total_resilience += backpack_item.resilience
            total_luck += backpack_item.luck

            total_max_hp += backpack_item.max_hp
            total_max_mp += backpack_item.max_mp
            total_max_fury += backpack_item.max_fury

        print('\nADD:')
        print(f'T_Strength: {total_strength}, T_Dexterity: {total_dexterity}, T_Magic: {total_magic}, '
              f'T_Vitality: {total_vitality}, T_Resilience: {total_resilience}, T_Luck: {total_luck}, '
              f'T_AttackPower: {total_attack_power}, T_AttackRating: {total_attack_rating}, T_MagicPower: {total_magic_power} '
              f'T_MaxHP: {total_max_hp}, T_MaxMP: {total_max_mp}, T_MaxFury: {total_max_fury} ')
        print('///////////' * 8)
        return total_strength, total_dexterity, total_magic, total_vitality, total_resilience, total_luck, \
               total_attack_power, total_attack_rating, total_magic_power, total_max_hp, total_max_mp, total_max_fury
