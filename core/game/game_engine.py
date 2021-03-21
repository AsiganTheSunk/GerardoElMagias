#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import display, quit

# Game Engine Constants Imports:
import constants.globals

# Game Event Control Import:
from core.game.game_event_controls import event_control

from game.stage.stage_initializer import StageInitializer


class GameEngine:
    def __init__(self):
        self.run_game = True
        self.run_stage = True

        self.stage_initializer = StageInitializer()

    def run(self):
        while constants.globals.run_game:
            self.stage_initializer.run_stage()
            event_control()
            display.update()
        quit()
