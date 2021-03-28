#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import StageNode Module
from game.map.stage_tree.stage_node import StageNode


class StageTree:
    def __init__(self):
        self.root = None
        self.nodes = []
        self.node_count = -1
        self.max_node_level = 0
        self._properties = {'name': self.__class__.__name__}

    def __getitem__(self, key):
        if key == 'properties':
            return self._properties
        elif key == 'root_identifier':
            return self.root.node_identifier
        elif key == 'root_hash':
            return self.root.hash
        elif key == 'root_lvl':
            return self.root.node_lvl
        elif key == 'node_count':
            return self.get_node_count() + 1
        return self._properties[key]

    def set_max_node_level(self, node_level):
        self.max_node_level = node_level

    def set_root(self, root):
        """
        This function sets the root node of the MerkleTree
        """
        self.root = root

    def get_nodes(self):
        """
        This function return the nodes of the MerkleTree
        :return: node identifier
        """
        return self.nodes

    def get_node_count(self):
        """
        This function returns node_count
        :return: node count
        """
        return self.node_count

    def add_node_count(self):
        """
        This function adds one to node_count
        :return: node count
        """
        self.node_count += 1
        return self.node_count

    def add_node(self, node_lvl=0, parent_identifier=None, root=False):
        """
        This function adds a node to the Merkle Tree
        :param node_lvl: node lvl, default it's 0
        :param parent_identifier: parent identifier for the current Node, default it's None
        :param root: root boolean for the StageTree, default False
        :return: New Node
        """
        try:
            if root:
                # Setting the Root Value
                new_stage_root_node = StageNode(node_identifier=self.add_node_count(), node_lvl=0, root=root)
                self.set_root(new_stage_root_node)
                self.nodes.append(new_stage_root_node)
                return new_stage_root_node
            else:
                new_stage_node = StageNode(node_identifier=self.add_node_count(), node_lvl=node_lvl)
                new_stage_node.set_parent(parent_identifier)
                self.nodes.append(new_stage_node)
                return new_stage_node

        except Exception as err:
            print('{0}'.format(err))

    def display_nodes_from_lvl(self, node_lvl):
        """
        :param node_lvl:
        :return:
        """
        try:
            tmp_nodes = []
            for tmp_node in self.get_nodes():
                if tmp_node.node_lvl == node_lvl:
                    tmp_nodes.append((tmp_node.name, tmp_node, tmp_node.node_identifier))

            return tmp_nodes

        except Exception as err:
            print('{0}'.format(err))

    def search_nodes_from_lvl(self, node_lvl):
        """
        This function ...
        :param node_lvl:
        :return:
        """
        try:
            tmp_nodes = []
            for tmp_node in self.get_nodes():
                if tmp_node.node_lvl == node_lvl:
                    tmp_nodes.append(tmp_node)

            return tmp_nodes

        except Exception as err:
            print('{0}'.format(err))

    def minimal_coverage(self, node_identifier, _minimal_coverage):
        """
        This function ...
        :param node_identifier:
        :param _minimal_coverage:
        :return:
        """
        if not _minimal_coverage:
            _minimal_coverage.append(node_identifier)

        if self.get_nodes()[node_identifier].is_root is True:
            return _minimal_coverage
        else:
            _minimal_coverage.append(self.get_nodes()[node_identifier].parent_identifier)
            return self.minimal_coverage(self.get_nodes()[node_identifier].parent_identifier, _minimal_coverage)

    def show_stage_tree(self):
        print('root', self.root.node_identifier)
        self.show_stage_branch(self.root.node_identifier)

    def show_stage_branch(self, identifier):
        for child in self.nodes[identifier].children_identifiers:
            print('\t'*child.node_lvl, 'child id:', child.node_identifier, 'lvl:', child.node_lvl)
            self.show_stage_branch(child.node_identifier)
