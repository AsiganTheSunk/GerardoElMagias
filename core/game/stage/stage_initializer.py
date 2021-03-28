#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Game Drawable Instance Imports:
from core.game.stage.stage_renderer import StageRenderer

# Master Game Engine Imports
from core.game.sound.sound_master import SoundMaster
from core.game.animations.animation_master import AnimationMaster
from core.game.battle.battle_master import BattleMaster
from core.game.stage.stage_resolver import StageResolver


class StageInitializer:
    def __init__(self, game_attributes):
        # Load Configuration File

        # Initializing InitGame & Stage Drawer
        self.sound_master = SoundMaster()
        self.animation_master = AnimationMaster(game_attributes.surface)

        self.stage_renderer = \
            StageRenderer(game_attributes.surface,
                          game_attributes.screen_width, game_attributes.screen_height,
                          0, game_attributes.panel_height,
                          game_attributes.clock, game_attributes.fps, self.animation_master)

        self.stage_renderer.display_caption()
        self.battle_master = BattleMaster(self.animation_master, game_attributes)
        self.stage_resolver = StageResolver(self.sound_master, self.battle_master, self.stage_renderer, game_attributes)

    def run_stage(self):
        self.stage_resolver.stage_loop_resolver()
