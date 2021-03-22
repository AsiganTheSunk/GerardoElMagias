from random import randint


class BasicNode:
    def __init__(self, name, node_index, properties=None, next_node=None, previous_node=None):
        self.name = name
        self.node_index = node_index
        self.previous_node = previous_node
        self.next_node = next_node
        self.right_alternative_path_node = None
        self.left_alternative_path_node = None
        self.dungeon_node = None

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
        self.right_alternative_path_node = alternative_path_node

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


class MapGraphNavigator:
    def __init__(self):
        pass


class MapGraphGenerator:
    def __init__(self):
        self.name = 'MAP'

    @staticmethod
    def roll_shop_node():
        return randint(1, 100) <= 10

    @staticmethod
    def roll_dungeon_node():
        return randint(1, 100) <= 20

    @staticmethod
    def roll_alternative_node(diminishing=1):
        return randint(1, 100) <= round(40 / diminishing)

    def create_node(self, name, index, properties):
        return BasicNode(name, index, properties)

    def create_alternative_node(self, name, index):
        return AlternativeNode(name, index)

    def create_dungeon_node(self, name, index):
        return DungeonNode(name, index)

    def create_shop_node(self, name, index):
        return ShopNode(name, index)

    def bind_dungeon_node(self, alternative_path_node, index):
        if alternative_path_node is not None:
            if self.roll_dungeon_node():
                dungeon_node = DungeonNode(alternative_path_node.name, index)
                alternative_path_node.set_dungeon_node(dungeon_node)
                dungeon_node.set_previous_node(alternative_path_node)
                return dungeon_node
            return None

    def bind_shop_node(self, dungeon_node, index):
        if dungeon_node is not None:
            if self.roll_shop_node():
                shop_node = ShopNode(dungeon_node.name, index)
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

    def bind_right_alt_node(self, current_node, previous_node, index):
        # current_diminishing = self.calculate_diminishing(previous_node)

        if self.roll_alternative_node(current_node.get_diminishing()):

            current_node.increment_diminishing()
            alternative_path_node = self.create_alternative_node(current_node.name, index)
            alternative_path_node.set_previous_node(current_node)

            if previous_node.right_alternative_path_node is not None:
                alternative_path_node.set_previous_node(previous_node.right_alternative_path_node)
                previous_node.right_alternative_path_node.set_next_node(alternative_path_node)

            current_node.set_right_alternative_path(alternative_path_node)
            return current_node, previous_node, alternative_path_node

        if previous_node.right_alternative_path_node is not None:
            previous_node.right_alternative_path_node.set_next_node(current_node)

        return current_node, previous_node, None

    def generate_main_map(self, stage_name, stage_property_list):
        final_list_of_nodes = []
        previous_node = None

        for index, stage_property in enumerate(stage_property_list):
            current_node = self.create_node(stage_name, index, stage_property)

            current_node, previous_node = self.bind_previous_nodes(current_node, previous_node)
            if current_node != previous_node:
                current_node, previous_node, alternative_path_node = \
                    self.bind_right_alt_node(current_node, previous_node, index)

                dungeon_node = self.bind_dungeon_node(alternative_path_node, index)
                self.bind_shop_node(dungeon_node, index)

                dungeon_node = self.bind_dungeon_node(current_node, index)
                self.bind_shop_node(dungeon_node, index)

            previous_node = current_node

            final_list_of_nodes.append(current_node)
        return final_list_of_nodes

    def generate_world_map(self, realm_name_list, list_of_realm_properties):
        # map_graph_generator = MapGraphGenerator()
        # nodes_of_forest_realm = map_graph_generator.generate_main_map('Forest', main_line_forest)
        # nodes_of_castle_real = map_graph_generator.generate_main_map('Castle', main_line_castle)
        world_map = []
        for realm_index, realm_name in enumerate(realm_name_list):
            current_realm = self.generate_main_map(realm_name, list_of_realm_properties[realm_index])
            world_map.append(current_realm)
            self.show_realm(current_realm)
        return world_map

    def show_realm(self, node_list):
        for item in node_list:
            print('-------' * 8)
            print(f'Current Node: {item.name} {item.node_index}')
            print(f'Properties: {item.properties.number_of_battles} {item.properties.boss_battle_index}')
            full_path = item.properties.get_full_path()
            print(f'Full Path:', full_path)
            if item.previous_node is not None:
                print(f'Previous Node: {item.previous_node.name} {item.previous_node.node_index}')
            if item.next_node is not None:
                print(f'Next Node: {item.next_node.name} {item.next_node.node_index}')
            if item.right_alternative_path_node is not None:
                print('Alt. Right Node:', item.right_alternative_path_node.name)
                if item.right_alternative_path_node.previous_node is not None:
                    print('Alt. Right Previous Node:', item.right_alternative_path_node.previous_node.name)
                if item.right_alternative_path_node.next_node is not None:
                    print('Alt. Right Next Node:', item.right_alternative_path_node.next_node.name,
                          item.right_alternative_path_node.next_node.node_index)
                if item.right_alternative_path_node.dungeon_node is not None:
                    print('Dungeon Alt. Node:', item.right_alternative_path_node.dungeon_node.name)
                    if item.right_alternative_path_node.dungeon_node.next_node is not None:
                        print('Alt. Shop Portal Node:', item.right_alternative_path_node.dungeon_node.next_node.name)
            if item.dungeon_node is not None:
                print('Dungeon Node:', item.dungeon_node.name)
                if item.dungeon_node.next_node is not None:
                    print('Shop Portal Node:', item.dungeon_node.next_node.name)


