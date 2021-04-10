#!/usr/bin/env python
# -*- coding: utf-8 -*-

import constants.globals


class StageResolver:
    def __init__(self, sound_master, battle_master, stage_renderer, game_attributes):
        self.action_wait_time = 90

        self.sound_master = sound_master
        self.battle_master = battle_master
        self.stage_renderer = stage_renderer

        self.game_attributes = game_attributes
        self.player = self.battle_master.get_hero()

    def stage_loop_resolver(self):
        # Resolve StageRenderer Run/Update Interface, Units, Resources, Text, CombatText
        self.stage_renderer.resolve_render()

        # Resolve SoundMaster Run/Update Sound
        self.resolve_sound()

        # Resolve Combat Phase
        self.resolve_combat_phase()

        constants.globals.action_cooldown += 1
        self.player.next_action = None

    def resolve_sound(self):
        self.sound_master.stage_sound_selector.select_sound(self.battle_master.level)
        self.sound_master.background_play(self.battle_master.game_mode)

    def resolve_combat_phase(self):
        if self.battle_master.is_battle_phase():
            if constants.globals.action_cooldown >= self.action_wait_time:
                self.battle_master.run_fighter_action(self.game_attributes.text_sprite)

