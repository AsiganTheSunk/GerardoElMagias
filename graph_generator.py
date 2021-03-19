from random import randint


# class StageSelector:
#     def __init__(self, mapa):
#         self.current_node = mapa[0]
#         self.mapa = mapa
#
#     def generate_stage(self):
#         data = self.current_node.data
#         # enemey_group()
#
#     def advance_to_node(self, node):
#         self.current_node = node
#
#
# class BasicNodeProperties:
#     def __init__(self):
#         self.number_of_bosses = 2
#         self.number_of_screens = 10
#         self.enemy_type = ''
#         pass


class BasicNode:
    def __init__(self, name, next_node=None, previous_node=None):
        self.name = name
        self.previous_node = previous_node
        self.next_node = next_node
        self.right_alternative_path_node = None
        self.left_alternative_path_node = None
        self.dungeon_node = None

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
        self.right_alternative_path_node = alternative_path_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node


class DungeonNode(BasicNode):
    def __init__(self, name):
        BasicNode.__init__(self, name + ' Dungeon ')


class ShopNode(BasicNode):
    def __init__(self, name):
        BasicNode.__init__(self, name + ' Shop')


class AlternativeNode(BasicNode):
    def __init__(self, name):
        BasicNode.__init__(self, 'Alternative ' + name)


class MapGraphNavigator:
    def __init__(self):
        pass


class MapGraphGenerator:
    def __init__(self):
        self.name = 'MAP'

    @staticmethod
    def roll_shop_node():
        return randint(1, 100) <= 100

    @staticmethod
    def roll_dungeon_node():
        return randint(1, 100) <= 20

    @staticmethod
    def roll_alternative_node(diminishing=1):
        return randint(1, 100) <= round(40 / diminishing)

    def create_node(self, name):
        return BasicNode(name)

    def create_alternative_node(self, name):
        return AlternativeNode(name)

    def create_dungeon_node(self, name):
        return DungeonNode(name)

    def create_shop_node(self, name):
        return ShopNode(name)

    def bind_dungeon_node(self, alternative_path_node):
        if alternative_path_node is not None:
            if self.roll_dungeon_node():
                dungeon_node = DungeonNode(alternative_path_node.name)
                alternative_path_node.set_dungeon_node(dungeon_node)
                dungeon_node.set_previous_node(alternative_path_node)
                return dungeon_node
            return None

    def bind_shop_node(self, dungeon_node):
        if dungeon_node is not None:
            if self.roll_shop_node():
                shop_node = ShopNode(dungeon_node.name)
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

    def bind_right_alt_node(self, current_node, previous_node):
        # current_diminishing = self.calculate_diminishing(previous_node)

        if self.roll_alternative_node(current_node.get_diminishing()):

            current_node.increment_diminishing()
            alternative_path_node = self.create_alternative_node(current_node.name)
            alternative_path_node.set_previous_node(current_node)

            if previous_node.right_alternative_path_node is not None:
                alternative_path_node.set_previous_node(previous_node.right_alternative_path_node)
                previous_node.right_alternative_path_node.set_next_node(alternative_path_node)

            current_node.set_right_alternative_path(alternative_path_node)
            return current_node, previous_node, alternative_path_node

        if previous_node.right_alternative_path_node is not None:
            previous_node.right_alternative_path_node.set_next_node(current_node)

        return current_node, previous_node, None

    def generate_main_map(self, stage_list):
        final_list_of_nodes = []
        previous_node = None

        for stage_name in stage_list:
            current_node = self.create_node(stage_name)

            current_node, previous_node = self.bind_previous_nodes(current_node, previous_node)
            # if current_node != previous_node:
            #     current_node, previous_node, alternative_path_node = \
            #         self.bind_right_alt_node(current_node, previous_node)
            #
            #     dungeon_node = self.bind_dungeon_node(alternative_path_node)
            #     self.bind_shop_node(dungeon_node)
            #
            #     dungeon_node = self.bind_dungeon_node(current_node)
            #     self.bind_shop_node(dungeon_node)
            #
            #     previous_node = current_node

            final_list_of_nodes.append(current_node)
        return final_list_of_nodes


# stage_list = ['Shop', 'Forest', 'Castle', 'Desert', 'Tombs', 'Dark Forest']
# stage_list = ['Shop', 'Forest', 'Castle']
#
#
# map_graph_generator = MapGraphGenerator()
# list_of_nodes = map_graph_generator.generate_main_map(stage_list)
#
# for index, item in enumerate(list_of_nodes):
#     print('Index:', index, 'Current Node:', item.name)
#     if item.previous_node is not None:
#         print('Previous Node:', item.previous_node.name)
#     if item.next_node is not None:
#         print('Next Node:', item.next_node.name)
#     if item.right_alternative_path_node is not None:
#         print('Alt. Right Node:', item.right_alternative_path_node.name)
#         if item.right_alternative_path_node.previous_node is not None:
#             print('Alt. Right Previous Node:', item.right_alternative_path_node.previous_node.name)
#         if item.right_alternative_path_node.next_node is not None:
#             print('Alt. Right Next Node:', item.right_alternative_path_node.next_node.name)
#         if item.right_alternative_path_node.dungeon_node is not None:
#             print('Dungeon Alt. Node:', item.right_alternative_path_node.dungeon_node.name)
#             if item.right_alternative_path_node.dungeon_node.next_node is not None:
#                 print('Alt. Shop Portal Node:', item.right_alternative_path_node.dungeon_node.next_node.name)
#     if item.dungeon_node is not None:
#         print('Dungeon Node:', item.dungeon_node.name)
#         if item.dungeon_node.next_node is not None:
#             print('Shop Portal Node:', item.dungeon_node.next_node.name)
#     print('-------' * 8)
