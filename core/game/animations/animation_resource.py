#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AnimationResource:
    def __init__(self, animation_type, frames, scale_x=2, scale_y=2):
        self.frames = frames
        self.animation_type = animation_type
        self.scale_x = scale_x
        self.scale_y = scale_y
