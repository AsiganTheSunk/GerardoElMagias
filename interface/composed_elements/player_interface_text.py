#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_colors import YELLOW_COLOR, WHITE_COLOR, RED_COLOR
from constants.game_fonts import default_font, interface_font
from core.game.stage.db.stage_unit_ui_data_positions import STAGE_UNIT_UI_DATA_POSITIONS
from interface.elements.ui_layout import UILayout
from interface.elements.ui_text_element import UITextElement
from interface.constants.player_messages import LEVEL_MESSAGE, EXPERIENCE_MESSAGE, STRENGHT_MESSAGE, \
    DEXTERITY_MESSAGE, MAGIC_MESSAGE, VITALITAD_MESSAGE, RESILIENCE_MESSAGE, LUCK_MESSAGE, CURRENT_STAGE, \
    PLAYER_HP, PLAYER_MP, PLAYER_FURY, PLAYER_CONSUMABLE, BOSS_UNIT_TITLE_MESSAGE, ENEMY_UNIT_TITLE_MESSAGE, \
    ENEMY_UNIT_PANEL_DATA, NEXT_BATTLE_MESSAGE, DEFEAT_MESSAGE, VICTORY_MESSAGE, CURRENT_TURN_MESSAGE, \
    TOTAL_ENEMIES_MESSAGE


from core.game.constants.game_modes import GameModes




class PlayerStatInformation(UILayout):
    def __init__(self, battle_master):
        super().__init__()
        self.player = battle_master.get_hero()

        self.elements = [
            UITextElement(self.player.stash.gold, (80, 30)),
            UITextElement(LEVEL_MESSAGE(self.player.level), (80, 30)),
            UITextElement(EXPERIENCE_MESSAGE(self.player.experience, self.player.exp_level_break), (80, 30)),
            UITextElement(STRENGHT_MESSAGE(self.player.strength), (150, 125)),
            UITextElement(DEXTERITY_MESSAGE(self.player.dexterity), (150, 175)),
            UITextElement(MAGIC_MESSAGE(self.player.magic), (150, 175)),
            UITextElement(VITALITAD_MESSAGE(self.player.vitality), (150, 175)),
            UITextElement(RESILIENCE_MESSAGE(self.player.resilience), (150, 175)),
            UITextElement(LUCK_MESSAGE(self.player.luck), (150, 175)),
        ]


class EnemyBottomPanelInformation(UILayout):
    def __init__(self, battle_master, game_attributes):
        super().__init__()
        self.battle_master = battle_master
        self.game_attributes = game_attributes

        self.panel_height_correction = self.game_attributes.screen_height - self.game_attributes.panel_height

        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, is_boss_battle, enemy_unit_list):
        self.reset()
        if is_boss_battle:
            self.add(UITextElement(BOSS_UNIT_TITLE_MESSAGE(enemy_unit_list[0].name),
                                   (680, self.panel_height_correction + 5)))
        else:
            for enemy_index, enemy_unit in enumerate(enemy_unit_list):
                self.add(UITextElement(ENEMY_UNIT_TITLE_MESSAGE(enemy_unit.value, enemy_index),
                                       (ENEMY_UNIT_PANEL_DATA[enemy_index][0],
                                        ENEMY_UNIT_PANEL_DATA[enemy_index][1](self.panel_height_correction))))


class PlayerBottomPanelInformation(UILayout):
    def __init__(self, battle_master, game_attributes):
        super().__init__()
        self.player = battle_master.get_hero()
        self.game_attributes = game_attributes

        panel_height_correction = self.game_attributes.screen_height - self.game_attributes.panel_height

        self.elements = [
            UITextElement(PLAYER_HP(self.player.current_hp, self.player.max_hp), (440, panel_height_correction + 18)),
            UITextElement(PLAYER_MP(self.player.current_mp, self.player.max_mp), (440, panel_height_correction + 38)),
            UITextElement(PLAYER_FURY(self.player.current_fury, self.player.max_fury), (440, panel_height_correction + 58)),
            UITextElement(PLAYER_CONSUMABLE(self.player.stash.healing_potions), (190, panel_height_correction + 20)),
            UITextElement(PLAYER_CONSUMABLE(self.player.stash.mana_potions), (190, panel_height_correction + 80)),
        ]


class StageUIInformation(UILayout):
    def __init__(self, stage_realm, stage_level):
        super().__init__()
        self.stage_realm = stage_realm
        self.stage_level = stage_level

    def render(self):
        return UITextElement(CURRENT_STAGE(self.get_stage_realm().value, self.get_stage_level().value), (510, 25),
                             color=RED_COLOR)

    def get_stage_realm(self):
        return self.stage_realm

    def get_stage_level(self):
        return self.stage_level

    def set_stage_realm(self, stage_realm):
        self.stage_realm = stage_realm

    def set_stage_level(self, stage_level):
        self.stage_level = stage_level

    def update(self, stage_realm, stage_level):
        self.set_stage_realm(stage_realm)
        self.set_stage_level(stage_level)


class StageUnitDebugInformation(UILayout):
    def __init__(self, battle_master):
        super().__init__()
        self.battle_master = battle_master
        self.elements = [

        ]

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, current_enemies, total_enemies, current_unit_turn, next_unit_turn):
        self.add(UITextElement(TOTAL_ENEMIES_MESSAGE(current_enemies, total_enemies), (600, 100)))
        self.add(UITextElement(CURRENT_TURN_MESSAGE(current_unit_turn, next_unit_turn), (600, 125)))


class StageUIGameModeInformation(UILayout):
    def __init__(self):
        super().__init__()
        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, game_mode):
        if game_mode is GameModes.VICTORY:
            self.add(UITextElement(VICTORY_MESSAGE, (540, 270)))
            self.add(UITextElement(NEXT_BATTLE_MESSAGE, (500, 300)))
        elif game_mode is GameModes.DEFEAT:
            self.add(UITextElement(DEFEAT_MESSAGE, (540, 270)))


class PlayerUITextStageInformation:
    def __init__(self, battle_master, game_attributes):
        # Player Related UI Information

        self.player_ui_text_stage_information_elements = [
            PlayerStatInformation(battle_master),
            PlayerBottomPanelInformation(battle_master, game_attributes)
        ]

        # Enemy Related UI Information
        # self.enemy_bottom_panel_information = EnemyBottomPanelInformation(battle_master, game_attributes)

        # Stage Related UI Information
        # self.stage_ui_game_mode_information = StageUIGameModeInformation()
        # self.stage_ui_information = StageUIInformation(battle_master.current_stage_realm, battle_master.level)
        # self.stage_unit_debug_information = StageUnitDebugInformation(battle_master)

#
# class PlayerInterfaceDataRenderer:
#     def __init__(self, surface, battle_master, game_attributes):
#         self.surface = surface
#         self.game_attributes = game_attributes
#         self.battle_master = battle_master
#
#         self.player_ui_stage_information = PlayerUITextStageInformation(battle_master, game_attributes)
#
#         self.render_ui_elements(self.player_ui_stage_information.elements)
#
    def render_text_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    ui_surface_element, ui_element_position = ui_element.render()
                    self.surface.blit(ui_surface_element, ui_element_position)



