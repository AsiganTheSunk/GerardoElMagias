#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from constants.game_colors import GRAY_COLOR, MEDIUM_GREEN_COLOR


class HealthBar:
    def __init__(self, x, y, current_hp, max_hp, size_x=160, size_y=15):
        self.x = x
        self.y = y

        self.size_x = size_x
        self.size_y = size_y

        self.max_hp = max_hp
        self.current_hp = current_hp

    def draw(self, hp, max_hp, screen):
        # Update: HealthBar Status
        self.max_hp = max_hp
        self.current_hp = hp
        ratio = self.current_hp / self.max_hp
        draw.rect(screen, GRAY_COLOR, (self.x, self.y, self.size_x, self.size_y))
        draw.rect(screen, MEDIUM_GREEN_COLOR, (self.x, self.y, self.size_x * ratio, self.size_y))
