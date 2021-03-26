#!/usr/bin/python3

class MerkleNode:
    def __init__(self, node_identifier, hash, block, node_lvl=0, root=False):
        self.name = __class__.__name__
        self.is_root = root
        self.node_identifier = node_identifier
        self.node_lvl = node_lvl
        self.hash = hash
        self.block = block
        self.parent_identifier = None
        self.children_identifiers = []

    def set_children(self, children_identifiers):
        '''
        This function sets the children_identifiers of a merkle node
        '''
        self.children_identifiers = children_identifiers

    def set_parent(self, parent_identifier):
        '''
        This function sets the parent_identifier of a merkle node
        '''
        self.parent_identifier = parent_identifier

    def set_node_lvl(self, node_lvl):
        '''
        This function sets the node_lvl of a merkle node
        '''
        self.node_lvl = node_lvl

    def set_hash(self, hash):
        '''
        This function sets the hash of a merkle node
        '''
        self.hash = hash

    def get_children(self):
        '''
        This function return the children of a merkle node
        :return: children
        '''
        return self.children_identifiers

    def get_node_identifier(self):
        '''
        This function return the hash of a merkle node
        :return: node identifier
        '''
        return self.node_identifier

    def get_hash(self):
        '''
        This function return the hash of a merkle node
        :return: node hash
        '''
        return self.hash

    def add_children(self, node_identifier):
        '''
        This function Adds a New Child to the children_identifiers list
        :param node_identifier:
        :return: None
        '''
        return self.children_identifiers.append(node_identifier)


    def remove_child(self, node_identifier):
        '''
        This function removes a child with basename from node children
        :param node_identifier:
        :return:
        '''
        tmp_children_indefier = []

        for item in self.get_children():
            if item.identifier != node_identifier:
                tmp_children_indefier.append(item)

        self.set_children(tmp_children_indefier)
        return self.get_children()
