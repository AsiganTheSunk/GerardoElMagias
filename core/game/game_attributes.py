#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import time, display, mixer, sprite


class GameAttributes:
    def __init__(self, clock, fps, width, height):
        self.clock = clock
        self.fps = fps
        self.surface = display.set_mode((width, height))
        self.update_time = time.get_ticks()
        self.sound_mixer = mixer
        self.text_sprite = sprite.Group()

        # Init Mixer
        self.sound_mixer.pre_init(44100, -16, 2, 4096)

