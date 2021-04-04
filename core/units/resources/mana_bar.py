#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from constants.game_colors import GRAY_COLOR, MEDIUM_BLUE_COLOR


class ManaBar:
    def __init__(self, x, y, mp, max_mp, size_x=160, size_y=10):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

        self.mp = mp
        self.max_mp = max_mp

    def draw(self, mp, max_mp, screen):
        # update mana
        self.mp = mp
        self.max_mp = max_mp
        ratio = self.mp / self.max_mp
        draw.rect(screen, GRAY_COLOR, (self.x, self.y, self.size_x, self.size_y))
        draw.rect(screen, MEDIUM_BLUE_COLOR, (self.x, self.y, self.size_x * ratio, self.size_y))
