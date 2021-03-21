#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import mouse


# Game Engine Constants Imports:

from constants.sound import ultimate_sound
import constants.globals

# Game Drawable Instance Imports:
from interface.composed_component.spell_book import open_spell_book

# Game Control Imports:
import constants.globals

# Master Game Engine Imports
from core.game.game_modes import GameModes

from core.text.damage_text import DamageText


# Init DamageText
damage_text = DamageText()


class StageResolver:
    def __init__(self, sound_master, battle_master, stage_drawer, game_attributes):
        self.action_wait_time = 90

        self.sound_master = sound_master
        self.battle_master = battle_master
        self.stage_drawer = stage_drawer
        self.game_attributes = game_attributes

        self.previous_mouse_collision = False
        self.player = self.battle_master.get_hero()

    def stage_loop_resolver(self):
        # Stage Drawer Update
        self.stage_drawer.update(self.battle_master.level,
                                 self.battle_master.friendly_fighters[0],
                                 self.battle_master.enemy_fighters,
                                 self.battle_master.is_boss_level(),
                                 self.game_attributes.text_sprite)

        # Sound Master:
        self.sound_master.stage_selector_sound.select_sound(self.battle_master.level)
        self.sound_master.background_play(self.battle_master.game_mode)

        # Kill Switch: Debugging
        self.kill_switch()

        # Player Interactions
        self.resolve_player_spell_book()
        self.resolve_player_mouse_actions()
        self.resolve_player_interface_actions()

        # Combat Phase
        self.resolve_combat_phase()

        # Victory/Defeat
        self.resolve_victory()
        self.resolve_defeat()

        constants.globals.action_cooldown += 1
        self.player.next_action = None

    def stage_reset(self):
        constants.globals.action_cooldown = 0
        self.battle_master.friendly_fighters[0].ultimate_status = False
        self.battle_master.friendly_fighters[0].multi_attacks_left = 7

    def resolve_player_spell_book(self):
        if self.stage_drawer.display_spell_book():
            if self.battle_master.is_player_phase():
                self.battle_master.game_mode = GameModes.SPELLBOOK

        if self.battle_master.is_spell_book_phase():
            open_spell_book(self.player, self.battle_master.enemy_fighters, self.game_attributes.surface,
                            self.game_attributes.text_sprite, self.battle_master)

    def resolve_player_interface_actions(self):
            if self.stage_drawer.display_health_potion():
                if self.player.stash.has_healing_potion() and self.battle_master.is_player_phase():
                    self.player.next_action = ['use', 'healing_potion']
                else:
                    damage_text.warning(self.player, 'No Healing Potions', self.game_attributes.text_sprite)

            if self.stage_drawer.display_mana_potion():
                if self.player.stash.has_mana_potion() and self.battle_master.is_player_phase():
                    self.player.next_action = ['use', 'mana_potion']
                else:
                    damage_text.warning(self.player, 'No Mana Potions', self.game_attributes.text_sprite)

            if self.player.has_full_fury() and self.battle_master.is_player_phase():
                if self.stage_drawer.display_ultimate() and constants.globals.action_cooldown >= self.action_wait_time:
                    # Todo: activar animacion pre-ulti
                    self.player.ultimate_status = True
                    ultimate_sound.play()
                    self.player.reset_fury()
                    constants.globals.action_cooldown = -25

    def resolve_mouse_display(self):

        pass

    def resolve_player_mouse_actions(self):
        if self.battle_master.is_victory_phase():

            for enemy_unit in self.battle_master.enemy_fighters:
                if enemy_unit.animation_set.mouse_collision():
                    self.previous_mouse_collision = True
                    self.stage_drawer.display_bag_mouse()
                    if constants.globals.clicked:
                        self.player.loot(enemy_unit, self.game_attributes.text_sprite)
                        constants.globals.clicked = False

                if self.previous_mouse_collision is True and not enemy_unit.animation_set.mouse_collision():
                    self.previous_mouse_collision = False
                    mouse.set_visible(True)

        elif self.battle_master.is_battle_phase():
            for enemy_unit in self.battle_master.enemy_fighters:
                if enemy_unit.animation_set.mouse_collision():
                    self.previous_mouse_collision = True
                    self.stage_drawer.display_sword_mouse()
                    if constants.globals.clicked and enemy_unit.alive:
                        self.player.next_action = ('attack', enemy_unit)

                if self.previous_mouse_collision is True and not enemy_unit.animation_set.mouse_collision():
                    self.previous_mouse_collision = False
                    mouse.set_visible(True)

    def resolve_combat_phase(self):
        if self.battle_master.is_battle_phase():
            if constants.globals.action_cooldown >= self.action_wait_time:
                self.battle_master.run_fighter_action(self.game_attributes.text_sprite)

    def resolve_victory(self):
        # Victory Check
        if self.battle_master.is_victory_phase():
            self.stage_drawer.display_victory()

            if self.stage_drawer.display_next_button():
                self.stage_reset()
                self.battle_master.next_level()

    def resolve_defeat(self):
        if self.battle_master.is_defeat_phase():
            self.stage_drawer.display_defeat()

    def kill_switch(self):
        if self.stage_drawer.display_kill_all():
            for target_unit in self.battle_master.enemy_fighters:
                if target_unit.alive:
                    target_unit.death()
                    target_unit.death_animation()

            self.battle_master.move_to_victory_phase()
