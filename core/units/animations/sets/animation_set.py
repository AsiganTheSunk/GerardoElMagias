#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import time, mask


class AnimationSet:
    def __init__(self, x, y, unit_name, animation_list):
        # Unit Information: Coordinates x,y & Unit Name
        self.x = x
        self.y = y
        self.unit_name = unit_name

        # Init Animation Set List: [Action][Frame Index]
        self.animation_list = animation_list

        # Init Default Frames
        self.frame_index = 0
        self.action = 0  # 0: Idle, 1: Attack, 2: Hurt, 3:Death, 4:Block, 5: Miss
        self.image = self.animation_list[self.action][self.frame_index]
        self.mask = mask.from_surface(self.image)

        self.update_time = time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def reset_frame_index(self):
        self.frame_index = 0
        self.update_time = time.get_ticks()
