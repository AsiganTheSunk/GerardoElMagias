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
    def __init__(self, x, y, value, max_value, size_x=160, size_y=15,
                 color=MEDIUM_GREEN_COLOR, background_color=GRAY_COLOR, transition_color=RED_COLOR):
        super().__init__()
        self.x = x
        self.y = y

        self.size_x = size_x
        self.size_y = size_y

        self.color = color
        self.background_color = background_color
        self.transition_color = transition_color

        self.resource_value = value
        self.max_value = max_value
        self.last_value = value

        self.upper_step = 0
        self.effect_upper_ratio = 0

        self.effect_lower_ratio = 0

        # Shake Offsets
        self.offset_y = 0
        self.offset_x = 0

        # Effects Cycles
        self.shake_effect_cycles = 0
        self.upper_effect_cycles = 0

        # Debounce Times
        self.last_update_shake_effect = 0
        self.last_upper_update_effect = 0

        self.percentage_value_change = 0

        self.state = UIResourceBarState.NEUTRAL
        self.gain_resource = None

    def default(self):
        ratio = self.resource_value / self.max_value
        self.add_ui_element(UIRect(self.x, self.y, self.size_x, self.size_y, color=GRAY_COLOR))
        self.add_ui_element(UIRect(self.x, self.y, self.size_x * ratio, self.size_y, color=MEDIUM_GREEN_COLOR))

    def draw(self, value, max_value, surface):
        self.value_difference(value)

        self.update_shake_effect()
        self.update_upper_effect(value)

        ratio = value / self.max_value
        self.resource_value = value
        self.max_value = max_value

        draw.rect(surface, GRAY_COLOR, (self.x + self.offset_x, self.y + self.offset_y,
                                        self.size_x, self.size_y))
        if self.state is UIResourceBarState.GAINING:
            draw.rect(surface, Color('DarkSeaGreen4'), (self.x + self.offset_x, self.y + self.offset_y,
                                                        self.size_x * ratio, self.size_y))
            draw.rect(surface, MEDIUM_GREEN_COLOR, (self.x + self.offset_x, self.y + self.offset_y,
                                                    self.size_x * self.effect_upper_ratio, self.size_y))
        elif self.state is UIResourceBarState.LOOSING:
            draw.rect(surface, Color('FireBrick2'), (self.x + self.offset_x, self.y + self.offset_y,
                                                     self.size_x * self.effect_lower_ratio, self.size_y))
            draw.rect(surface, Color('Tomato'), (self.x + self.offset_x, self.y + self.offset_y,
                                                 self.size_x * self.effect_upper_ratio, self.size_y))
            draw.rect(surface, MEDIUM_GREEN_COLOR, (self.x + self.offset_x, self.y + self.offset_y,
                                                    self.size_x * ratio, self.size_y))
        elif self.state is UIResourceBarState.NEUTRAL:
            draw.rect(surface, MEDIUM_GREEN_COLOR, (self.x + self.offset_x, self.y + self.offset_y,
                                                    self.size_x * ratio, self.size_y))

    def value_difference(self, current_value):
        self.last_value = self.resource_value

        if self.resource_value > current_value:
            self.state = UIResourceBarState.LOOSING
            self.shake_effect_cycles = 3

            self.effect_lower_ratio = self.last_value / self.max_value
            self.percentage_value_change = (self.last_value / self.max_value) - \
                                           (current_value / self.max_value)

            if self.percentage_value_change > 0.60:
                self.upper_effect_cycles = 20
            else:
                self.upper_effect_cycles = 10
            self.upper_step = self.percentage_value_change / self.upper_effect_cycles

        elif self.resource_value < current_value:
            self.state = UIResourceBarState.GAINING

            self.percentage_value_change = (self.last_value / self.max_value) - \
                                           (current_value / self.max_value)

            if self.percentage_value_change > 0.60:
                self.upper_effect_cycles = 30
            else:
                self.upper_effect_cycles = 20
            self.upper_step = self.percentage_value_change / self.upper_effect_cycles

    def update_shake_effect(self):
        if self.debounce_shake_effect_time():
            if self.shake_effect_cycles >= 1:
                self.shake_effect_cycles -= 1
                self.offset_x = randint(-3, 3)
                self.offset_y = randint(-3, 3)
            else:
                self.offset_x = 0
                self.offset_y = 0

            self.last_update_shake_effect = time.get_ticks()

    def update_upper_effect(self, current_resource):
        if self.debounce_upper_effect_time():
            if self.upper_effect_cycles >= 1:

                self.upper_effect_cycles -= 1
                self.effect_upper_ratio = \
                    (self.upper_step * self.upper_effect_cycles) + (current_resource / self.max_value)

            elif self.upper_effect_cycles == 0:
                self.state = UIResourceBarState.NEUTRAL

            self.last_upper_update_effect = time.get_ticks()

    def debounce_shake_effect_time(self, interval=50):
        return time.get_ticks() - self.last_update_shake_effect >= interval

    def debounce_upper_effect_time(self, interval=50):
        return time.get_ticks() - self.last_upper_update_effect >= interval

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

