#!/usr/bin/env python
from pygame import mixer

from core.units.sound.sound_resource import SoundResource


class SoundSet:
    def __init__(self, unit_type, sound_set):
        # Unit Information: Unit Name
        self.unit_type = unit_type

        # Init Animation Set List: [Action][Frame Index]
        self.animation_list = []

        # Load Animation onto animation_list
        for sound_resource in sound_set:
            # Load: Unit Animations using Path to Resources
            self.animation_list.append(self.load(self.unit_type, sound_resource.sound_type, sound_resource.volume))

    @staticmethod
    def load(name, sound_type, volume):
        # Load: Sound from Path
        sound = mixer.Sound(f"resources/sound/{name}/{sound_type}.wav")
        sound.set_volume(volume)
        return sound

    def play(self, loop=False):
        pass
