#!/usr/bin/python3

# Import MerkleTree Module
from merkletree.merkle_tree import MerkleTree

# Import System Modules
import math
import hashlib

# Imports Custom Logger & Logging Modules
from logger.custom_logger import CustomLogger
from logging import INFO, DEBUG, WARNING
import logging

# Import Constant
from constants.constants import message_separator

class MerkleBuilder():
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

    def build_merkle_tree(self, blocks):
        """
        This function Creates the Merkle Tree.
        :param blocks:
        :return:
        """
        tmp_merkle_tree = MerkleTree()
        n = int(len(blocks))

        self.logger.debug(message_separator)
        self.logger.debug('[ {0} ]: Building {1}'.format(self.name, tmp_merkle_tree.name))
        self.logger.debug(message_separator)
        self.logger.debug('')
        if len(blocks) > 2:
            tmp_merkle_tree = self.create_leaf_lvl(tmp_merkle_tree, blocks[:int(math.pow(2, n.bit_length() - 1))])
            tmp_merkle_tree = self.create_node_lvl(tmp_merkle_tree, 0)
            return tmp_merkle_tree

    def create_leaf_lvl(self,tmp_merkle_tree, blocks):
        "create leaf lvl for the hashed values"
        self.logger.debug('[ {0} ]: Number Of Leafs Detected {1}'.format(self.name, len(blocks)))
        try:
            for block_index in range(0, len(blocks), 1):
                hashed_block = hashlib.sha256(blocks[block_index]).hexdigest()
                tmp_merkle_tree.add_node(hash=hashed_block, block= blocks[block_index])
            return tmp_merkle_tree
        except Exception as err:
            print('{0}'.format(err))

    def create_node_lvl(self, merkle_tree, node_lvl):
        """
        Create tree lvl till the root node
        :param merkle_tree:
        :param node_lvl:
        :return:
        """
        tmp_nodes = merkle_tree.search_nodes_from_lvl(node_lvl)
        self.logger.debug(message_separator)
        while len(tmp_nodes) != 2:
            self.logger.debug('[ {0} ]: Building {1} Lvl {2}'.format(self.name, merkle_tree.name, node_lvl))
            self.logger.debug('[ {0} ]: Tree_Size {1} '.format(self.name, len(tmp_nodes)))
            self.logger.debug(message_separator)
            for index in range(0, len(tmp_nodes), 2):
                composed_hash = bytes(tmp_nodes[index].hash + tmp_nodes[index+ 1].hash, 'utf-8')
                hashed_block = hashlib.sha256(composed_hash).hexdigest()
                merkle_tree.add_node(hash=hashed_block, node_lvl=node_lvl + 1, children=[tmp_nodes[index].node_identifier, tmp_nodes[index+1].node_identifier])

            node_lvl+=1
            tmp_nodes = merkle_tree.search_nodes_from_lvl(node_lvl)

        if len(tmp_nodes) == 2:

            self.logger.debug('[ {0} ]: Building {1} Lvl {2}'.format(self.name, merkle_tree.name, node_lvl))
            self.logger.debug('[ {0} ]: Tree_Size {1} '.format(self.name, len(tmp_nodes)))
            self.logger.debug(message_separator)
            composed_hash = bytes(tmp_nodes[0].hash + tmp_nodes[1].hash, 'utf-8')
            hashed_block = hashlib.sha256(composed_hash).hexdigest()
            tmp_node = merkle_tree.add_node(hash=hashed_block, node_lvl=node_lvl + 1, children=[tmp_nodes[0].node_identifier, tmp_nodes[1].node_identifier], root=True)
            merkle_tree.set_root(tmp_node)
            return merkle_tree

        return merkle_tree


    def validate_hash(self, merkle_tree, node_identifier, challenger_hash):
        """
        This function applies the minimal coverage method plus the recalculation of the hashes till the root to find out if one node it's from the tree or not.
        :param merkle_tree:
        :param node_identifier:
        :param challenger_hash:
        :return:
        """
        if node_identifier > len(merkle_tree.search_nodes_from_lvl(0)):
            return 0
        else:
            aux_coverage = []
            minimal_coverage = merkle_tree.minimal_coverage(node_identifier, aux_coverage)
            self.logger.debug(message_separator)
            self.logger.debug('[ Challenger_Node_Identifier ]: {0} [ Challenger_Node_Hash_Value ]: {1}'.format(node_identifier, challenger_hash))
            self.logger.debug('[ Minimal_Coverage ]: {0}'.format(minimal_coverage))
            self.logger.debug(message_separator)
            hashed_block = None
            for index in range(1, len(minimal_coverage), 1):
                if hashed_block is None:

                    # Minimal Coverage Here
                    children = merkle_tree.get_nodes()[minimal_coverage[index]].children_identifiers
                    self.logger.debug('[ Parent_Node_Identifier ]: {0},  Children_Node_Identifiers {1}'.format(merkle_tree.get_nodes()[minimal_coverage[index]].get_node_identifier(), children))

                    sibling_index = minimal_coverage[index - 1]

                    # Here we check with child it's the one we need for the next step in the calculations
                    if sibling_index != children[0]:
                        sibling = children[0]
                        sibling_hash = merkle_tree.get_nodes()[sibling].hash
                        self.logger.debug('[ Sibling_Node_Identifier ]: {0} [ Sibling_Hash_Value ]: {1}'.format(sibling, merkle_tree.get_nodes()[sibling].hash))
                        composed_hash = bytes(sibling_hash + challenger_hash, 'utf-8')
                        self.logger.debug('[ Composed_Hash ]: Sibling_Hash {0} + Challenger_Hash {1}'.format(sibling_hash, challenger_hash))
                    else:
                        sibling = children[1]
                        sibling_hash = merkle_tree.get_nodes()[sibling].hash
                        self.logger.debug('[ Sibling_Node_Identifier ]: {0} [ Sibling_Hash_Value ]: {1}'.format(sibling,merkle_tree.get_nodes()[sibling].hash))
                        composed_hash = bytes(challenger_hash + sibling_hash, 'utf-8')
                        self.logger.debug('[ Composed_Hash ]: Challenger_Hash {0} + Sibling_Hash {1}'.format(challenger_hash, sibling_hash))

                    # Here we compose the hash.
                    hashed_block = hashlib.sha256(composed_hash).hexdigest()
                    self.logger.debug('[ Real_Parent_Hash_Value ]: {0}'.format(merkle_tree.get_nodes()[minimal_coverage[index]].hash))
                    self.logger.debug('[ Calculated_Parent_Hash_Value ]: {0}'.format(hashed_block))
                    self.logger.debug(message_separator)
                else:
                    # Minimal Coverage Here
                    children = merkle_tree.get_nodes()[minimal_coverage[index]].children_identifiers
                    sibling_index = minimal_coverage[index - 1]

                    self.logger.debug('[ Parent_Node_Identifier ]: {0},  Children_Node_Identifiers {1}'.format(
                        merkle_tree.get_nodes()[minimal_coverage[index]].get_node_identifier(), children))

                    # Here we check with child it's the one we need for the next step in the calculations
                    if sibling_index != children[0]:
                        sibling = children[0]
                        sibling_hash = merkle_tree.get_nodes()[sibling].hash
                        self.logger.debug('[ Sibling_Node_Identifier ]: {0} [ Sibling_Hash_Value ]: {1}'.format(sibling, merkle_tree.get_nodes()[sibling].hash))
                        composed_hash = bytes(sibling_hash + hashed_block, 'utf-8')
                        self.logger.debug('[ Composed_Hash ]: Sibling_Hash {0} + Challenger_Hash {1}'.format(sibling_hash, challenger_hash))
                    else:
                        sibling = children[1]
                        sibling_hash = merkle_tree.get_nodes()[sibling].hash
                        self.logger.debug('[ Sibling_Node_Identifier ]: {0} [ Sibling_Hash_Value ]: {1}'.format(sibling,merkle_tree.get_nodes()[sibling].hash))
                        composed_hash = bytes(hashed_block + sibling_hash, 'utf-8')
                        self.logger.debug('[ Composed_Hash ]: Challenger_Hash {0} + Sibling_Hash {1}'.format(challenger_hash, sibling_hash))

                    hashed_block = hashlib.sha256(composed_hash).hexdigest()
                    self.logger.debug('[ Real_Parent_Hash_Value ]: {0}'.format(merkle_tree.get_nodes()[minimal_coverage[index]].hash))
                    self.logger.debug('[ Calculated_Parent_Hash_Value ]: {0}'.format(hashed_block))
                    self.logger.debug(message_separator)

            self.logger.debug('[ Root Real_Parent_Hash_Value ]: {0}'.format(merkle_tree.root.hash))
            self.logger.debug('[ Root Calculated_Parent_Hash_Value ]: {0}'.format(hashed_block))
            self.logger.info(message_separator)
            # Las iteration we add the root.
            if merkle_tree.root.hash != hashed_block:
                self.logger.info('[ Challenger_Hash ]: {0} is{1}a Leaf of the Merkle Tree'.format(challenger_hash, ' Not '))
                self.logger.info(message_separator)
                return 0

            self.logger.info('[ Challenger_Hash ]: {0} is{1}a Leaf of the Merkle Tree'.format(challenger_hash, ' '))
            self.logger.info(message_separator)
            return 1