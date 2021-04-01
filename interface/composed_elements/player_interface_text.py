#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_colors import YELLOW_COLOR, WHITE_COLOR, RED_COLOR
from constants.game_fonts import default_font, interface_font
from core.game.stage.db.stage_unit_ui_data_positions import STAGE_UNIT_UI_DATA_POSITIONS
from interface.elements.ui_layout import UILayout

class PlayerInterfaceDataRenderer:
    def __init__(self, surface, game_attributes):
        self.surface = surface
        self.game_attributes = game_attributes

    def render_text(self, message, font, color, message_position):
        message_font_surface = font.render(message, True, color)
        self.surface.blit(message_font_surface, message_position)


class PlayerStatInformation(UILayout):
    def __init__(self, player_interface_data_renderer):
        super().__init__()

        self.player_interface_data_renderer = player_interface_data_renderer

        self.elements = [

        ]


    def display_player_information(self, level, player):
        self.player_interface_data_renderer.render_text(f"{player.stash.gold}", default_font, YELLOW_COLOR, 80, 30)
        self.player_interface_data_renderer.render_text(f"Nivel: {player.level}", default_font, WHITE_COLOR, 150, 100)
        self.player_interface_data_renderer.render_text(f"Experiencia: [ {player.experience}/{player.exp_level_break} ]", default_font, WHITE_COLOR, 150, 125)
        self.player_interface_data_renderer.render_text(f"Fuerza: {player.strength}", default_font, WHITE_COLOR, 150, 175)
        self.player_interface_data_renderer.render_text(f"Destreza: {player.dexterity}", default_font, WHITE_COLOR, 150, 200)
        self.player_interface_data_renderer.render_text(f"Poder Mágico: {player.magic}", default_font, WHITE_COLOR, 150, 225)
        self.player_interface_data_renderer.render_text(f"Vitalidad: {player.vitality}", default_font, WHITE_COLOR, 150, 250)
        self.player_interface_data_renderer.render_text(f"Resiliencia: {player.resilience}", default_font, WHITE_COLOR, 150, 275)
        self.player_interface_data_renderer.render_text(f"Suerte: {player.luck}", default_font, WHITE_COLOR, 150, 300)
        # self.display_stage_information(level)


class PlayerInterfaceText:
    def __init__(self, surface, width, height, panel_width, panel_height):
        self.surface = surface
        self.width = width
        self.height = height
        self.panel_width = panel_width
        self.panel_height = panel_height

    # create function for drawing text
    def display_text(self, text, font, color, x, y):
        font_surface = font.render(text, True, color)
        self.surface.blit(font_surface, (x, y))

    def display_player_information(self, level, player):
        self.display_text(f"{player.stash.gold}", default_font, YELLOW_COLOR, 80, 30)
        self.display_text(f"Nivel: {player.level}", default_font, WHITE_COLOR, 150, 100)
        self.display_text(f"Experiencia: [ {player.experience}/{player.exp_level_break} ]", default_font, WHITE_COLOR, 150, 125)
        self.display_text(f"Fuerza: {player.strength}", default_font, WHITE_COLOR, 150, 175)
        self.display_text(f"Destreza: {player.dexterity}", default_font, WHITE_COLOR, 150, 200)
        self.display_text(f"Poder Mágico: {player.magic}", default_font, WHITE_COLOR, 150, 225)
        self.display_text(f"Vitalidad: {player.vitality}", default_font, WHITE_COLOR, 150, 250)
        self.display_text(f"Resiliencia: {player.resilience}", default_font, WHITE_COLOR, 150, 275)
        self.display_text(f"Suerte: {player.luck}", default_font, WHITE_COLOR, 150, 300)
        self.display_stage_information(level)

    def display_next_battle_message(self):
        self.display_text(f" Next Battle ", default_font, RED_COLOR, 980, 270)

    def display_victory_message(self):
        self.display_text(f" GET YOUR LOOT! ", default_font, RED_COLOR, 530, 300)
        self.display_next_battle_message()

    def display_defeat_message(self):
        self.display_text(f" YOU ARE A NOOB ", default_font, RED_COLOR, 540, 350)

    def display_stage_information(self, level):
        if level <= 7:
            self.display_text(f"THE WOODS: STAGE {level}", default_font, RED_COLOR, 510, 25)
        elif level <= 14:
            self.display_text(f"THE CASTLE: STAGE {level - 7}", default_font, RED_COLOR, 510, 25)
        else:
            self.display_text(f"THE DUNGEON: STAGE {level - 15}", default_font, RED_COLOR, 510, 25)

    def display_debug_information(self, _current_fighter, _total_fighters):
        self.display_text(f"Total fighters: {_total_fighters}", default_font, YELLOW_COLOR, 600, 100)
        self.display_text(f"Current fighter: {_current_fighter}", default_font, YELLOW_COLOR, 600, 125)

    def display_player_bottom_panel_information(self, player):
        # show hero stats
        self.display_text(f"HP: {player.current_hp} / {player.max_hp}",
                          interface_font, WHITE_COLOR, 440, self.height - self.panel_height + 18)
        self.display_text(f"MP: {player.current_mp} / {player.max_mp}",
                          interface_font, WHITE_COLOR, 440, self.height - self.panel_height + 38)

        self.display_text(f"FP: {player.current_fury} / {player.max_fury}",
                          interface_font, WHITE_COLOR, 440, self.height - self.panel_height + 58)
        # show number of pots
        self.display_text(f"x{player.stash.healing_potions}", default_font, WHITE_COLOR, 190,
                          self.height - self.panel_height + 20)
        # show number of lightnings
        self.display_text(f"x{player.stash.mana_potions}", default_font, WHITE_COLOR, 190,
                          self.height - self.panel_height + 80)

    def display_enemy_bottom_panel_information(self, scripted_battle, enemy_list):
        # draw name and health of enemy
        ENEMY_TEXT_POS_0 = [680, self.height - self.panel_height + 5]
        ENEMY_TEXT_POS_1 = [680, self.height - self.panel_height + 65]
        ENEMY_TEXT_POS_2 = [900, self.height - self.panel_height + 5]
        ENEMY_TEXT_POS_3 = [900, self.height - self.panel_height + 65]

        # STAGE_UNIT_UI_DATA_POSITIONS
        tmp = [
            ENEMY_TEXT_POS_0,
            ENEMY_TEXT_POS_1,
            ENEMY_TEXT_POS_2,
            ENEMY_TEXT_POS_3
        ]

        if scripted_battle:
            self.display_text(f" {enemy_list[0].name}", default_font, WHITE_COLOR, tmp[0][0], tmp[0][1])
        else:
            for index, enemy_fighter in enumerate(enemy_list):
                self.display_text(f"{enemy_fighter.name} {index + 1}", default_font, WHITE_COLOR, tmp[index][0], tmp[index][1])

