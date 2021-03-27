#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:

# Game Engine Constants Imports:
from constants.game_windows import screen_height, screen_width, panel_height

# Game Drawable Instance Imports:
from core.game.stage.stage_renderer import StageRenderer

# Master Game Engine Imports
from core.game.sound.sound_master import SoundMaster
from core.game.animations.animation_loader import AnimationLoader
from core.game.battle.battle_master import BattleMaster
from core.game.game_attributes import GameAttributes

# Game Event Control Import:
from core.game.stage.stage_resolver import StageResolver


class StageInitializer:
    def __init__(self):
        # Load Configuration File

        # Initializing InitGame & Stage Drawer
        self.game_attributes = GameAttributes(screen_width, screen_height)
        self.animation_loader = AnimationLoader(self.game_attributes.surface)
        self.sound_master = SoundMaster()
        self.stage_drawer = \
            StageRenderer(self.game_attributes.surface, screen_width, screen_height, 0, panel_height,
                          self.game_attributes.clock, self.game_attributes.fps, self.animation_loader)

        self.stage_drawer.display_caption()
        self.battle_master = BattleMaster(self.animation_loader)
        self.stage_resolver = StageResolver(self.sound_master, self.battle_master, self.stage_drawer, self.game_attributes)

    def run_stage(self):
        self.stage_resolver.stage_loop_resolver()
