from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_rect import UIRect
from constants.game_colors import GRAY_COLOR, MEDIUM_GREEN_COLOR, RED_COLOR
from pygame import time, draw, Color
from random import randint


# self.reset_ui_elements()
# self.add_ui_element(UIRect(self.x + self.offset_x, self.y + self.offset_y,
#                            self.size_x, self.size_y, color=GRAY_COLOR))
# self.add_ui_element(UIRect(self.x + self.offset_x, self.y + self.offset_y,
#                            self.size_x * ratio, self.size_y, color=RED_COLOR))
# self.add_ui_element(UIRect(self.x + self.offset_x, self.y + self.offset_y,
#                            self.size_x * ratio, self.size_y, color=GREEN_COLOR))

from enum import Enum


class UIResourceBarState(Enum):
    NEUTRAL = 'Neutral'
    GAINING = 'Gaining'
    LOOSING = 'Loosing'


class UIResourceBar(UILayout):
    def __init__(self, x, y, current_resource, max_resource, size_x=160, size_y=15,
                 color=MEDIUM_GREEN_COLOR, background_color=GRAY_COLOR, transition_color=RED_COLOR):
        super().__init__()
        self.x = x
        self.y = y

        self.size_x = size_x
        self.size_y = size_y

        self.color = color
        self.background_color = background_color
        self.transition_color = transition_color

        self.resource_value = current_resource
        self.max_resource_value = max_resource

        self.last_resource_value = current_resource
        self.dynamic_ratio = 0
        self.step = 0

        # Shake Offsets
        self.offset_y = 0
        self.offset_x = 0

        # Effects Cycles
        self.shake_effect_cycles = 0
        self.update_effect_cycles = 0

        # Debounce Times
        self.last_update_shake_effect = 0
        self.last_update_update_effect = 0
        self.resource_percentage_change = 0

        self.resource_state = UIResourceBarState.NEUTRAL
        self.gain_resource = None

    def default(self):
        ratio = self.resource_value / self.max_resource_value
        self.add_ui_element(UIRect(self.x, self.y, self.size_x, self.size_y, color=GRAY_COLOR))
        self.add_ui_element(UIRect(self.x, self.y, self.size_x * ratio, self.size_y, color=MEDIUM_GREEN_COLOR))

    def draw(self, resource_value, max_resource_value, surface):
        self.last_resource_value = self.resource_value
        self.evaluate_resource_diff(resource_value)

        self.shake_effect()
        self.update_effect(resource_value)

        self.resource_value = resource_value
        self.max_resource_value = max_resource_value

        ratio = self.resource_value / self.max_resource_value

        draw.rect(surface, GRAY_COLOR, (self.x + self.offset_x, self.y + self.offset_y, self.size_x, self.size_y))

        if self.resource_state is UIResourceBarState.GAINING:
            draw.rect(surface, Color('darkolivegreen4'), (self.x + self.offset_x, self.y + self.offset_y, self.size_x * ratio, self.size_y))
            draw.rect(surface, MEDIUM_GREEN_COLOR, (self.x + self.offset_x, self.y + self.offset_y, self.size_x * self.dynamic_ratio, self.size_y))
        elif self.resource_state is UIResourceBarState.LOOSING:
            draw.rect(surface, Color('Tomato'), (self.x + self.offset_x, self.y + self.offset_y, self.size_x * self.dynamic_ratio, self.size_y))
            draw.rect(surface, MEDIUM_GREEN_COLOR, (self.x + self.offset_x, self.y + self.offset_y, self.size_x * ratio, self.size_y))
        elif self.resource_state is UIResourceBarState.NEUTRAL:
            self.shake_effect_cycles = 0
            self.update_effect_cycles = 0

            draw.rect(surface, MEDIUM_GREEN_COLOR,
                      (self.x + self.offset_x, self.y + self.offset_y, self.size_x * ratio, self.size_y))

    def evaluate_resource_diff(self, current_value):

        if self.resource_value > current_value:
            self.resource_state = UIResourceBarState.LOOSING
            self.shake_effect_cycles = 3
            self.last_resource_value = self.resource_value
            self.resource_percentage_change = (self.last_resource_value / self.max_resource_value) - \
                                              (current_value / self.max_resource_value)

            if self.resource_percentage_change > 0.50:
                self.update_effect_cycles = 20
            else:
                self.update_effect_cycles = 10

            self.step = self.resource_percentage_change / self.update_effect_cycles

        elif self.resource_value < current_value:
            self.resource_state = UIResourceBarState.GAINING

            self.last_resource_value = self.resource_value
            self.resource_percentage_change = (self.last_resource_value / self.max_resource_value) - \
                                              (current_value / self.max_resource_value)

            if self.resource_percentage_change > 0.50:
                self.update_effect_cycles = 25
            else:
                self.update_effect_cycles = 15

            self.step = self.resource_percentage_change / self.update_effect_cycles

    def shake_effect(self):
        if self.debounce_shake_effect_time():
            if self.shake_effect_cycles >= 1:
                self.shake_effect_cycles -= 1
                self.offset_x = randint(-3, 3)
                self.offset_y = randint(-3, 3)
            else:
                self.offset_x = 0
                self.offset_y = 0

            self.last_update_shake_effect = time.get_ticks()

    def update_effect(self, current_resource):
        if self.debounce_update_effect_time():
            if self.update_effect_cycles >= 1:

                self.update_effect_cycles -= 1
                self.dynamic_ratio = (self.step * self.update_effect_cycles) + (current_resource / self.max_resource_value)

            elif self.update_effect_cycles == 0:
                self.resource_state = UIResourceBarState.NEUTRAL

            self.last_update_update_effect = time.get_ticks()

    def debounce_shake_effect_time(self, interval=50):
        return time.get_ticks() - self.last_update_shake_effect >= interval

    def debounce_update_effect_time(self, interval=30):
        return time.get_ticks() - self.last_update_update_effect >= interval

    # def get_text_placement(self):
    #     text_width, text_height = self.text_font.size(self.text_message)
    #     center_x, center_y = self.button.rect.center
    #     if self.text_placement == 'center':
    #         return (center_x - text_width/2), (center_y - text_height/2)
    #     elif self.text_placement == 'bottom_center':
    #         return (center_x - text_width/2), (center_y + text_height - 2)
    #     elif self.text_placement == 'bottom_under':
    #         return (center_x - text_width/2), (center_y + self.button.image_height/2)
    #     elif self.text_placement == 'top_center':
    #         return (center_x - text_width/2), (center_y - self.button.image_height/2 - 2)
    #     elif self.text_placement == 'top_over':
    #         return (center_x - text_width/2), (self.button.rect.y - text_height - 2)

