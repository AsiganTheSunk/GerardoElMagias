#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from constants.game_colors import *


class FuryBar:
    def __init__(self, x, y, fury, max_fury):
        self.x = x
        self.y = y
        self.fury = fury
        self.max_fury = max_fury

    def draw(self, fury, max_fury, screen):
        # update fury
        self.fury = fury
        self.max_fury = max_fury
        ratio = self.fury / self.max_fury
        draw.rect(screen, GRAY_COLOR, (self.x, self.y + 20, 160, 15))
        draw.rect(screen, ORANGE_COLOR, (self.x, self.y + 20, 160 * ratio, 15))
