#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import StageTree Module
from core.game.map.stage_tree.stage_tree import StageTree

# Import System Modules
from random import randint

# Imports Custom Logger & Logging Modules
from logger.logger_master import LoggerMaster
from logger.constants.logger_level_type import LoggingLevelType


class StageTreeBuilder:
    def __init__(self):
        self.stage_tree_logger = LoggerMaster(__class__.__name__, level=LoggingLevelType.DEBUG.value)

    def roll_leaf_level_properties(self, stage_tree):
        pass

    def roll_node_level_properties(self, stage_tree, node_lvl):
        pass

    def build_tree(self, max_number_of_children):
        stage_tree = StageTree()
        self.stage_tree_logger.log_debug_header(f'[ {self.__class__.__name__} ]:'
                                                f' Building {stage_tree.__class__.__name__}')
        self.stage_tree_logger.log_debug_message()
        stage_root_node = stage_tree.add_node(root=True)
        self.build_branch(stage_tree, stage_root_node, max_number_of_children)
        return stage_tree

    def build_branch(self, stage_tree, parent_stage_node, max_number_of_children, diminishing=0):
        diminishing_list = [95, 75, 60, 20, 0]

        for child in range(0, max_number_of_children, 1):
            branch_chance = randint(1, 99) < diminishing_list[diminishing]
            if branch_chance:
                current_stage_node = stage_tree.add_node(parent_stage_node.node_lvl + 1, parent_stage_node.node_identifier)
                stage_tree.set_max_node_level(parent_stage_node.node_lvl + 1)
                self.stage_tree_logger.log_debug_message(f'[ {self.__class__.__name__} ]:'
                                                         f' Generate {current_stage_node.__class__.__name__}'
                                                         f' Parent Stage Level {parent_stage_node.node_lvl}'
                                                         f' Child Number {child}'
                                                         f' with {diminishing_list[diminishing]} diminishing'
                                                         f' CREATED')
                parent_stage_node.add_children(current_stage_node)
                self.build_branch(stage_tree, current_stage_node, max_number_of_children, diminishing + 1)
            else:
                self.stage_tree_logger.log_debug_message(f'[ {self.__class__.__name__} ]:'
                                                         f' Generate StageNode Parent Stage Level'
                                                         f' Parent Stage Level {parent_stage_node.node_lvl}'
                                                         f' Child Number {child}'
                                                         f' with {diminishing_list[diminishing]} diminishing'
                                                         f' FAILED')

    def build_node_properties(self):
        pass
