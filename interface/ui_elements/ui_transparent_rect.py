#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import Rect, Color, Surface, SRCALPHA
from interface.ui_elements.ui_element import UIElement


class UITransparentRect(UIElement):
    def __init__(self, x, y, width, height, color=Color('Tomato')):
        super().__init__()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color

    def render(self):
        alpha_surface = Surface((self.width, self.height), SRCALPHA, 32)
        alpha_surface.set_alpha(100)
        alpha_surface.fill(self.color)
        return alpha_surface, self.x, self.y