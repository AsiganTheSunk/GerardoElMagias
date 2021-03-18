from random import randint

class BasicNode:
    def __init__(self, name, next_node=None, previous_node=None):
        self.name = name
        self.previous_node = previous_node
        self.next_node = next_node
        self.alternative_path_node = None
        self.dungeon_node = None

    def set_dungeon_node(self, dungeon_node):
        self.dungeon_node = dungeon_node

    def set_alternative_path(self, alternative_paht_node):
        self.alternative_path_node = alternative_paht_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

class DungeonNode(BasicNode):
    def __init__(self, name):
        BasicNode.__init__(self, name  + ' Dungeon ')

class ShopNode(BasicNode):
    def __init__(self, name):
        BasicNode.__init__(self, name  + ' Shop')





class AlternativeNode(BasicNode):
    def __init__(self, name):
        BasicNode.__init__(self, 'Alternative ' + name)
        self.diminishing = 1

    def uptdate_diminishing(self, diminishing):
        self.diminishing = diminishing

class MapGraphNavigator:
    def __init__(self):
        pass

class MapGraphGenerator:
    def __init__(self):
        self.name = 'MAP'

    def roll_shop_node(self):
        return randint(1, 100) <= 100

    def roll_dungeon_node(self):
        return randint(1, 100) <= 20

    def roll_alternative_node(self, diminishing=1):
        return randint(1, 100) <= round(40 / diminishing)


    def generate_main_line(self, stage_list):
        list_of_nodes = []
        previous_node = None
        current_dimishing = 1
        for index, stage_name in enumerate(stage_list):
            current_node = BasicNode(stage_name)

            if previous_node is None:
                previous_node = current_node
            else:
                previous_node.set_next_node(current_node)
                current_node.set_previous_node(previous_node)

                # increment diminishing if previous node has alternative path
                if previous_node.alternative_path_node is not None:
                    current_dimishing = previous_node.alternative_path_node.diminishing + 1
                    previous_node.alternative_path_node.set_next_node(current_node)
                else:
                    current_dimishing = 1
                    # print('Reset Diminishing')

                if self.roll_alternative_node(diminishing=current_dimishing):
                    alternative_node_path = AlternativeNode(current_node.name)
                    alternative_node_path.set_previous_node(current_node)

                    if previous_node.alternative_path_node is not None:
                        alternative_node_path.set_previous_node(previous_node.alternative_path_node)
                        previous_node.alternative_path_node.set_next_node(alternative_node_path)

                    alternative_node_path.uptdate_diminishing(current_dimishing)
                    print('current diminishing:', alternative_node_path.diminishing)
                    current_node.set_alternative_path(alternative_node_path)
                    if self.roll_dungeon_node():
                        dungeon_node = DungeonNode(alternative_node_path.name)
                        alternative_node_path.set_dungeon_node(dungeon_node)
                        dungeon_node.set_previous_node(alternative_node_path)
                        if self.roll_shop_node():
                            current_shop_node = ShopNode(dungeon_node.name)
                            current_shop_node.set_previous_node(dungeon_node)
                            dungeon_node.set_next_node(current_shop_node)

                if self.roll_dungeon_node():
                    dungeon_node = DungeonNode(current_node.name)
                    current_node.set_dungeon_node(dungeon_node)
                    dungeon_node.set_previous_node(current_node)
                    if self.roll_shop_node():
                        current_shop_node = ShopNode(dungeon_node.name)
                        current_shop_node.set_previous_node(dungeon_node)
                        dungeon_node.set_next_node(current_shop_node)

                previous_node = current_node

            list_of_nodes.append(current_node)
        return list_of_nodes


stage_list = ['Shop', 'Forest', 'Castle', 'Desert', 'Tombs', 'Dark Forest']

map_graph_generator = MapGraphGenerator()
list_of_nodes = map_graph_generator.generate_main_line(stage_list)

for index, item in enumerate(list_of_nodes):
    print('Index:', index, 'Current_Node:', item.name)
    if item.previous_node is not None:
        print('Previous Node:', item.previous_node.name)
    if item.next_node is not None:
        print('Next Node:', item.next_node.name)
    if item.alternative_path_node is not None:
        print('Alternative Path Node:', item.alternative_path_node.name)
        if item.alternative_path_node.previous_node is not None:
            print('Alternative Path Previous Node:', item.alternative_path_node.previous_node.name)
        if item.alternative_path_node.next_node is not None:
            print('Alternative Path Next Node:', item.alternative_path_node.next_node.name)
        if item.alternative_path_node.dungeon_node is not None:
            print('Dungeon Alternative Path Node:', item.alternative_path_node.dungeon_node.name)
            if item.alternative_path_node.dungeon_node.next_node is not None:
                print('Alternative Dungeon Shop:', item.alternative_path_node.dungeon_node.next_node.name)
    if item.dungeon_node is not None:
        print('Dungeon Node:', item.dungeon_node.name)
        if item.dungeon_node.next_node is not None:
            print('Dungeon Shop Node:', item.dungeon_node.next_node.name)


    print('-------' * 8)