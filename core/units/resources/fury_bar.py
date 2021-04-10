#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from constants.game_colors import GRAY_COLOR, ORANGE_COLOR


class FuryBar:
    def __init__(self, x, y, fury, max_fury, size_x=160, size_y=15):
        self.x = x
        self.y = y

        self.size_x = size_x
        self.size_y = size_y

        self.fury = fury
        self.max_fury = max_fury

    def draw(self, fury, max_fury, screen):
        # update fury
        self.fury = fury
        self.max_fury = max_fury
        ratio = self.fury / self.max_fury
        draw.rect(screen, GRAY_COLOR, (self.x, self.y + 20, self.size_x, self.size_y))
        draw.rect(screen, ORANGE_COLOR, (self.x, self.y + 20, self.size_x * ratio, self.size_y))
