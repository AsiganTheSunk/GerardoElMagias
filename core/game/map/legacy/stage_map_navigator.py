#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import font, init, time, key, mouse, draw, Color, Rect, event as pygame_events, MOUSEBUTTONUP, \
    QUIT, K_LEFT, K_a, K_RIGHT, K_d, K_SPACE, K_RETURN, display, Surface, SRCALPHA

from core.game.map.legacy.stage_map_renderer import MapGraphRenderer

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

        self.map_graph_generator = MapGraphRenderer(self.surface)
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
