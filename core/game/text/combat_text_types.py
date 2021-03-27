#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.basic_fonts import combat_text_font, critical_combat_text_font, cast_text_font
from game.text.floating_text_effects import FloatingTextEffects


class CombatTextTypes(FloatingTextEffects):
    def __init__(self, x, y, animation_type):
        FloatingTextEffects.__init__(self, x, y, animation_type)
        self.image = None

    def cast_text(self, text, text_color, displacement_x=0, displacement_y=0):
        self.image = cast_text_font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + displacement_x, self.y + displacement_y)

    def combat_text(self, text, text_color, displacement_x=0, displacement_y=0):
        self.image = combat_text_font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + displacement_x, self.y + displacement_y)

    def critical_combat_text(self, text, text_color, displacement_x=0, displacement_y=0):
        self.image = critical_combat_text_font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + displacement_x, self.y + displacement_y)
