#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image, transform
from core.game.animations.db.unit_animation_db import UNIT_ANIMATION_SETS
from core.game.animations.db.skill_animation_db import SKILL_ANIMATION_SETS
from core.game.animations.constants.animation_resource_type import AnimationResourceType
from logger.logger_master import LoggerMaster
from logger.constants.logger_level_type import LoggingLevelType


class AnimationLoader:
    def __init__(self):
        self.animation_loader_logger = LoggerMaster(self.__class__.__name__, LoggingLevelType.DEBUG.value)

        self.environment_animation_sets = []
        self.unit_animation_sets = self.load_resource_sets(UNIT_ANIMATION_SETS, AnimationResourceType.UNITS.value)
        self.skill_animation_sets = self.load_resource_sets(SKILL_ANIMATION_SETS, AnimationResourceType.SKILLS.value)

    def get_skill_resource_animation_set(self, resource_type):
        return self.skill_animation_sets[resource_type]

    def get_unit_resource_animation_set(self, resource_type):
        return self.unit_animation_sets[resource_type]

    @staticmethod
    def generate_animation_callback(index):
        return lambda animation_set: (animation_set.set_action(index), animation_set.reset_frame_index())

    def load_resource_sets(self, animation_pool, resource_type):
        self.animation_loader_logger.log_debug_header(f'[ Loading {resource_type.title()} Animation Resources ]:')
        animation_sets = dict()
        # For Each AnimationSet present in AnimationSets: Environment, Skills, Units
        for animation_set_type in animation_pool:
            animation_set = []
            animation_set_callbacks = dict()
            # Load Each Animation Resource present in the Animation to be displayed
            self.animation_loader_logger.log_debug_message()
            self.animation_loader_logger.log_debug_message(f'Animation Resource Type: {animation_set_type.value}')
            self.animation_loader_logger.log_debug_message('------' * 10)
            for index, animation_resource in enumerate(animation_pool[animation_set_type]):
                animation_set_callbacks[animation_resource.animation_type.value] = self.generate_animation_callback(index)
                # Load: Sequence Animations using Path to Resources
                self.animation_loader_logger.log_debug_message(f'Animation Resource: {animation_resource.animation_type.value}')
                animation_set.append(self.load_resource_sequence(
                    resource_type, animation_set_type.value,
                    animation_resource.animation_type, animation_resource.frames))

            animation_sets[animation_set_type.value + 'CallBacks'] = animation_set_callbacks
            animation_sets[animation_set_type.value] = animation_set

        self.animation_loader_logger.log_debug_message()
        self.animation_loader_logger.log_debug_message('Done.')
        return animation_sets

    def load_resource_sequence(self, resource_type, name, animation, sequence_length, x_scale=2, y_scale=2):
        # Load: Unit Animation Sequence based on Resource Type
        animation_sequence = []
        for index in range(sequence_length):
            animation_sequence.append(self.load_resource(resource_type, name, animation.value, index, x_scale, y_scale))
        return animation_sequence

    def load_resource(self, resource_type, unit_type, value, index, x_scale, y_scale):
        self.animation_loader_logger.log_debug_message(f"> resources/{resource_type}/{unit_type.lower()}/sprites/{value}/{index}.png")
        loaded_image = image.load(f"resources/{resource_type}/{unit_type.lower()}/sprites/{value}/{index}.png")
        normalized_image = transform.scale(loaded_image,
                                           (loaded_image.get_width() * x_scale,
                                            loaded_image.get_height() * y_scale))
        return normalized_image
