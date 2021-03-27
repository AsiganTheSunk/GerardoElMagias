#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StageSoundsSet:
    def __init__(self, sounds):
        self.gold_loot_sound = sounds['fx']['items']['gold']
        self.error_loot_sound = sounds['fx']['items']['error']
        self.roll_loot_sound = sounds['fx']['items']['drum_roll']

        self.empty_loot_sound = sounds['fx']['items']['empty']
        self.victory_sound = sounds['music']['background']['victory']
        # self.defeat_sound = sounds['music']['background']['defeat']
