#!/usr/bin/env python
from pygame import mixer
from core.units.sound.sound_db import SOUND_POOL


class SoundMaster:
    def __init__(self):
        self.sound_mixer = mixer
        self.sound_mixer.init()
        self.sound_mixer.pre_init(44100, -16, 2, 4096)
        self.sounds = dict()
        self.load_sound_sets()

    def load_sound_sets(self):
        print('[ Loading Sound Resources ]:')
        print('-------' * 10)

        sound_type = dict()
        sound_subtype = dict()
        sound_resource = dict()
        # For Each AnimationSet present in AnimationSets: Environment, Skills, Units
        for sound_resource_type in SOUND_POOL:
            # Load Each Animation Resource present in the Animation to be displayed
            # print('Sound_Type:', sound_resource_type.value)
            for index, sound_set in enumerate(SOUND_POOL[sound_resource_type]):
                # print('Sound_SubType:',sound_set.value)
                for sound in SOUND_POOL[sound_resource_type][sound_set]:
                    sound_resource[sound.sound_name] = self.load_resource(sound_resource_type.value, sound_set.value, sound.sound_name, sound.file_extension, sound.volume)
                sound_subtype[sound_set.value.lower()] = sound_resource
            sound_type[sound_resource_type.value.lower()] = sound_subtype
        print('\n', 'Done.')
        self.sounds = sound_type

    def load_resource(self, resource_type, sound_set, sound_name, sound_file_extension, sound_volume):
        # print(f"> resources/sound/{resource_type.lower()}/{sound_set.lower()}/{sound_name.lower()}.{sound_file_extension.value}")
        sound_resource = self.sound_mixer.Sound(f"resources/sound/{resource_type.lower()}/{sound_set.lower()}/{sound_name.lower()}.{sound_file_extension.value}")
        sound_resource.set_volume(sound_volume)
        return sound_resource



