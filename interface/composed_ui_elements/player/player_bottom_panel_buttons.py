#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_fonts import default_font

# Game Engine Constants Imports:
import constants.globals

# Game Drawable Instance Imports:
from ui_elements.ui_button import UIButton
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_button import UITextButton
from interface.composed_ui_elements.player_spell_book import SpellBook

# Game Control Imports:
import constants.globals

# Master Game Engine Imports
from core.game.constants.game_modes import GameModes
from constants.game_images import skull_button_image, spell_book_button_image, kill_button_image, \
    health_potion_image, mana_potion_image, ultimate_image, next_button_image, whirlwind_image


class PlayerBottomPanelButtons(UILayout):
    def __init__(self, sound_master, battle_master, stage_renderer, game_attributes):
        super().__init__()
        self.sound_master = sound_master
        self.battle_master = battle_master
        self.game_attributes = game_attributes
        self.stage_renderer = stage_renderer

        self.elements = []

        # Consumable Buttons
        self.healing_potion_button = \
            UIButton('healing_potion', 130, self.game_attributes.screen_height - self.game_attributes.panel_height + 1,
                     health_potion_image, 64, 64)

        self.mana_potion_button = \
            UIButton('mana_potion', 132, self.game_attributes.screen_height - self.game_attributes.panel_height + 65,
                     mana_potion_image, 60, 60)

        # Skill Buttons
        self.ultimate_button = UIButton('ultimate', 555, 590, ultimate_image, 60, 60)
        self.ultimate_button.hidden = True

        self.whirlwind_button = UIButton('whirlwind', 280, 655, whirlwind_image, 40, 40)
        self.whirlwind_button.hidden = True

        # SpellBook Button and Reference Layout:
        self.spell_book_button = UIButton('spell_book', 10, 600, spell_book_button_image, 100, 100)
        self.spell_book = SpellBook(self.battle_master, self.game_attributes.text_sprite, self.stage_renderer.add_effect)
        self.spell_book.hidden = True

        # Next Button
        self.next_button = UIButton('next', 1015, 180, next_button_image, 80, 80)
        self.next_button.hidden = True

        # Debug Buttons:
        self.kill_switch_button = UIButton('kill_switch', 30, 260, skull_button_image, 60, 60)
        self.kill_switch_and_next_button = UIButton('kill_switch_and_next', 30, 350, kill_button_image, 60, 60)

        # Handle Buttons Events
        self.mana_potion_button.on_click(self.battle_master.handle_potion_click)
        self.healing_potion_button.on_click(self.battle_master.handle_potion_click)
        self.ultimate_button.on_click(self.handle_ultimate_click)
        self.whirlwind_button.on_click(self.handle_whirlwind_click)
        self.spell_book_button.on_click(self.toggle_player_spell_book)
        self.next_button.on_click(self.handle_next_click)
        self.kill_switch_button.on_click(self.handle_kill_switch)
        self.kill_switch_and_next_button.on_click(self.handle_kill_switch_and_next)

        # Add Elements to Layout
        self.add(self.healing_potion_button)
        self.add(self.mana_potion_button)
        self.add(self.ultimate_button)
        self.add(self.whirlwind_button)
        self.add(self.spell_book_button)
        self.add(self.spell_book)
        self.add(self.next_button)
        self.add(self.kill_switch_button)
        self.add(self.kill_switch_and_next_button)

    def add(self, ui_element):
        self.elements.append(ui_element)

    def handle_ultimate_click(self, event, button):
        if self.battle_master.is_player_phase():
            self.battle_master.get_hero().ultimate_status = True
            self.sound_master.play_unit_fx_sound('ultimate')
            self.battle_master.get_hero().reset_fury()
            constants.globals.action_cooldown = -25

    def handle_whirlwind_click(self, event, button):
        if self.battle_master.is_player_phase():
            self.battle_master.get_hero().whirlwind_status = True
            self.sound_master.play_unit_fx_sound('ultimate')
            self.battle_master.get_hero().reduce_fury(50)
            constants.globals.action_cooldown = -25

    def toggle_player_spell_book(self, event, spell_book):
        if self.battle_master.is_player_phase():
            self.spell_book.hidden = not self.spell_book.hidden
            if self.battle_master.is_battle_phase():
                self.battle_master.swap_battle_mode(GameModes.SPELL_BOOK)
            else:
                self.battle_master.swap_battle_mode()

    def handle_next_click(self, event, button):
        self.battle_master.reset_stage()
        self.battle_master.next_level()
        constants.globals.action_cooldown = 0
        self.next_button.hidden = True

    def handle_kill_switch(self, event, button):
        self.battle_master.kill_all_and_gain_experience()
        self.battle_master.move_to_victory_phase()

    def handle_kill_switch_and_next(self, event, button):
        self.battle_master.kill_all_and_gain_experience()
        self.battle_master.move_to_victory_phase()
        self.battle_master.next_level()

