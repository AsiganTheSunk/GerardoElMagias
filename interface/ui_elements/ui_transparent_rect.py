#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import Rect, Color
from interface.ui_elements.ui_element import UIElement


class UITransparentRect(UIElement):
    def __init__(self, x, y, width, height, border_size=0, color=Color('Tomato')):
        super().__init__()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.border_size = border_size
        self.color = color

    def render(self):
        return


    #     mouse_over = Surface((self.button.image_width, self.button.image_width), SRCALPHA, 32)
    #     mouse_over.set_alpha(100)
    #     mouse_over.fill(Color('LightBlue'))
    #
    #     self.surface.blit(mouse_over, (self.rect.x, self.rect.y))
    #     draw.rect(self.surface, Color('Blue'), (self.rect.x, self.rect.y, self.image_width+1, self.image_height+1), 2)