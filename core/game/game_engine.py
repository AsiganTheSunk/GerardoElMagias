#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import display, quit, Color

# Game Engine Constants Imports:
import constants.globals

# Game Event Control Import:
from core.game.game_event_control import event_control

# Master Game Engine Imports
from core.game.sound.sound_master import SoundMaster
from core.game.animations.animation_master import AnimationMaster
from core.game.stage.stage_initializer import StageInitializer
from core.game.game_attributes import GameAttributes
from logger.logger_master import LoggerMaster


class GameEngine:
    def __init__(self):
        self.run_game = True
        self.run_stage = True

        self.game_engine_logger = LoggerMaster(self.__class__.__name__, file_streamer=False, console_streamer=True)
        self.game_engine_logger.log_info_header(f'[ Starting {self.__class__.__name__} ]:')

        # Initializing Game Attributes, Sound Master, Animation Master
        self.game_attributes = GameAttributes()
        self.sound_master = SoundMaster()
        self.animation_master = AnimationMaster(self.game_attributes.surface)

        # Initializing Stage Initializer: This should call Stage Selector in the near future
        self.stage_initializer = StageInitializer(self.game_attributes, self.animation_master, self.sound_master)

    def run(self):
        while constants.globals.run_game:
            self.game_attributes.surface.fill(Color('Black'))
            self.stage_initializer.run_stage()
            event_control()
            display.update()
        quit()
