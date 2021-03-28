#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BasicSpellEffect:
    def __init__(self, target):
        # Basic Unit Target Coordinates x,y
        self.target_x = target.animation_set.rect.x
        self.target_y = target.animation_set.rect.y
