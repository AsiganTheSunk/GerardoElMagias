#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import Rect
from interface.ui_elements.ui_element import UIElement


class UIImage(UIElement):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())