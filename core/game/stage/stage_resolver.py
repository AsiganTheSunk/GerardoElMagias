#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import mouse


# Game Engine Constants Imports:

from constants.sound import ultimate_sound
import constants.globals

# Game Drawable Instance Imports:
from interface.basic_components.button import Button
from interface.composed_components.spell_book import Spellbook

# Game Control Imports:
import constants.globals

# Master Game Engine Imports
from core.game.game_modes import GameModes

from core.text.damage_text import DamageText

from constants.basic_images import skull_image, spellbook_image, \
    health_potion_image, mana_potion_image, restart_image, ultimate_image, next_button_image, gold_image, \
    background_forest, background_castle, panel_image, sword_image, victory_banner_image, loot_image, \
    defeat_banner_image


# Init DamageText
damage_text = DamageText()


class StageResolver:
    def __init__(self, sound_master, battle_master, stage_drawer, game_attributes):
        self.action_wait_time = 90

        self.sound_master = sound_master
        self.battle_master = battle_master
        self.stage_drawer = stage_drawer

        self.game_attributes = game_attributes

        healing_potion_button = \
            Button('healing_potion', 130, self.stage_drawer.height - self.stage_drawer.panel_height + 1, health_potion_image, 64, 64)

        mana_potion_button = \
            Button('mana_potion', 132, self.stage_drawer.height - self.stage_drawer.panel_height + 65, mana_potion_image, 60, 60)

        spell_book_button = Button('spellbook', 10, 600, spellbook_image, 100, 100)
        self.ultimate_button = Button('ultimate', 555, 590, ultimate_image, 60, 60)
        self.ultimate_button.hidden = True
        kill_all_button = Button('kill_all', 40, 260, skull_image, 60, 60)
        self.next_button = Button('next', 1015, 180, next_button_image, 80, 80)
        self.next_button.hidden = True

        mana_potion_button.on_click(battle_master.handle_potion_click)
        healing_potion_button.on_click(battle_master.handle_potion_click)
        spell_book_button.on_click(self.toggle_player_spell_book)
        self.ultimate_button.on_click(self.handle_ultimate_click)
        kill_all_button.on_click(self.kill_switch)
        self.next_button.on_click(self.handle_next_click)

        self.stage_drawer.add(mana_potion_button)
        self.stage_drawer.add(healing_potion_button)
        self.stage_drawer.add(spell_book_button)
        self.stage_drawer.add(self.ultimate_button)
        self.stage_drawer.add(kill_all_button)
        self.stage_drawer.add(self.next_button)

        self.spellbook = Spellbook(self.battle_master, self.game_attributes.text_sprite)
        self.spellbook.hidden = True
        self.stage_drawer.add(self.spellbook)

        self.player = self.battle_master.get_hero()

    def stage_loop_resolver(self):
        # Stage Drawer Update
        self.stage_drawer.update(self.battle_master.level,
                                 self.battle_master.friendly_fighters[0],
                                 self.battle_master.enemy_fighters,
                                 self.battle_master.is_boss_level(),
                                 self.game_attributes.text_sprite)

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

    def stage_reset(self):
        self.battle_master.friendly_fighters[0].ultimate_status = False
        self.battle_master.friendly_fighters[0].multi_attacks_left = 7

    def toggle_player_spell_book(self, event, spellbook):
        if self.battle_master.is_player_phase():
            self.spellbook.hidden = not self.spellbook.hidden

            if self.battle_master.is_battle_phase():
                self.battle_master.swap_battle_mode(GameModes.SPELLBOOK)
            else:
                self.battle_master.swap_battle_mode()

    def resolve_player_interface_actions(self):
        if self.player.has_full_fury() and self.battle_master.is_player_phase():
            self.ultimate_button.hidden = False
        else:
            self.ultimate_button.hidden = True

    def handle_ultimate_click(self, event, button):
        self.battle_master.get_hero().ultimate_status = True
        ultimate_sound.play()
        self.battle_master.get_hero().reset_fury()
        constants.globals.action_cooldown = -25

    def resolve_mouse_display(self):
        pass

    def resolve_player_mouse_actions(self):
        if self.battle_master.is_victory_phase():
            for enemy_unit in self.battle_master.enemy_fighters:
                if enemy_unit.animation_set.mouse_collision():
                    self.stage_drawer.display_bag_mouse()
                    if constants.globals.clicked:
                        self.player.loot(enemy_unit, self.game_attributes.text_sprite)
                        constants.globals.clicked = False
                    # Return to avoid normal mouse showing up
                    return

        elif self.battle_master.is_battle_phase():
            for enemy_unit in self.battle_master.enemy_fighters:
                if enemy_unit.animation_set.mouse_collision():
                    self.stage_drawer.display_sword_mouse()
                    if constants.globals.clicked and enemy_unit.alive:
                        self.player.next_action = ('attack', enemy_unit)
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
            self.next_button.hidden = False
            self.stage_drawer.display_victory()

    def handle_next_click(self, *args):
        self.stage_reset()
        self.battle_master.next_level()
        self.next_button.hidden = True

    def resolve_defeat(self):
        if self.battle_master.is_defeat_phase():
            self.stage_drawer.display_defeat()

    def kill_switch(self, event, button):
        for target_unit in self.battle_master.enemy_fighters:
            if target_unit.alive:
                target_unit.death()
                target_unit.death_animation()

        self.battle_master.move_to_victory_phase()
