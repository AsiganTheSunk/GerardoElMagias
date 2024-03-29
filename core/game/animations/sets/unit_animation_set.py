#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import time, mask, mouse
from core.game.animations.animation_set import AnimationSet


class UnitAnimationSet(AnimationSet):
    def __init__(self, surface, x, y, unit_name, animation_list):
        AnimationSet.__init__(self, x, y, unit_name, animation_list)

        self.surface = surface
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def set_action(self, action):
        self.action = action

    def update(self, animation_cooldown=100):
        # Update Action Frame Index
        self.image = self.animation_list[self.action][self.frame_index]

        # Evaluate if enough time has passed since the last update
        if time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = time.get_ticks()
            self.frame_index += 1

        # Reset Animations to Idle unless Death status is triggered
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 1:
                self.frame_index = len(self.animation_list[1]) - 1
            else:
                self.action = 0     # Idle Animation
                self.reset_frame_index()

    # def draw_hitbox(self, surface, color, rect):
    #     shape_surf = Surface(Rect(rect).size, SRCALPHA)
    #     draw.rect(shape_surf, color, shape_surf.get_rect())
    #     surface.blit(shape_surf, rect)

    def mouse_collision(self):
        return self.rect.collidepoint(mouse.get_pos())

    def draw(self):
        # Place Animation on the Screen
        self.surface.blit(self.image, self.rect)
        self.mask = mask.from_surface(self.image)
