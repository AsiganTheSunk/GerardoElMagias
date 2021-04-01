#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_element import UIElement
from constants.game_fonts import interface_font
from constants.game_colors import WHITE_COLOR


class UITextElement(UIElement):
    def __init__(self, message, position, color=WHITE_COLOR, font=interface_font, bold=False, italic=False):
        super().__init__()

        self.message = message
        self.color = color
        self.font = font
        self.bold = bold
        self.italic = italic

        x, y = position
        self.x = x
        self.y = y

    def set_style(self):
        if self.bold:
            self.font.set_bold(True)

        if self.italic:
            self.font.set_italic(True)

    def render(self):
        message_font_surface = self.font.render(str(self.message), True, self.color)
        return message_font_surface, (self.x, self.y)
