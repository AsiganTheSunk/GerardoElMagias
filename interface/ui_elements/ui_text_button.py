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
                 text_placement='center'):
        super().__init__()

        self.button = UIButton(ui_identifier, x, y, image, image_width, image_height)

        self.text_color = text_color
        self.text_message = text_message
        self.text_font = font.Font(text_font, text_font_size)
        self.text_font.set_bold(True)
        self.text_placement = text_placement

        # self.surface = surface
        self.last_update = 0

        self.key_bind = None
        self.button_status = True

        self.show_text = True

        text_x, text_y = self.button_text_placement()

        self.elements = [
            self.button,
            UITextElement(self.text_message, (text_x, text_y))
        ]

    def activate(self):
        self.button.active = True

    def deactivate(self):
        self.button.active = False

    def add(self, ui_button_element):
        self.elements.append(ui_button_element)

    def update_button_status(self):
        if self.debounce_time(interval=200):
            self.button.clicked = False
            self.reset()

    def reset(self):
        text_x, text_y = self.button_text_placement()

        self.elements = [
            self.button,
            UITextElement(self.text_message, (text_x, text_y))
        ]

    def handle_on_click_event(self, event, button):
        print('entra aqui')
        if mouse.get_pressed(num_buttons=3)[0]:
            self.button.clicked = True

            self.add(UIRect(Color('Blue'), self.button.x, self.button.y, self.button.image_width + 10, self.button.image_height + 10, 2))
            if not self.button.active:
                inactive_image = self.grayscale(self.button.image)
                self.add(UIImage(inactive_image, inactive_image.get_width(), inactive_image.get_height()))
                # self.surface.blit(inactive_image, (self.rect.x, self.rect.y))

            if self.show_text:
                text_x, text_y = self.button_text_placement()
                if not self.active:
                    self.add(UITextElement(self.text_message, (text_x, text_y)))
                    # self.surface.blit(self.text_font.render(self.text_message, True, Color('White')), (text_x, text_y))
                else:
                    self.add(UITextElement(self.text_message, (text_x, text_y), color=Color('Tomato')))
                    # self.surface.blit(self.text_font.render(self.text_message, True, Color('Tomato')),  (text_x, text_y))

            if self.debounce_time():
                self.last_update = time.get_ticks()
        #         return True
        # return False

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

    # def mouse_over_effect(self):
    #     mouse_over = Surface((self.button.image_width, self.button.image_width), SRCALPHA, 32)
    #     mouse_over.set_alpha(100)
    #     mouse_over.fill(Color('LightBlue'))
    #
    #     self.surface.blit(mouse_over, (self.rect.x, self.rect.y))
    #     draw.rect(self.surface, Color('Blue'), (self.rect.x, self.rect.y, self.image_width+1, self.image_height+1), 2)
    #
    # def is_hover(self):
    #     if self.mouse_collide():
    #         self.mouse_over_effect()
    #


    def debounce_time(self, interval=500):
        return time.get_ticks() - self.last_update >= interval

    @staticmethod
    def grayscale(img):
        arr = surfarray.array3d(img)
        # Luminosity Filter
        avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
        arr = array([[[avg, avg, avg] for avg in col] for col in avgs])
        return surfarray.make_surface(arr)
