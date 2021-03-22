#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mouse, transform, Surface, time, SRCALPHA, font, Color, surfarray, draw, display, Rect
from numpy import array


class BasicButton:
    def __init__(self, surface, x, y, image, image_width, image_height, text_message='',
                 text_color=Color('Black'), text_font_size=10, text_font='./resources/fonts/Verdana.ttf'):
        self.x = x
        self.y = y

        self.image_width = image_width
        self.image_height = image_height

        self.text_color = text_color
        self.text_message = text_message
        self.text_font = font.Font(text_font, text_font_size)
        self.text_font.set_bold(True)

        self.image = transform.scale(image, (self.image_width, self.image_height))
        self.clicked_image = transform.scale(image, (self.image_width - 2, self.image_height - 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface
        self.last_update = 0

        self.button_status = True

    def button_text_placement(self, placement):
        if placement == 'center':
            # return (self.x + (self.image_width / 2)), (self.y + (self.image_height / 2))
            return (self.x + (self.image_width / 2)), (self.y - (self.image_height / 2))
        elif placement == 'under':
            pass

    def button_text(self, text, placement):
        pass

    def display_text(self):
        # Todo: Find bette fit
        text_width, text_height = self.text_font.size(self.text_message)
        self.surface.blit(
            self.text_font.render(self.text_message, True, self.text_color),
            ((self.x + (self.image_width / 2)) + text_width/2, (self.y + (self.image_height / 2) + text_height/2)))

    def display(self, show_text=False):
        # draw button
        if self.button_status:
            self.surface.blit(self.image, (self.rect.x, self.rect.y))
        else:
            inactive_image = self.grayscale(self.image)
            self.surface.blit(inactive_image, (self.rect.x, self.rect.y))

        if show_text:
            self.display_text()

    def mouse_collide(self):
        return self.rect.collidepoint(mouse.get_pos())

    def activate_button(self):
        self.button_status = True

    def deactivate_button(self):
        self.button_status = False

    def is_hover(self):
        if self.mouse_collide():
            mouse_over = Surface((self.image_width, self.image_width), SRCALPHA, 32)
            mouse_over.set_alpha(100)
            mouse_over.fill(Color('LightBlue'))
            self.surface.blit(mouse_over, (self.rect.x, self.rect.y))

    def click_animation(self):
        # Todo: find a way to create the proper push down animation
        pass

    def debounce_time(self, interval=500):
        return time.get_ticks() - self.last_update >= interval

    def is_clicked(self):
        if self.mouse_collide() and self.button_status:
            if mouse.get_pressed(num_buttons=3)[0] and self.debounce_time():
                self.last_update = time.get_ticks()
                return True
        return False

    def grayscale(self, img):
        arr = surfarray.array3d(img)
        # luminosity filter
        avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
        arr = array([[[avg, avg, avg] for avg in col] for col in avgs])
        return surfarray.make_surface(arr)
