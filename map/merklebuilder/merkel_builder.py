#!/usr/bin/python3

# Import MerkleTree Module
from map.merkletree.merkle_tree import StageTree

# Import System Modules
from random import randint

# Imports Custom Logger & Logging Modules
from map.logger.custom_logger import CustomLogger
from logging import INFO, DEBUG, WARNING
import logging

# Basic Command from the server
message_separator = '////////////' * 10


class StageBuilder:
    def __init__(self, logging_lvl=DEBUG):
        self.name = __class__.__name__
        self.logger = CustomLogger(name=__name__, level=logging_lvl)

        # CustomLogger Format Definition
        formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)s]: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # Custom Logger File Configuration: File Init Configuration
        file_handler = logging.FileHandler('log/merkle_builder.log', 'w')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level=logging_lvl)

        # Custom Logger Console Configuration; Console Init Configuration
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging_lvl)

        # Custom Logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def roll_leaf_lvl(self, tmp_merkle_tree, number_of_blocks):
        pass

    def roll_node_lvl(self, merkle_tree, node_lvl):
        """
        Create tree lvl till the root node
        :param merkle_tree:
        :param node_lvl:
        :return:
        """
        pass

    def build_tree(self, max_number_of_children):
        merkle_tree = StageTree()

        self.logger.debug(message_separator)
        self.logger.debug('[ {0} ]: Building {1}'.format(self.name, merkle_tree.name))
        self.logger.debug(message_separator)
        self.logger.debug('')

        stage_root_node = merkle_tree.add_node(root=True)
        self.build_branch(merkle_tree, stage_root_node, max_number_of_children)
        self.logger.debug(message_separator)
        return merkle_tree

    def build_branch(self, merkle_tree, parent_stage_node, max_number_of_children, diminishing=0):
        diminishing_list = [95, 75, 60, 20, 0]

        self.logger.debug(message_separator)
        for child in range(0, max_number_of_children, 1):
            branch_chance = randint(1, 99) < diminishing_list[diminishing]
            if branch_chance:
                current_stage_node = merkle_tree.add_node(parent_stage_node.node_lvl + 1, parent_stage_node.node_identifier)
                merkle_tree.set_max_node_level(parent_stage_node.node_lvl + 1)
                self.logger.debug(
                    '[ {0} ]: Generate {1} Parent Stage Level {2} Child Number {3} with {4} diminishing CREATED'.format(
                        self.name, current_stage_node.name,
                        parent_stage_node.node_lvl, child, diminishing_list[diminishing]))
                parent_stage_node.add_children(current_stage_node)

                self.build_branch(merkle_tree, current_stage_node, max_number_of_children, diminishing+1)
                self.logger.debug(message_separator)
            else:
                self.logger.debug(
                    '[ {0} ]: Generate {1} Parent Stage Level {2}, Number {3} with {4} diminishing FAILED'.format(
                        self.name, 'StageNode', parent_stage_node.node_lvl, child, diminishing_list[diminishing]))

    def build_node_properties(self):
        pass
