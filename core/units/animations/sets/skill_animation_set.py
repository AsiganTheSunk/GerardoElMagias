#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import time, Surface, Rect, SRCALPHA, draw, mask
from core.units.animations.sets.animation_set import AnimationSet


class SkillAnimationSet(AnimationSet):
    def __init__(self, surface, x, y, skill_name, animation_list):
        AnimationSet.__init__(self, x, y, skill_name, animation_list)

        self.surface = surface
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        if skill_name == "Firestorm":
            self.additional_cycles = 1
        else:
            self.additional_cycles = 0

    def update(self, animation_cooldown=100):
        # Evaluate if animation is finished
        if self.frame_index >= len(self.animation_list[self.action]) and self.additional_cycles == 0:
            self.additional_cycles = 0
            return True

        # Update Action Frame Index
        self.image = self.animation_list[self.action][self.frame_index]

        # Evaluate if enough time has passed since the last update
        if time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = time.get_ticks()
            self.frame_index += 1

        if self.additional_cycles > 0:
            # Reset Animations to Idle unless Death status is triggered
            if self.frame_index >= len(self.animation_list[self.action]):
                self.reset_frame_index()
                self.additional_cycles -= 1
        return False

    def draw(self):
        # Place Animation on the Screen
        self.surface.blit(self.image, self.rect)
        self.mask = mask.from_surface(self.image)
