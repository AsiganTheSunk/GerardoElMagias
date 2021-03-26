#!/usr/bin/python3

# Import MerkleNode Module
from merkletree.merkle_node import MerkleNode

class MerkleTree():
    def __init__(self):
        self.name = __class__.__name__
        self.root = None
        self.nodes = []
        self.node_count = -1
        self._properties = {'name': self.name }

    def __getitem__(self, key):
        if key == 'properties':
            return self._properties
        elif key == 'root_identifier':
            return self.root.node_identifier
        elif key == 'root_hash':
            return self.root.hash
        elif key == 'root_lvl':
            return  self.root.node_lvl
        elif key == 'node_count':
            return self.get_node_count() + 1
        return self._properties[key]

    def set_root(self, root):
        '''
        This function sets the root node of the MerkleTree
        '''
        self.root = root

    def get_nodes(self):
        '''
        This function return the nodes of the MerkleTree
        :return: node identifier
        '''
        return self.nodes

    def get_node_count(self):
        '''
        This function returns node_count
        :return: node count
        '''
        return self.node_count

    def add_node_count(self):
        '''
        This function adds one to node_count
        :return: node count
        '''
        self.node_count += 1
        return self.node_count

    def add_node(self, hash, block=b'', node_lvl=0, children=None, root=False):
        '''
        This function adds a node to the Merkle Tree
        :param hash: hash value
        :param block: block data, default it's b''
        :param node_lvl: node lvl, default it's 0
        :param children: children of the merkle node, default it's None
        :param root: root boolean for the merkle tree, default Fase
        :return: New Node
        '''
        try:
            tmp_node = MerkleNode(node_identifier=self.add_node_count(), hash=hash, block=block, node_lvl=node_lvl, root=root)
            if children != None:
                # Setting the Childrens List
                tmp_node.children_identifiers = children
                # Updating the Children Value
                self.get_nodes()[children[0]].parent_identifier = tmp_node.get_node_identifier()
                self.get_nodes()[children[1]].parent_identifier = tmp_node.get_node_identifier()
            if root:
                # Setting the Root Value
                self.set_root(tmp_node)
            self.nodes.append(tmp_node)
            return tmp_node

        except Exception as err:
            print('{0}'.format(err))

    def search_nodes_from_lvl(self, node_lvl):
        '''

        :param node_lvl:
        :return:
        '''
        try:
            tmp_nodes = []
            for tmp_node in self.get_nodes():
                if tmp_node.node_lvl == node_lvl:
                    tmp_nodes.append(tmp_node)

            return tmp_nodes

        except Exception as err:
            print('{0}'.format(err))

    def minimal_coverage(self, node_identifier, _minimal_coverage):
        '''

        :param node_identifier:
        :param _minimal_coverage:
        :return:
        '''
        if _minimal_coverage == []:
            _minimal_coverage.append(node_identifier)

        if self.get_nodes()[node_identifier].is_root is True:
            return _minimal_coverage
        else:
            _minimal_coverage.append(self.get_nodes()[node_identifier].parent_identifier)
            return self.minimal_coverage(self.get_nodes()[node_identifier].parent_identifier, _minimal_coverage)

    def show_merkle_tree(self):
        '''

        :return:
        '''
        for lvl in range(self.root.node_lvl, 0, -1):
            print('////////////' * 10)
            print('{0}'.format(self.search_nodes_from_lvl(lvl)))

