from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_rect import UIRect
from constants.game_colors import GRAY_COLOR, MEDIUM_GREEN_COLOR
from pygame import time, draw, Color
from random import randint


from enum import Enum


class UIResourceBarState(Enum):
    NEUTRAL = 'Neutral'
    GAINING = 'Gaining'
    LOOSING = 'Loosing'


class UIResourceBar(UILayout):
    def __init__(self, x, y, value, max_value, size_x=160, size_y=15, color=MEDIUM_GREEN_COLOR,
                 bg_color=GRAY_COLOR, tl1_color=Color('FireBrick2'), tl2_color=Color('Tomato'),
                 tg1_color=Color('DarkSeaGreen4'), shake_effect_status=True):
        super().__init__()
        self.x = x
        self.y = y

        self.size_x = size_x
        self.size_y = size_y

        self.color = color
        self.bg_color = bg_color
        self.tl1_color = tl1_color
        self.tl2_color = tl2_color
        self.tg1_color = tg1_color

        self.resource_value = value
        self.max_value = max_value
        self.last_value = value

        self.upper_step = 0
        self.effect_upper_ratio = 0

        self.ratio = 0
        self.tg1_ratio = 0

        # Shake Offsets
        self.offset_y = 0
        self.offset_x = 0

        # Effects Cycles
        self.shake_effect_status = shake_effect_status
        self.shake_effect_cycles = 0
        self.upper_effect_cycles = 0

        # Debounce Times
        self.last_update_shake_effect = 0
        self.last_upper_update_effect = 0

        self.percentage_value_change = 0

        self.state = UIResourceBarState.NEUTRAL
        self.gain_resource = None

    # def default(self):
    #     ratio = self.resource_value / self.max_value
    #     self.add_ui_element(UIRect(self.x, self.y, self.size_x, self.size_y, color=GRAY_COLOR))
    #     self.add_ui_element(UIRect(self.x, self.y, self.size_x * ratio, self.size_y, color=MEDIUM_GREEN_COLOR))

    # self.reset_ui_elements()
    # self.add_ui_element(UIRect(self.x + self.offset_x, self.y + self.offset_y,
    #                            self.size_x, self.size_y, color=GRAY_COLOR))
    # self.add_ui_element(UIRect(self.x + self.offset_x, self.y + self.offset_y,
    #                            self.size_x * ratio, self.size_y, color=RED_COLOR))
    # self.add_ui_element(UIRect(self.x + self.offset_x, self.y + self.offset_y,
    #                            self.size_x * ratio, self.size_y, color=GREEN_COLOR))

    def draw(self, value, max_value, surface):
        self.value_difference(value)

        if self.shake_effect_status:
            self.update_shake_effect()
        self.update_upper_effect(value)

        self.ratio = value / self.max_value
        self.resource_value = value
        self.max_value = max_value

        self.manage_resource_state(surface)

    def manage_resource_state(self, surface):
        # Background Color
        draw.rect(surface, self.bg_color, (self.x + self.offset_x, self.y + self.offset_y,
                                           self.size_x, self.size_y))
        if self.state is UIResourceBarState.GAINING:
            # Darker: Resource Gain
            draw.rect(surface, self.tg1_color, (self.x + self.offset_x, self.y + self.offset_y,
                                                self.size_x * self.ratio, self.size_y))
            # Lighter: Transitioning Resource Gain
            draw.rect(surface, self.color, (self.x + self.offset_x, self.y + self.offset_y,
                                            self.size_x * self.effect_upper_ratio, self.size_y))
        elif self.state is UIResourceBarState.LOOSING:
            # Darker: Resource Loss
            draw.rect(surface, self.tl1_color, (self.x + self.offset_x, self.y + self.offset_y,
                                                self.size_x * self.tg1_ratio, self.size_y))
            # Lighter: Transitioning Resource Loss
            draw.rect(surface, self.tl2_color, (self.x + self.offset_x, self.y + self.offset_y,
                                                self.size_x * self.effect_upper_ratio, self.size_y))
            draw.rect(surface, self.color, (self.x + self.offset_x, self.y + self.offset_y,
                                            self.size_x * self.ratio, self.size_y))
        elif self.state is UIResourceBarState.NEUTRAL:
            # Default Color:
            draw.rect(surface, self.color, (self.x + self.offset_x, self.y + self.offset_y,
                                            self.size_x * self.ratio, self.size_y))

    def value_difference(self, current_value):
        self.last_value = self.resource_value

        if self.resource_value > current_value:
            # Update State of UIResourceBar, add Shake Effect Cycles
            self.state = UIResourceBarState.LOOSING
            self.shake_effect_cycles = 3

            # Establish Darker Resource Ratio
            self.tg1_ratio = self.last_value / self.max_value
            # Establish Percentage Change to be used in the Transition Color
            # Since this will report positive values, the effect will be reducing the current Resource
            self.percentage_value_change = (self.last_value / self.max_value) - \
                                           (current_value / self.max_value)
            # Establish Number of Transition Cycles based on Percentage Value Change
            if self.percentage_value_change > 0.60:
                self.upper_effect_cycles = 20
            else:
                self.upper_effect_cycles = 10

            # Establish Step for Light, UpperEffect
            self.upper_step = self.percentage_value_change / self.upper_effect_cycles

        elif self.resource_value < current_value:
            # Update State of UIResourceBar
            self.state = UIResourceBarState.GAINING

            # Establish Darker Resource Ratio
            # Since this will report negative values, the effect will be incrementing the current Resource
            self.percentage_value_change = (self.last_value / self.max_value) - \
                                           (current_value / self.max_value)

            # Establish Number of Transition Cycles based on Percentage Value Change
            if self.percentage_value_change > 0.60:
                self.upper_effect_cycles = 30
            else:
                self.upper_effect_cycles = 20

            # Establish Step for Light, UpperEffect
            self.upper_step = self.percentage_value_change / self.upper_effect_cycles

    def update_shake_effect(self):
        if self.debounce_shake_effect_time():
            if self.shake_effect_cycles >= 1:
                self.shake_effect_cycles -= 1
                # Establish Offset Variation for the Shake Effect
                self.offset_x = randint(-3, 3)
                self.offset_y = randint(-3, 3)
            else:
                # Reset Offsets
                self.offset_x = 0
                self.offset_y = 0

            self.last_update_shake_effect = time.get_ticks()

    def update_upper_effect(self, current_resource):
        if self.debounce_upper_effect_time():
            if self.upper_effect_cycles >= 1:
                self.upper_effect_cycles -= 1
                # Establish current Ratio for the Upper Effect, Lighter
                self.effect_upper_ratio = \
                    (self.upper_step * self.upper_effect_cycles) + (current_resource / self.max_value)

            elif self.upper_effect_cycles == 0:
                # Reset UIResource State to the Default State
                self.state = UIResourceBarState.NEUTRAL

            self.last_upper_update_effect = time.get_ticks()

    # Establish Timer for each Step to be Made during the Shake Effect
    def debounce_shake_effect_time(self, interval=50):
        return time.get_ticks() - self.last_update_shake_effect >= interval

    # Establish Timer for each Step to be Made during the Upper Effect
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

