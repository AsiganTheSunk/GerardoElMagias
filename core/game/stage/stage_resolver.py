#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import mouse
import constants.globals
from core.game.text.damage_text import DamageText

# Init DamageText
damage_text = DamageText()


class StageResolver:
    def __init__(self, sound_master, battle_master, stage_renderer, game_attributes):
        self.action_wait_time = 90

        self.sound_master = sound_master
        self.battle_master = battle_master
        self.stage_renderer = stage_renderer

        self.game_attributes = game_attributes
        self.player = self.battle_master.get_hero()

    def stage_loop_resolver(self):
        # Stage Drawer Update
        self.stage_renderer.update(self.game_attributes.text_sprite)

        # Sound Master:
        self.sound_master.stage_sound_selector.select_sound(self.battle_master.level)
        self.sound_master.background_play(self.battle_master.game_mode)

        # Player Interactions
        self.resolve_player_mouse_actions()
        self.resolve_player_interface_actions()

        # Combat Phase
        self.resolve_combat_phase()

        # Victory/Defeat
        self.resolve_victory()
        self.resolve_defeat()

        constants.globals.action_cooldown += 1
        self.player.next_action = None

    def resolve_player_interface_actions(self):
        if self.player.has_enough_fury():
            self.stage_renderer.player_bottom_panel_buttons.ultimate_button.activate()
        else:
            self.stage_renderer.player_bottom_panel_buttons.ultimate_button.deactivate()

        if self.player.has_enough_fury(50):
            self.stage_renderer.player_bottom_panel_buttons.whirlwind_button.activate()
        else:
            self.stage_renderer.player_bottom_panel_buttons.whirlwind_button.deactivate()

    def resolve_player_mouse_actions(self):
        if self.battle_master.is_victory_phase():
            for enemy_unit in self.battle_master.stage_unit_renderer.stage_units[1:]:
                if enemy_unit.animation_set.mouse_collision():
                    self.stage_renderer.display_bag_mouse()
                    if constants.globals.clicked:
                        self.player.get_loot(enemy_unit.unit, self.game_attributes.text_sprite)
                        constants.globals.clicked = False
                    # Return to avoid normal mouse showing up
                    return

        if self.battle_master.is_battle_phase():
            for enemy_unit in self.battle_master.stage_unit_renderer.stage_units[1:]:
                if enemy_unit.unit.animation_set.mouse_collision():
                    self.stage_renderer.display_sword_mouse()
                    if constants.globals.clicked and enemy_unit.unit.alive:
                        self.player.next_action = ('attack', enemy_unit.unit)
                    # Return to avoid normal mouse showing up
                    return
        # Enable default mouse
        mouse.set_visible(True)

    def resolve_combat_phase(self):
        if self.battle_master.is_battle_phase():
            if constants.globals.action_cooldown >= self.action_wait_time:
                self.battle_master.run_fighter_action(self.game_attributes.text_sprite)

    def resolve_victory(self):
        if self.battle_master.is_victory_phase():
            self.stage_renderer.player_bottom_panel_buttons.next_button.hidden = False
            self.stage_renderer.display_victory()

    def resolve_defeat(self):
        if self.battle_master.is_defeat_phase():
            self.stage_renderer.display_defeat()
