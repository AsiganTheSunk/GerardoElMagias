from pygame import font, init, time, key, mouse, draw, Color, Rect, event as pygame_events, MOUSEBUTTONUP, \
    QUIT, K_LEFT, K_a, K_RIGHT, K_d, K_SPACE, K_RETURN, display, Surface, SRCALPHA


class MapGraphDrawer:
    def __init__(self, surface):
        self.surface = surface
        self.current_realm_map = None
        self.basic_step = 25  # 25px

        self.stage_binding_list = []
        self.stage_rect_node_list = []
        self.stage_rect_alternative_node_list = []
        self.stage_rect_dungeon_node = []

        self.binding_height = 8
        self.starting_node_position_x = 100
        self.starting_node_position_y = 250

        self.last_updated = 0
        self.total_steps = 0

    def set_current_realm(self, realm_map):
        self.current_realm_map = realm_map

    def add_stage_node(self, stage_node):
        self.stage_rect_node_list.append(stage_node)

    def display_selector(self):
        starting_pos_x = 100
        starting_pos_y = 250
        draw.circle(self.surface, Color('Red'), (starting_pos_x, starting_pos_y), 25)

    def create_node(self, x, y):
        return Rect(x, y, 30, 30)

    def generate_portal_shop_position(self):
        pass

    def generate_dungeon_node_position(self):
        # for alternative_stage_index, alternative_stage_node in enumerate(self.current_realm_map):
        print('xxxxxxxxxxxxxx'*8)
        current_helper_index = 0
        for stage_index, stage_node in enumerate(self.current_realm_map):
            print('Stage Node:', stage_node.name, stage_node.node_index)
            if stage_node.right_child is not None:

                if stage_node.right_child.dungeon_node is not None:
                    starting_pos_y = self.stage_rect_alternative_node_list[current_helper_index].y - \
                                     round((self.basic_step * stage_node.properties.number_of_battles) / 2)
                    starting_pos_x = self.stage_rect_alternative_node_list[current_helper_index].x + \
                                     round((self.basic_step * stage_node.properties.number_of_battles) / 2)

                    print('Has Dungeon Node Linked to Alternative')
                    print(starting_pos_x, starting_pos_y)
                    new_dungeon_rect = self.create_node(starting_pos_x, starting_pos_y)
                    self.stage_rect_dungeon_node.append(new_dungeon_rect)
                current_helper_index += 1

            if stage_node.dungeon_node is not None:
                starting_pos_x = self.stage_rect_node_list[stage_index].x + round(
                    (self.basic_step * stage_node.properties.number_of_battles) / 2)
                starting_pos_y = self.stage_rect_node_list[stage_index].y + round(
                    (self.basic_step * stage_node.properties.number_of_battles) / 2)

                print('Has Dungeon Node Linked to Stage Node')
                print(starting_pos_x, starting_pos_y)
                new_dungeon_rect = self.create_node(starting_pos_x, starting_pos_y)
                self.stage_rect_dungeon_node.append(new_dungeon_rect)

    def display_dungeon_node_bindings(self):
        alternative_path_index = 0
        dungeon_alternative_index = 0
        for index, stage_rect_node in enumerate(self.stage_rect_node_list):
            if self.current_realm_map[index].right_child is not None:
                if self.current_realm_map[index].right_child.dungeon_node is not None:

                    current_stage_alternative_center = self.stage_rect_alternative_node_list[alternative_path_index].center
                    current_stage_dungeon_center = self.stage_rect_dungeon_node[dungeon_alternative_index].center

                    draw.line(self.surface, Color('Brown'), current_stage_alternative_center, current_stage_dungeon_center,
                              int(self.binding_height * 1.5))
                    draw.line(self.surface, Color('Tomato'), current_stage_alternative_center, current_stage_dungeon_center,
                              int(self.binding_height / 1.2))

                    dungeon_alternative_index += 1
                alternative_path_index += 1

            if self.current_realm_map[index].dungeon_node is not None:
                current_stage_node_center = stage_rect_node.center
                current_stage_dungeon_center = self.stage_rect_dungeon_node[dungeon_alternative_index].center
                draw.line(self.surface, Color('Brown'), current_stage_node_center, current_stage_dungeon_center,
                          int(self.binding_height * 1.5))
                draw.line(self.surface, Color('Tomato'), current_stage_node_center, current_stage_dungeon_center,
                          int(self.binding_height / 1.2))

                dungeon_alternative_index += 1

    def generate_alternative_node_position(self):
        for stage_index, stage_node in enumerate(self.current_realm_map):
            starting_pos_x = self.stage_rect_node_list[stage_index].x + round(
                (self.basic_step * stage_node.properties.number_of_battles) / 2)
            starting_pos_y = self.stage_rect_node_list[stage_index].y - round(
                (self.basic_step * stage_node.properties.number_of_battles) / 2)

            if stage_node.right_child is not None:
                new_alternative_node = self.create_node(starting_pos_x, starting_pos_y)
                self.stage_rect_alternative_node_list.append(new_alternative_node)

    def display_alternative_node_bindings(self):
        alternative_path_index = 0
        for index, stage_rect_node in enumerate(self.stage_rect_node_list):
            if self.current_realm_map[index].right_child is not None:
                current_stage_node_center = stage_rect_node.center
                current_stage_alternative_center = self.stage_rect_alternative_node_list[alternative_path_index].center
                draw.line(self.surface, Color('Brown'), current_stage_node_center, current_stage_alternative_center,
                          int(self.binding_height * 1.5))
                draw.line(self.surface, Color('Tomato'), current_stage_node_center, current_stage_alternative_center,
                          int(self.binding_height / 1.2))

                alternative_path_index += 1

    def generate_main_line_node_position(self):
        starting_pos_x = self.starting_node_position_x
        for stage_node in self.current_realm_map:
            new_stage_node = self.create_node(starting_pos_x, self.starting_node_position_y)
            self.add_stage_node(new_stage_node)
            starting_pos_x += self.basic_step * stage_node.properties.number_of_battles
            self.total_steps += starting_pos_x

    def display_main_line_node_bindings(self):
        previous_stage_node_center = None
        for index, stage_rect_node in enumerate(self.stage_rect_node_list):
            current_stage_node_center = stage_rect_node.center
            if previous_stage_node_center is not None:
                draw.line(self.surface, Color('Brown'), previous_stage_node_center, current_stage_node_center,
                          self.binding_height)
                draw.line(self.surface, Color('Tomato'), previous_stage_node_center, current_stage_node_center,
                          int(self.binding_height / 2))
            previous_stage_node_center = current_stage_node_center

    def display_alternative_node_positions(self):
        for alternative_stage_rect_node in self.stage_rect_alternative_node_list:
            draw.rect(self.surface, Color('LightYellow'), alternative_stage_rect_node)

    def display_dungeon_node_positions(self):
        for dungeon_stage_rect_node in self.stage_rect_dungeon_node:
            draw.rect(self.surface, Color('LightPink'), dungeon_stage_rect_node)

    def display_main_line_node_positions(self):
        for stage_rect_node in self.stage_rect_node_list:
            draw.rect(self.surface, Color('LightBlue'), stage_rect_node)

    def display_graph_map(self):
        self.display_dungeon_node_bindings()
        self.display_dungeon_node_positions()
        self.display_alternative_node_bindings()
        self.display_alternative_node_positions()
        self.display_main_line_node_bindings()
        self.display_main_line_node_positions()

    def get_mouse_over_stage(self):
        for stage_node_index, stage_rect_node in enumerate(self.stage_rect_node_list):
            if stage_rect_node.collidepoint(mouse.get_pos()):
                # print(stage_rect_node, stage_node_index)
                return stage_node_index, stage_rect_node
        return None, None

    def get_mouse_click_stage(self):
        stage_node_index, stage_node_rect = self.get_mouse_over_stage()
        if stage_node_index is not None:
            if mouse.get_pressed(num_buttons=3)[0] and self.debounce_time():
                print('click')
                self.last_updated = time.get_ticks()
                return stage_node_index, stage_node_rect
        return None, None

    def update_last_time(self):
        self.last_updated = time.get_ticks()

    def debounce_time(self, interval=600):
        return time.get_ticks() - self.last_updated >= interval


