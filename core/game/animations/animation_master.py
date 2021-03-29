#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.animations.animation_loader import AnimationLoader


class AnimationMaster:
    def __init__(self, surface):
        self.surface = surface
        self.animation_loader = AnimationLoader()

    def get_skill_animation_set(self, resource_type):
        return self.animation_loader.skill_animation_sets[resource_type]

    def get_skill_animation_set_callbacks(self, resource_type):
        return self.animation_loader.skill_animation_sets[resource_type + 'CallBacks']

    def get_unit_animation_set(self, resource_type):
        return self.animation_loader.unit_animation_sets[resource_type]

    def get_unit_animation_set_callbacks(self, resource_type):
        return self.animation_loader.unit_animation_sets[resource_type + 'CallBacks']
