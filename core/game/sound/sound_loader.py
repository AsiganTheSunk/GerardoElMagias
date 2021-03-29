#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.sound.db.sound_db import SOUND_POOL
from logger.logger_master import LoggerMaster
from logger.constants.logger_level_type import LoggingLevelType
from core.game.sound.wrapper_sound import WrappedSound


class SoundLoader:
    def __init__(self, sound_mixer):
        self.animation_loader_logger = LoggerMaster(self.__class__.__name__, LoggingLevelType.DEBUG.value)

        self.sound_mixer = sound_mixer
        self.sounds = dict()
        self.load_sound_sets()

    def load_sound_sets(self):
        self.animation_loader_logger.log_debug_header('[ Loading Sound Resources ]:')
        sound_type = dict()
        # For Each AnimationSet present in AnimationSets: Environment, Skills, Units
        for sound_resource_type in SOUND_POOL:
            sound_subtype = dict()
            self.animation_loader_logger.log_debug_message()
            self.animation_loader_logger.log_debug_message(f'Sound Type: {sound_resource_type.value}')
            self.animation_loader_logger.log_debug_message('------' * 10)
            for index, sound_set in enumerate(SOUND_POOL[sound_resource_type]):
                sound_resource = dict()
                self.animation_loader_logger.log_debug_message(f'Sound Sub Type: {sound_set.value}')
                for sound in SOUND_POOL[sound_resource_type][sound_set]:
                    sound_resource[sound.sound_name] = self.load_resource(sound_resource_type.value,
                                                                          sound_set.value, sound.sound_name,
                                                                          sound.file_extension, sound.volume)
                sound_subtype[sound_set.value.lower()] = sound_resource
            sound_type[sound_resource_type.value.lower()] = sound_subtype

        self.animation_loader_logger.log_debug_message()
        self.animation_loader_logger.log_debug_message('Done')
        self.sounds = sound_type

        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.sounds)

    def load_resource(self, resource_type, sound_set, sound_name, sound_file_extension, sound_volume):
        sound_path = f'resources/sound/{resource_type.lower()}/{sound_set.lower()}/{sound_name.lower()}.{sound_file_extension.value}'
        self.animation_loader_logger.log_debug_message('> ' + sound_path)
        sound_resource = WrappedSound(sound_path)
        sound_resource.set_volume(sound_volume)
        return sound_resource
