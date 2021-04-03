#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mouse, transform, Surface, time, SRCALPHA, font, Color, surfarray, draw, display, Rect
from numpy import array
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_button import UIButton
from interface.ui_elements.ui_image import UIImage
from interface.ui_elements.ui_text_element import UITextElement
from interface.ui_elements.ui_rect import UIRect


class UITextButton(UILayout):
    def __init__(self, ui_identifier, x, y, image, image_width, image_height, text_message='',
                 text_color=Color('Black'), text_font_size=10, text_font='./resources/fonts/Verdana.ttf',
                 text_placement='center', show_text=True):
        super().__init__()
        self.text_color = text_color
        self.text_message = text_message
        self.text_font = font.Font(text_font, text_font_size)
        self.text_font.set_bold(True)
        self.text_placement = text_placement

        self.button = UIButton(ui_identifier, x, y, image, image_width, image_height)

        self.key_bind = None
        self.last_update = 0
        self.show_text = show_text

        self.reset()

    def activate(self):
        self.button.active = True

    def deactivate(self):
        self.button.active = False

    def add(self, ui_button_element):
        self.elements.append(ui_button_element)

    def update(self):
        if self.debounce_time():
            self.button.clicked = False
            self.reset()

    def reset(self):
        text_x, text_y = self.button_text_placement()
        self.elements = [
            UIRect(self.button.x - 1, self.button.y - 1,
                   self.button.image_width + 2, self.button.image_height + 2, color=Color('DarkBlue')),
            self.button,
            UITextElement(self.text_message, (text_x, text_y))
        ]

    def handle_on_click_event(self, event, button):
        if mouse.get_pressed(num_buttons=3)[0]:
            self.button.clicked = True

            if not self.button.active:
                inactive_image = self.grayscale(self.button.image)
                self.add(UIImage(inactive_image, inactive_image.get_width(), inactive_image.get_height()))
                # self.surface.blit(inactive_image, (self.rect.x, self.rect.y))

            if self.show_text:
                text_x, text_y = self.button_text_placement()
                if not self.active:
                    self.add(UITextElement(self.text_message, (text_x, text_y)))
                else:
                    self.add(UITextElement(self.text_message, (text_x, text_y), color=Color('Tomato')))

            if self.debounce_time():
                self.last_update = time.get_ticks()

    def handle_mouse_over_event(self, event, button):
        pass

    def button_text_placement(self):
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

    def debounce_time(self, interval=200):
        return time.get_ticks() - self.last_update >= interval

    @staticmethod
    def grayscale(img):
        arr = surfarray.array3d(img)
        # Luminosity Filter
        avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
        arr = array([[[avg, avg, avg] for avg in col] for col in avgs])
        return surfarray.make_surface(arr)