list_of_nodes = ['Forest', 'Castle', 'Desert', 'Tombs']


class MapGraphNavigator:
    def __init__(self, surface, full_world_map, current_realm_index):
        self.map_font_path = '../../../../resources/fonts/Tahoma.ttf'
        self.map_font = font.Font(self.map_font_path, 15)
        self.map_font.set_bold(True)
        self.last_updated = 0

        self.surface = surface

        self.last_updated = 0

        self.current_node_index = 0
        self.full_world_map = full_world_map
        self.current_realm = self.full_world_map[current_realm_index]

        self.map_graph_generator = MapGraphDrawer(self.surface)
        self.map_graph_generator.set_current_realm(self.current_realm)
        self.map_graph_generator.generate_main_line_node_position()
        self.map_graph_generator.generate_alternative_node_position()
        self.map_graph_generator.generate_dungeon_node_position()

        self.navigation_rect = Rect(self.map_graph_generator.starting_node_position_x,
                                    self.map_graph_generator.starting_node_position_y, 30, 30)

    def navigate_world_map(self):
        pass

    def update_current_realm(self, current_realm_index):
        self.current_realm = self.full_world_map[current_realm_index]
        self.map_graph_generator.set_current_realm(self.current_realm)
        self.map_graph_generator.generate_main_line_node_position()

    def debounce_time(self, interval=600):
        return time.get_ticks() - self.last_updated >= interval

    def navigate_to_previous_stage_node(self):
        if self.current_node_index > 0:
            # First Update the Index to the proper step Previous Node
            self.current_node_index -= 1

            # Get current stage node properties
            current_stage_node_properties = self.current_realm[self.current_node_index].properties

            # Establish the basic_step * number_of_battles
            current_step_size = self.map_graph_generator.basic_step * current_stage_node_properties.number_of_battles

            # Move Distance
            self.navigation_rect.x -= current_step_size
            if self.navigation_rect.x < self.map_graph_generator.starting_node_position_x:
                self.navigation_rect.x = self.map_graph_generator.starting_node_position_x

    def navigate_to_next_stage_node(self):
        if self.current_node_index < len(self.current_realm) - 1:
            # Get current stage node properties
            current_stage_node_properties = self.current_realm[self.current_node_index].properties

            # Establish the basic_step * number_of_battles
            current_step_size = self.map_graph_generator.basic_step * current_stage_node_properties.number_of_battles

            # Update Rect Navigation Position
            self.navigation_rect.x += current_step_size
            if self.navigation_rect.x > self.map_graph_generator.total_steps:
                self.navigation_rect.x = self.map_graph_generator.total_steps

            # Lastly Update the Index to the proper step Next Node
            self.current_node_index += 1

    def navigate(self):
        keys = key.get_pressed()

        # Navigate to Previous Stage Node
        if (keys[K_a] or keys[K_LEFT]) and self.debounce_time():
            self.navigate_to_previous_stage_node()

            # Update last_updated for debounce time
            self.last_updated = time.get_ticks()

        # Navigate to Next Stage Node
        if (keys[K_d] or keys[K_RIGHT]) and self.debounce_time():
            self.navigate_to_next_stage_node()

            # Update last_updated for debounce time
            self.last_updated = time.get_ticks()

        if (keys[K_SPACE] or keys[K_RETURN]) and self.debounce_time():
            print('Entering',
                  f'[ Stage {self.current_realm[self.current_node_index].name} '
                  f'{self.current_realm[self.current_node_index].node_index} ]',
                  '...')
            self.last_updated = time.get_ticks()

    def select_node_via_click(self):
        stage_node_index, stage_node_rect = self.map_graph_generator.get_mouse_click_stage()
        if stage_node_index is not None:
            self.current_node_index = stage_node_index
            self.navigation_rect.x = stage_node_rect.x
            self.navigation_rect.y = stage_node_rect.y

    def display_navigation_rect(self):
        draw.rect(self.surface, Color('Cyan'), self.navigation_rect)

    def display(self):
        self.navigate()
        self.map_graph_generator.display_graph_map()
        self.display_navigation_rect()
        self.display_mouse_over_rect()
        self.display_stage_information()
        self.select_node_via_click()

    def display_stage_information(self):
        stage_node_index, stage_node_rect = self.map_graph_generator.get_mouse_over_stage()
        if stage_node_rect is not None:
            self.stage_node_information(stage_node_index)
        else:
            self.stage_node_information(self.current_node_index)

    def stage_node_information(self, stage_node_index):
        stage_node_data = self.current_realm[stage_node_index]
        self.surface.blit(
            self.map_font.render(f'[ Stage {stage_node_data.name} {stage_node_data.node_index} ]', True, (255, 0, 0)),
            (200, 100))

    def mouse_over_effect(self, stage_node_x, stage_node_y):
        mouse_over = Surface((30, 30), SRCALPHA, 32)
        mouse_over.set_alpha(100)
        mouse_over.fill(Color('Green'))
        self.surface.blit(mouse_over, (stage_node_x, stage_node_y))
        rect_hover = Rect(stage_node_x, stage_node_y, 30, 30)
        draw.rect(self.surface, Color('Tomato'), rect_hover, 2)

    def display_mouse_over_rect(self):
        stage_node_index, stage_node_rect = self.map_graph_generator.get_mouse_over_stage()
        if stage_node_rect is not None:
            self.mouse_over_effect(stage_node_rect.x, stage_node_rect.y)
