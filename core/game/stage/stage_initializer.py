#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Game Drawable Instance Imports:
from render.stage_renderer import StageRenderer

# Master Game Engine Imports
from core.game.battle.battle_master import BattleMaster
from core.game.stage.stage_resolver import StageResolver


class StageInitializer:
    def __init__(self, game_attributes, animation_master, sound_master):
        # Load Configuration File

        self.battle_master = BattleMaster(animation_master, sound_master, game_attributes)
        self.stage_renderer = StageRenderer(self.battle_master, game_attributes, animation_master)
        self.stage_renderer.display_caption()
        self.stage_resolver = StageResolver(sound_master, self.battle_master, self.stage_renderer, game_attributes)

    def run_stage(self):
        self.stage_resolver.stage_loop_resolver()
