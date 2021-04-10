#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_element import UIElement


class UILayout(UIElement):
    def __init__(self):
        super().__init__()
        self.static = True
        self.elements = []

    def update_ui_elements(self, *args):
        pass

    def reset_ui_elements(self):
        self.elements = []

    def add_ui_element(self, element):
        self.elements.append(element)
