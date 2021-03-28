# def generate_new_level(self, main_node_line, index):
#     new_child_right = self.generate_child_node(main_node_line, index, 'Right')
#     new_child_left = self.generate_child_node(main_node_line, index, 'Left')
#
#     if new_child_left is not None:
#         self.bind_previous_nodes(new_child_left, main_node_line)
#         self.generate_new_level(new_child_left, index)
#
#     if new_child_right is not None:
#         self.bind_previous_nodes(new_child_right, main_node_line)
#         self.generate_new_level(new_child_right, index)
#
#     return main_node_line
#
#
# def recursive_node_creation(self, main_node_line):
#     for index, main_node in enumerate(main_node_line):
#         main_node.right_child = self.generate_new_level(main_node, index)
#         main_node.left_child = self.generate_new_level(main_node, index)
#
#     return main_node_line
#
#
# def generate_realm_main_line(self, main_stage_name, number_of_main_nodes):
#     main_node_line = []
#     previous_node = None
#     for index in range(number_of_main_nodes):
#         current_node = self.create_node(main_stage_name, index, None)
#         current_node, previous_node = self.bind_previous_nodes(current_node, previous_node)
#         previous_node = current_node
#         main_node_line.append(current_node)
#     return main_node_line


# Source https://www.dailycodingproblem.com/blog/big-tree/
# Source 2: https://www.geeksforgeeks.org/select-random-node-tree-equal-probability/

import random


class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.level = 0

    def __str__(self, level=0):
        ret = ''
        if level == 0:
            ret = "-" * level + repr(self.value) + "\n"
        if self.right_child is not None:
            ret += "-" * level + f'> right child {level}' + "\n" + self.right_child.__str__(level+1)
        if self.left_child is not None:
            ret += "-" * level + f'> left child {level}' + "\n" + self.left_child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'


def generate():
    root = Node(0)

    if random.random() < 0.4:
        root.left_child = generate()
    if random.random() < 0.6:
        root.right_child = generate()

    return root

print(generate())

