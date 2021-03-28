#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import time, display, mixer, sprite
from config.config_parser import CustomConfigParser


class GameAttributes:
    def __init__(self):
        self.config_parser = CustomConfigParser()
        game_windows = self.config_parser.get_section_map('GameWindows')
        tick_rate = self.config_parser.get_section_map('TickRate')

        # Display Section
        self.panel_height = int(game_windows['panel_height'])
        self.screen_width = int(game_windows['screen_width'])
        self.screen_height = int(game_windows['screen_height']) + self.panel_height
        self.surface = display.set_mode((self.screen_width, self.screen_height))

        # Tick Rate Section
        self.clock = time.Clock()
        self.fps = int(tick_rate['fps'])
        self.update_time = time.get_ticks()

        # Sound Section
        self.sound_mixer = mixer
        self.text_sprite = sprite.Group()

        # Init Mixer
        self.sound_mixer.pre_init(44100, -16, 2, 4096)

