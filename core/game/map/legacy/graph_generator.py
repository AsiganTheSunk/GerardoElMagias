#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.game.map.legacy.graph_node import BasicNode, AlternativeNode, DungeonNode, ShopNode


class MapGraphGenerator:
    def __init__(self):
        self.name = 'MAP'

    @staticmethod
    def roll_shop_node():
        return randint(1, 100) <= 10

    @staticmethod
    def roll_dungeon_node():
        return randint(1, 100) <= 50

    @staticmethod
    def roll_alternative_node(diminishing=1):
        return randint(1, 100) <= round(50 / diminishing)

    def create_node(self, name, index, properties):
        return BasicNode(name, index, properties)

    def create_alternative_node(self, name, index):
        return AlternativeNode(name, index)

    def create_dungeon_node(self, name, index):
        return DungeonNode(name, index)

    def create_shop_node(self, name, index):
        return ShopNode(name, index)

    def bind_dungeon_node(self, alternative_path_node, index):
        if alternative_path_node is not None:
            if self.roll_dungeon_node():
                dungeon_node = DungeonNode(alternative_path_node.name, index)
                alternative_path_node.set_dungeon_node(dungeon_node)
                dungeon_node.set_previous_node(alternative_path_node)
                return dungeon_node
            return None

    def bind_shop_node(self, dungeon_node, index):
        if dungeon_node is not None:
            if self.roll_shop_node():
                shop_node = ShopNode(dungeon_node.name, index)
                shop_node.set_previous_node(dungeon_node)
                dungeon_node.set_next_node(shop_node)
                return shop_node
            return None

    def bind_previous_nodes(self, current_node, previous_node=None):
        if previous_node is None:
            return current_node, current_node
        else:
            previous_node.set_next_node(current_node)
            current_node.set_previous_node(previous_node)
            return current_node, previous_node

    def calculate_diminishing(self, previous_node):
        # increment diminishing if previous node has alternative path
        if previous_node is not None and previous_node.right_alternative_path_node is not None:
            return previous_node.diminishing + 1
        return 1

    def bind_right_alt_node(self, current_node, previous_node, index):
        # current_diminishing = self.calculate_diminishing(previous_node)
        if self.roll_alternative_node(current_node.get_diminishing()):

            current_node.increment_diminishing()
            alternative_path_node = self.create_alternative_node(current_node.name, index)
            alternative_path_node.set_previous_node(current_node)

            if previous_node.right_child is not None:
                alternative_path_node.set_previous_node(previous_node.right_child)
                previous_node.right_child.set_next_node(alternative_path_node)

            current_node.set_right_alternative_path(alternative_path_node)
            return current_node, previous_node, alternative_path_node

        if previous_node.right_child is not None:
            previous_node.right_child.set_next_node(current_node)

        return current_node, previous_node, None

    def generate_realm_map(self, stage_name, stage_property_list, main_line=False):
        final_list_of_nodes = []
        previous_node = None
        for index, stage_property in enumerate(stage_property_list):
            current_node = self.create_node(stage_name, index, stage_property)

            current_node, previous_node = self.bind_previous_nodes(current_node, previous_node)

            if not main_line:
                if current_node != previous_node:
                    current_node, previous_node, alternative_path_node = \
                        self.bind_right_alt_node(current_node, previous_node, index)

                    dungeon_node = self.bind_dungeon_node(alternative_path_node, index)
                    self.bind_shop_node(dungeon_node, index)

                dungeon_node = self.bind_dungeon_node(current_node, index)
                self.bind_shop_node(dungeon_node, index)

            previous_node = current_node

            final_list_of_nodes.append(current_node)
        return final_list_of_nodes

    def generate_world_map(self, realm_name_list, list_of_realm_properties):
        # map_graph_generator = MapGraphGenerator()
        # nodes_of_forest_realm = map_graph_generator.generate_main_map('Forest', main_line_forest)
        # nodes_of_castle_real = map_graph_generator.generate_main_map('Castle', main_line_castle)
        world_map = []
        for realm_index, realm_name in enumerate(realm_name_list):
            current_realm = self.generate_realm_map(realm_name, list_of_realm_properties[realm_index])
            world_map.append(current_realm)
            self.show_realm(current_realm)
        return world_map

    def show_realm(self, node_list):
        for item in node_list:
            print('-------' * 8)
            print(f'Current Node: {item.name} {item.node_index}')
            print(f'Properties: {item.properties.number_of_battles} {item.properties.boss_battle_index}')
            full_path = item.properties.get_full_path()
            print(f'Full Path:', full_path)
            if item.previous_node is not None:
                print(f'Previous Node: {item.previous_node.name} {item.previous_node.node_index}')
            if item.next_node is not None:
                print(f'Next Node: {item.next_node.name} {item.next_node.node_index}')
            if item.right_child is not None:
                print('Alt. Right Node:', item.right_child.name)
                if item.right_child.previous_node is not None:
                    print('Alt. Right Previous Node:', item.right_child.previous_node.name)
                if item.right_child.next_node is not None:
                    print('Alt. Right Next Node:', item.right_child.next_node.name,
                          item.right_child.next_node.node_index)
                if item.right_child.dungeon_node is not None:
                    print('Dungeon Alt. Node:', item.right_child.dungeon_node.name)
                    if item.right_child.dungeon_node.next_node is not None:
                        print('Alt. Shop Portal Node:', item.right_child.dungeon_node.next_node.name)
            if item.dungeon_node is not None:
                print('Dungeon Node:', item.dungeon_node.name)
                if item.dungeon_node.next_node is not None:
                    print('Shop Portal Node:', item.dungeon_node.next_node.name)

    def generate_child_node(self, parent_node, index, side):
        luck = [90, 80, 60, 30, 0]
        test_luck = randint(1, 99) < luck[parent_node.node_level]
        if test_luck:
            print( '----------', luck[parent_node.node_level], '----------')
            new_name = f'{side} Child {parent_node.name} {parent_node.node_level}'

            new_node = self.create_node(new_name, index, None)
            new_node.node_level += 1
            print(new_name)
            return new_node
        return None




# map_generator = MapGraphGenerator()
# main_node_line = map_generator.generate_realm_main_line('Forest', 1)
# complete_graph = map_generator.recursive_node_creation(main_node_line)
