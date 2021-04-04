#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import time, font, Color, mouse

from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_button import UIButton
from interface.ui_elements.ui_text_element import UITextElement
from interface.ui_elements.ui_rect import UIRect
from interface.ui_elements.ui_transparent_rect import UITransparentRect


class UITextButton(UILayout):
    def __init__(self, ui_identifier, x, y, image, image_width, image_height, text_message='',
                 text_color=Color('White'), text_font_size=10, text_font='./resources/fonts/Verdana.ttf',
                 text_placement='center', show_text=True, background=True):
        super().__init__()

        self.text_color = text_color
        self.text_message = text_message
        self.text_font = font.Font(text_font, text_font_size)
        self.text_font.set_bold(True)
        self.text_placement = text_placement

        self.button = UIButton(ui_identifier, x, y, image, image_width, image_height)
        self.background = background
        self.key_bind = None
        self.last_update = 0
        self.show_text = show_text
        self.reset_ui_elements()

    def activate(self):
        self.button.active = True

    def deactivate(self):
        self.button.active = False

    def add(self, ui_button_element):
        self.elements.append(ui_button_element)

    def reset_ui_elements(self):
        self.elements = []

        self.default_button()
        if self.button.mouse_over:
            self.mouse_over_effect()

        if self.button.clicked:
            self.click_effect()

    def update(self):
        if self.debounce_time():
            self.button.clicked = mouse.get_pressed(num_buttons=3)[0] and self.button.rect.collidepoint(mouse.get_pos())
            self.button.mouse_over = self.button.rect.collidepoint(mouse.get_pos())
            self.reset_ui_elements()

    def default_button(self):
        if self.background:
            self.add(UIRect(self.button.x - 1, self.button.y - 1, self.button.image_width + 2, self.button.image_height + 2, color=Color('DarkBlue')))
        self.add(self.button)
        self.button_text()

    def button_text(self):
        text_x, text_y = self.get_text_placement()
        if self.show_text:
            self.add(UITextElement(self.text_message, (text_x, text_y)))

    def clicked_button_text_effect(self):
        if self.show_text:
            text_x, text_y = self.get_text_placement()
            self.add(UITextElement(self.text_message, (text_x, text_y), color=Color('Tomato')))

    def click_effect(self):
        self.add(UIRect(self.button.x - 1, self.button.y - 1, self.button.image_width, self.button.image_height, 2,
                        color=Color('Pink')))
        self.clicked_button_text_effect()

    def mouse_over_effect(self):
        self.add(UITransparentRect(self.button.x, self.button.y, self.button.image_width, self.button.image_height))
        self.add(UIRect(self.button.x - 1, self.button.y - 1, self.button.image_width, self.button.image_height, 2,
                        color=Color('Green')))

    def get_text_placement(self):
        text_width, text_height = self.text_font.size(self.text_message)
        center_x, center_y = self.button.rect.center
        if self.text_placement == 'center':
            return (center_x - text_width/2), (center_y - text_height/2)
        elif self.text_placement == 'bottom_center':
            return (center_x - text_width/2), (center_y + text_height - 2)
        elif self.text_placement == 'bottom_under':
            return (center_x - text_width/2), (center_y + self.button.image_height/2)
        elif self.text_placement == 'top_center':
            return (center_x - text_width/2), (center_y - self.button.image_height/2 - 2)
        elif self.text_placement == 'top_over':
            return (center_x - text_width/2), (self.button.rect.y - text_height - 2)

    def debounce_time(self, interval=50):
        return time.get_ticks() - self.last_update >= interval
