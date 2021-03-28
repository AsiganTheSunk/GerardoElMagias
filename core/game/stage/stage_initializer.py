#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Game Drawable Instance Imports:
from core.game.stage.stage_renderer import StageRenderer

# Master Game Engine Imports
from core.game.battle.battle_master import BattleMaster
from core.game.stage.stage_resolver import StageResolver


class StageInitializer:
    def __init__(self, game_attributes, animation_master, sound_master):
        # Load Configuration File

        self.stage_renderer = \
            StageRenderer(game_attributes.surface,
                          game_attributes.screen_width, game_attributes.screen_height,
                          0, game_attributes.panel_height,
                          game_attributes.clock, game_attributes.fps, animation_master)

        self.stage_renderer.display_caption()
        self.battle_master = BattleMaster(animation_master, game_attributes)
        self.stage_resolver = StageResolver(sound_master, self.battle_master, self.stage_renderer, game_attributes)

    def run_stage(self):
        self.stage_resolver.stage_loop_resolver()
