#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mouse, transform, Surface, time, SRCALPHA, font, Color, surfarray, draw, display, Rect
from numpy import array

# BasicButton(screen, 100, 100, ultimate_image, 50, 50, 'Ultimate', text_color=pygame.Color('White'))


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

        self.key_bind = None
        self.button_status = True

    def set_key_bind(self, key_bind):
        self.key_bind = key_bind

    def get_key_bind(self):
        return self.key_bind

    def button_text_placement(self, placement):
        text_width, text_height = self.text_font.size(self.text_message)
        center_x, center_y = self.rect.center
        if placement == 'center':
            return (center_x - text_width/2), (center_y - text_height/2)
        elif placement == 'bottom_center':
            return (center_x - text_width/2), (center_y + text_height - 2)
        elif placement == 'bottom_under':
            return (center_x - text_width/2), (center_y + self.image_height/2)
        elif placement == 'top_center':
            return (center_x - text_width/2), (center_y - self.image_height/2 - 2)
        elif placement == 'top_over':
            return (center_x - text_width/2), (self.rect.y - text_height - 2)

    def display_text(self, active=False, placement='bottom_under'):
        text_x, text_y = self.button_text_placement(placement)
        if not active:
            self.surface.blit(self.text_font.render(self.text_message, True, Color('White')), (text_x, text_y))
        else:
            self.surface.blit(self.text_font.render(self.text_message, True, Color('Tomato')),  (text_x, text_y))

    def display(self, show_text=False):
        if self.button_status:
            self.surface.blit(self.image, (self.rect.x, self.rect.y))
        else:
            inactive_image = self.grayscale(self.image)
            self.surface.blit(inactive_image, (self.rect.x, self.rect.y))

        if show_text:
            self.display_text()

    def mouse_collide(self):
        return self.rect.collidepoint(mouse.get_pos())

    def activate(self):
        self.button_status = True

    def deactivate(self):
        self.button_status = False

    def mouse_over_effect(self):
        mouse_over = Surface((self.image_width, self.image_width), SRCALPHA, 32)
        mouse_over.set_alpha(100)
        mouse_over.fill(Color('LightBlue'))
        self.surface.blit(mouse_over, (self.rect.x, self.rect.y))
        draw.rect(self.surface, Color('Blue'), (self.rect.x, self.rect.y, self.image_width+1, self.image_height+1), 2)

    def is_hover(self):
        if self.mouse_collide():
            self.mouse_over_effect()

    def click_effect(self):
        self.surface.blit(self.clicked_image, (self.rect.x + 3, self.rect.y + 3))
        if self.is_hover():
            self.mouse_over_effect()
        draw.rect(self.surface, Color('Tomato'), (self.rect.x, self.rect.y, self.image_width+1, self.image_height+1), 2)

    def debounce_time(self, interval=500):
        return time.get_ticks() - self.last_update >= interval

    def activate_button(self, interval=500):
        self.is_key_bind_clicked(interval)
        self.is_mouse_clicked(interval)

    def is_key_bind_clicked(self, interval=500):
        pass

    def is_mouse_clicked(self, interval=500):
        if self.mouse_collide() and self.button_status:
            if mouse.get_pressed(num_buttons=3)[0]:
                self.click_effect()
                self.display_text(True)
                if self.debounce_time(interval):
                    self.last_update = time.get_ticks()
                    return True
        return False

    @staticmethod
    def grayscale(img):
        arr = surfarray.array3d(img)
        # Luminosity Filter
        avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
        arr = array([[[avg, avg, avg] for avg in col] for col in avgs])
        return surfarray.make_surface(arr)
