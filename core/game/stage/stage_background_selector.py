#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_images import background_forest, background_castle, background_dungeon


class StageBackgroundSelector:
    def __init__(self, surface):
        self.surface = surface

        self.forest_background_image = background_forest
        self.forest_background = None

        self.castle_background_image = background_castle
        self.castle_background = None

        self.dungeon_background_image = background_dungeon
        self.dungeon_background = None

    def set_stage_background(self, level):
        # draw backgrounds
        if level <= 7:
            self.surface.blit(self.forest_background_image, (128, 0))
        if level > 7:
            self.surface.blit(self.castle_background_image, (128, 0))
        if level > 15:
            self.surface.blit(self.dungeon_background_image, (128, 0))
