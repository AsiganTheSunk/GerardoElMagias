#!/usr/bin/env python

from pygame import image, transform
from core.units.animations.db.unit_animation_db import UNIT_ANIMATION_SETS, SKILL_ANIMATION_SETS
from enum import Enum


class AnimationResourceClass(Enum):
    UNITS = 'units'
    SKILLS = 'skills'
    ENVIRONMENT = 'environment'


class AnimationMaster:
    def __init__(self, surface):
        self.surface = surface
        self.environment_animation_sets = []
        self.unit_animation_sets = self.load_resource_sets(UNIT_ANIMATION_SETS, AnimationResourceClass.UNITS.value)
        # self.skill_animation_sets = self.load_resource_sets(SKILL_ANIMATION_SETS, AnimationResourceClass.SKILLS.value)

    def get_unit_resource_animation_set(self, resource_type):
        return self.unit_animation_sets[resource_type]

    def load_resource_sets(self, animation_pool, resource_type):
        print('[ Loading Image Resources ]:')
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
        print('\n', 'Done.')
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


