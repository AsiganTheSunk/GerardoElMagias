#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image, transform
from core.game.animations.db.unit_animation_db import UNIT_ANIMATION_SETS
from core.game.animations.db.skill_animation_db import SKILL_ANIMATION_SETS
from core.game.animations.constants.animation_resource_type import AnimationResourceType


class AnimationLoader:
    def __init__(self):
        self.environment_animation_sets = []
        self.unit_animation_sets = self.load_resource_sets(UNIT_ANIMATION_SETS, AnimationResourceType.UNITS.value)
        self.skill_animation_sets = self.load_resource_sets(SKILL_ANIMATION_SETS, AnimationResourceType.SKILLS.value)

    def get_skill_resource_animation_set(self, resource_type):
        return self.skill_animation_sets[resource_type]

    def get_unit_resource_animation_set(self, resource_type):
        return self.unit_animation_sets[resource_type]

    def load_resource_sets(self, animation_pool, resource_type):
        print('[ Loading Animation Resources ]:')
        print('-------' * 10)
        animation_sets = dict()
        # For Each AnimationSet present in AnimationSets: Environment, Skills, Units
        for animation_set_type in animation_pool:
            animation_set = []
            # Load Each Animation Resource present in the Animation to be displayed
            # print('Animation_Resource_Type:', animation_set_type.value)
            for index, animation_resource in enumerate(animation_pool[animation_set_type]):
                # Load: Sequence Animations using Path to Resources
                # print('Animation Resource:', animation_resource.animation_type.value)
                animation_set.append(self.load_resource_sequence(
                    resource_type, animation_set_type.value,
                    animation_resource.animation_type, animation_resource.frames))

            animation_sets[animation_set_type.value] = animation_set
        # print('\n', 'Done.')
        # print(animation_sets)
        return animation_sets

    def load_resource_sequence(self, resource_type, name, animation, sequence_length, x_scale=2, y_scale=2):
        # Load: Unit Animation Sequence based on Resource Type
        animation_sequence = []
        for index in range(sequence_length):
            animation_sequence.append(self.load_resource(resource_type, name, animation.value, index, x_scale, y_scale))
        return animation_sequence

    @staticmethod
    def load_resource(resource_type, unit_type, value, index, x_scale, y_scale):
        # print(f"> resources/{resource_type}/{unit_type.lower()}/sprites/{value}/{index}.png")
        loaded_image = image.load(f"resources/{resource_type}/{unit_type.lower()}/sprites/{value}/{index}.png")
        normalized_image = transform.scale(loaded_image,
                                           (loaded_image.get_width() * x_scale,
                                            loaded_image.get_height() * y_scale))
        return normalized_image