#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.stage.stage_sounds import StageSounds


class StageSoundSelector:
    def __init__(self, sounds):
        self.list_of_stages = {
            'forest': StageSounds('forest', sounds),
            'castle': StageSounds('castle', sounds),
            'dungeon': StageSounds('dungeon', sounds),
        }
        self.current_stage = None

    def select_sound(self, level):
        if level <= 7:
            self.set_stage_sounds('forest')
        elif 7 < level < 16:
            self.set_stage_sounds('castle')
        else:
            self.set_stage_sounds('dungeon')

    def set_stage_sounds(self, stage_name):
        self.current_stage = self.list_of_stages[stage_name]

    def get_stage_sounds(self):
        return self.current_stage
