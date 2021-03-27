#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game.sound.sets.consumable_sound_set import ConsumableSounds
from game.sound.sets.menu_sound_set import MenuSounds
from game.sound.sets.stage_sound_set import StageSoundsSet


class StageSounds(StageSoundsSet, ConsumableSounds, MenuSounds):
    def __init__(self, stage_name, sounds):
        self.stage_name = stage_name
        StageSoundsSet.__init__(self, sounds)
        ConsumableSounds.__init__(self, sounds)
        MenuSounds.__init__(self, sounds)

        self.background_boss_sound = sounds['music']['background']['boss']
        self.background_sound = sounds['music']['background'][stage_name.lower()]