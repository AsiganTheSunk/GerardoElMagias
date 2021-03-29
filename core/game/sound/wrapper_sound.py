#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.mixer import Sound


class WrappedSound(Sound):
    def __init__(self, sound_path):
        Sound.__init__(self, sound_path)
        self.sound_path = sound_path

    def get_sound_path(self):
        return self.sound_path