class BasicNodeProperties:
    def __init__(self, level, number_of_battles=None, boss_battle_index=None, enemy_types=None, boss_types=None):
        self.level = level
        self.number_of_battles = self.generate_number_of_battles(number_of_battles)
        self.boss_battle_index = boss_battle_index
        self.number_of_bosses = len(boss_battle_index)
        self.enemy_types = enemy_types
        self.boss_types = boss_types
        self.complete_status = False

    def generate_number_of_battles(self, number_of_battles):
        if number_of_battles is None:
            return self.random_number_of_battles()
        return number_of_battles

    def random_number_of_battles(self):
        return 1

    def random_boss_battle_index(self):
        return 1

    def complete_stage_node(self):
        self.complete_status = True

    def get_full_path(self):
        full_path_list = []
        for battle_index in range(self.number_of_battles):
            if battle_index in self.boss_battle_index:
                full_path_list.append(True)
            else:
                full_path_list.append(False)
        return full_path_list


main_line_forest = [
    BasicNodeProperties(1, 5, [], ['Bandit'], []),
    BasicNodeProperties(2, 6, [5], ['Bandit'], ['Chief Bandit']),
    BasicNodeProperties(3, 4, [1, 3], ['Bandit'], ['Chief Bandit', 'Djinn']),
]

main_line_castle = [
    BasicNodeProperties(1, 5, [], ['Esqueleteiro'], []),
    BasicNodeProperties(2, 6, [5], ['Esqueleteiro'], ['Chief Esqueleteiro']),
    BasicNodeProperties(3, 4, [1, 3], ['Esqueleteiro'], ['Chief Esqueleteiro', 'Djinn']),
]

map_generator = MapGraphGenerator()
normal_world = map_generator.generate_world_map(['Forest', 'Castle'], [main_line_forest, main_line_castle])


class StageSelector:
    def __init__(self, world_map):
        self.world_map = world_map
        self.current_realm_index = 0
        self.current_realm = self.world_map[self.current_realm_index]
        self.current_stage = self.world_map[self.current_realm_index][0]

    def get_current_stage(self):
        return self.current_stage

    # Todo: Review how to properly implement this step, via index would be a better option
    def set_current_stage(self, stage_node):
        if stage_node.previous.properties.complete_status:
            return stage_node

    # Todo: Talk with stage initializer to run the stage
    def run_stage_node(self):
        pass

    def has_been_completed(self):
        return self.current_stage.properties.complete_status

    def move_to_next_node(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.next_node

    def move_to_previous_node(self):
        if self.current_stage.previous_node is not None:
            self.current_stage = self.current_stage.previous_node

    def move_to_right_alternative_node(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.right_alternative_path_node

    def move_to_left_alternative_node(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.left_alternative_path_node

    def move_to_dungeon(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.dungeon_node

    def is_main_line_completed(self):
        self.is_completed_realm(self.current_realm[0])

    def is_completed_realm(self, stage_node=None):
        if stage_node is not None:
            if stage_node.propierties.complete_status:
                self.is_completed_realm(stage_node.next_node)
            return False
        return True

    def move_to_next_realm(self):
        if self.is_completed_realm() and self.current_realm_index < len(self.world_map):
            self.current_realm_index += 1
            self.current_realm = self.world_map[self.current_realm_index]

    def move_to_previous_realm(self):
        if self.current_realm_index > 0:
            self.current_realm_index -= 1
            self.current_realm = self.world_map[self.current_realm_index]
