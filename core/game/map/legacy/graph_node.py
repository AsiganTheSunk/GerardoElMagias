#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicNode:
    def __init__(self, name, node_index, properties=None, next_node=None, previous_node=None):
        self.name = name
        self.node_index = node_index
        self.previous_node = previous_node
        self.next_node = next_node
        self.right_child = None
        self.left_child = None
        self.dungeon_node = None
        self.node_level = 0

        self.properties = properties

        self.diminishing = 1

    def get_diminishing(self):
        return self.diminishing

    def increment_diminishing(self):
        self.diminishing += 1

    def reset_diminishing(self):
        self.diminishing = 1

    def set_dungeon_node(self, dungeon_node):
        self.dungeon_node = dungeon_node

    def set_right_alternative_path(self, alternative_path_node):
        self.right_child = alternative_path_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node


class DungeonNode(BasicNode):
    def __init__(self, name, index):
        BasicNode.__init__(self, name + ' Dungeon ', index)


class ShopNode(BasicNode):
    def __init__(self, name, index):
        BasicNode.__init__(self, name + ' Shop', index)


class AlternativeNode(BasicNode):
    def __init__(self, name, index):
        BasicNode.__init__(self, 'Alternative ' + name, index)