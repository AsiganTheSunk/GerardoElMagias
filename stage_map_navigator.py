from pygame import font, init, time, key, mouse, draw, Color, Rect, event as pygame_events, MOUSEBUTTONUP, \
    QUIT, K_LEFT, K_a, K_RIGHT, K_d, K_SPACE, K_RETURN, display


# basic_step = 25
# total_steps = 0
# for realm in normal_world[0]:
#     print(realm.name, realm.node_index, realm.properties.number_of_battles)
#     current_step = basic_step * realm.properties.number_of_battles
#     total_steps += basic_step * realm.properties.number_of_battles
#     print(current_step)
# print(total_steps)


class MapGraphDrawer:
    def __init__(self, surface):
        self.surface = surface
        self.current_realm_map = None
        self.basic_step = 25        # 25px

        self.stage_binding_list = []
        self.stage_rect_node_list = []

        self.binding_height = 4
        self.starting_node_position_x = 100
        self.starting_node_position_y = 250

        self.last_updated = 0
        self.total_steps = 0

    # def draw_circle(self):
    #     draw.circle(self.surface, Color('Blue'), mouse.get_pos(), 20)

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
                draw.line(self.surface, Color('Brown'), previous_stage_node_center, current_stage_node_center, self.binding_height)
            previous_stage_node_center = current_stage_node_center

    def display_main_line_node_positions(self):
        for stage_rect_node in self.stage_rect_node_list:
            draw.rect(self.surface, Color('LightBlue'), stage_rect_node)

    def display_graph_map(self):
        self.display_main_line_node_bindings()
        self.display_main_line_node_positions()

    def mouse_click(self):
        for stage_node_index, stage_rect_node in enumerate(self.stage_rect_node_list):
            if stage_rect_node.collidepoint(mouse.get_pos()) and self.debounce_time():
                print(stage_rect_node, stage_node_index)
                self.update_last_time()
                return stage_rect_node, self.current_realm_map[stage_node_index]

        return None, None

    def mouse_over(self):
        for stage_node_index, stage_rect_node in enumerate(self.stage_rect_node_list):
            if stage_rect_node.collidepoint(mouse.get_pos()):
                return self.current_realm_map[stage_node_index]
        return None

    def update_last_time(self):
        self.last_updated = time.get_ticks()

    def debounce_time(self, interval=600):
        return time.get_ticks() - self.last_updated >= interval


list_of_nodes = ['Forest', 'Castle', 'Desert', 'Tombs']


class MapGraphNavigator:
    def __init__(self, surface, full_world_map, current_realm_index):
        self.map_font_path = './resources/fonts/Tahoma.ttf'
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

        self.navigation_rect = Rect(self.map_graph_generator.starting_node_position_x,
                                    self.map_graph_generator.starting_node_position_y, 30, 30)

    def update_current_realm(self, current_realm_index):
        self.current_realm = self.full_world_map[current_realm_index]
        self.map_graph_generator.set_current_realm(self.current_realm)
        self.map_graph_generator.generate_main_line_node_position()

    def debounce_time(self, interval=600):
        return time.get_ticks() - self.last_updated >= interval

    def move_to_next_stage_node(self):
        pass

    def move_to_previous_stage_node(self):
        pass


    def calculate_previous_step(self):
        if self.current_node_index > 0:
            self.current_node_index -= 1
            # Get current stage node properties before adding 1 to the index
            current_stage_node_properties = self.current_realm[self.current_node_index].properties

            # Establish the basic_step * number_of_battles
            current_step_size = self.map_graph_generator.basic_step * current_stage_node_properties.number_of_battles

            print('C. Node Index:', self.current_node_index, 'Step Size: ', current_step_size, 'Number Of Battles:',
                  current_stage_node_properties.number_of_battles)

            # Lastly Update the Index to the proper step

            # Move Distance
            self.navigation_rect.x -= current_step_size
            if self.navigation_rect.x < self.map_graph_generator.starting_node_position_x:
                self.navigation_rect.x = self.map_graph_generator.starting_node_position_x

        else:
            print('Principio')


            # print(self.navigation_rect.x)
            self.last_updated = time.get_ticks()


    def calculate_next_step(self):
        if self.current_node_index < len(self.current_realm) - 1:
            # Get current stage node properties before adding 1 to the index
            current_stage_node_properties = self.current_realm[self.current_node_index].properties

            # Establish the basic_step * number_of_battles
            current_step_size = self.map_graph_generator.basic_step * current_stage_node_properties.number_of_battles

            print('C. Node Index:', self.current_node_index, 'Step Size: ', current_step_size, 'Number Of Battles:',
                  current_stage_node_properties.number_of_battles)

            # Update Rect Navigation Position
            self.navigation_rect.x += current_step_size
            if self.navigation_rect.x > self.map_graph_generator.total_steps:
                self.navigation_rect.x = self.map_graph_generator.total_steps

            # Lastly Update the Index to the proper step
            self.current_node_index += 1
        else:
            print('Final')

        # Update last_updated for debounce time
        self.last_updated = time.get_ticks()





    def navigate(self):
        keys = key.get_pressed()
        ev = pygame_events.get()

        current_stage_node_rect = self.map_graph_generator.stage_rect_node_list[self.current_node_index]
        current_stage_node = self.map_graph_generator.current_realm_map[self.current_node_index]


        #
        # for event in ev:
        #     if event.type == MOUSEBUTTONUP:
        #         stage_node_rect, stage_node_data = self.map_graph_generator.mouse_click()
        #         if stage_node_rect is not None:
        #             self.navigation_rect.x = stage_node_rect.x
        #
        #     if event.type == QUIT:
        #         # Todo: Return to World Map
        #         running = False

        if (keys[K_a] or keys[K_LEFT]) and self.debounce_time():  # to move left
            print('press A')
            self.calculate_previous_step()


            # print(self.navigation_rect.x)
            self.last_updated = time.get_ticks()

        if (keys[K_d] or keys[K_RIGHT]) and self.debounce_time():
            print('press D')
            self.calculate_next_step()

        if (keys[K_SPACE] or keys[K_RETURN]) and self.debounce_time():
            # to move right
            # print('Entering', '[ ' + list_of_nodes[index_to_draw].name + ' ]', '....')
            print('Entering', '[ Stage ]', '....')
            self.last_updated = time.get_ticks()

        # self.display_navigation_box()

    def display_navigation_box(self):
        # print(self.navigation_rect.x, self.navigation_rect.y)
        draw.rect(self.surface, Color('Cyan'), self.navigation_rect)

    def display(self):
        self.map_graph_generator.display_graph_map()
        starting_stage_position_x = self.map_graph_generator.starting_node_position_x
        starting_stage_position_y = self.map_graph_generator.starting_node_position_y

    def perform_mouse_over_action(self):
        stage_node_rect, stage_node_data = self.map_graph_generator.mouse_click()
        if stage_node_rect is not None:
            rect_hover = Rect(stage_node_rect.x, stage_node_rect.y, 30, 30)
            draw.rect(self.surface, (100, 100, 20), rect_hover)
            # display.update()

    def stage_node_header_information(self):
        stage_node_rect, stage_node_data = self.map_graph_generator.mouse_click()
        if stage_node_rect is not None:
            self.surface.blit(self.map_font.render(
                f'[ Stage {stage_node_data.name} {stage_node_data.node_index} ]', True, (255, 0, 0)), (200, 100))


    # def navigate(self):
    #     ev = pygame.event.get()
    #     self.map_drawer.display_node(screen)

