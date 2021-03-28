#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import display, quit, Color

# Game Engine Constants Imports:
import constants.globals

# Game Event Control Import:
from core.game.event_control import event_control

from core.game.stage.stage_initializer import StageInitializer
from core.game.game_attributes import GameAttributes


class GameEngine:
    def __init__(self):
        self.run_game = True
        self.run_stage = True

        self.game_attributes = GameAttributes()
        self.stage_initializer = StageInitializer(self.game_attributes)

    def run(self):
        while constants.globals.run_game:
            self.game_attributes.surface.fill(Color('Black'))
            self.stage_initializer.run_stage()
            event_control()
            display.update()
        quit()
