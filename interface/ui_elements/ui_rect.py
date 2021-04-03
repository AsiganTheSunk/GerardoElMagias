#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import Rect, Color
from interface.ui_elements.ui_element import UIElement


class UIRect(UIElement):
    def __init__(self, x, y, width, height, border_size=0, color=Color('Tomato')):
        super().__init__()
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.border_size = border_size
        self.color = color

    def render(self):
        if self.border_size != 0:
            return self.color, self.x, self.y, \
                   self.width + round(self.border_size/2), self.height + round(self.border_size/2), self.border_size
        return self.color, self.x, self.y, \
               self.width, self.height, self.border_size


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