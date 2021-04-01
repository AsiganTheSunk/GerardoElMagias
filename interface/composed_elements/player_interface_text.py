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
    def __init__(self):
        super().__init__()

        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, player):
        self.reset()
        self.add(UITextElement(player.stash.gold, (80, 30)))
        self.add(UITextElement(LEVEL_MESSAGE(player.level), (150, 30)))
        self.add(UITextElement(EXPERIENCE_MESSAGE(player.experience, player.exp_level_break), (150, 60)))
        self.add(UITextElement(STRENGHT_MESSAGE(player.strength), (150, 90)))
        self.add(UITextElement(DEXTERITY_MESSAGE(player.dexterity), (150, 120)))
        self.add(UITextElement(MAGIC_MESSAGE(player.magic), (150, 150)))
        self.add(UITextElement(VITALITAD_MESSAGE(player.vitality), (150, 180)))
        self.add(UITextElement(RESILIENCE_MESSAGE(player.resilience), (150, 210)))
        self.add(UITextElement(LUCK_MESSAGE(player.luck), (150, 240)))


class EnemyBottomPanelInformation(UILayout):
    def __init__(self, game_attributes):
        super().__init__()
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
                self.add(UITextElement(ENEMY_UNIT_TITLE_MESSAGE(enemy_unit.name, enemy_index + 1),
                                       (ENEMY_UNIT_PANEL_DATA[enemy_index][0],
                                        ENEMY_UNIT_PANEL_DATA[enemy_index][1](self.panel_height_correction))))


class PlayerBottomPanelInformation(UILayout):
    def __init__(self, game_attributes):
        super().__init__()
        self.game_attributes = game_attributes
        self.panel_height_correction = self.game_attributes.screen_height - self.game_attributes.panel_height
        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, player):
        self.reset()
        self.add(UITextElement(PLAYER_HP(player.current_hp, player.max_hp), (440, self.panel_height_correction + 18)))
        self.add(UITextElement(PLAYER_MP(player.current_mp, player.max_mp), (440, self.panel_height_correction + 38)))
        self.add(UITextElement(PLAYER_FURY(player.current_fury, player.max_fury), (440, self.panel_height_correction + 58)))
        self.add(UITextElement(PLAYER_CONSUMABLE(player.stash.healing_potions), (190, self.panel_height_correction + 20)))
        self.add(UITextElement(PLAYER_CONSUMABLE(player.stash.mana_potions), (190, self.panel_height_correction + 80)))


class StageUIInformation(UILayout):
    def __init__(self):
        super().__init__()
        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, stage_realm, stage_level):
        self.reset()
        self.add(UITextElement(CURRENT_STAGE(stage_realm.value, stage_level), (510, 25), color=RED_COLOR))


class StageUnitDebugInformation(UILayout):
    def __init__(self):
        super().__init__()
        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, current_enemies, total_enemies, current_unit_turn, current_unit_index, is_player_phase):
        self.reset()
        self.add(UITextElement(TOTAL_ENEMIES_MESSAGE(current_enemies, total_enemies), (600, 100)))
        if is_player_phase:
            self.add(UITextElement(CURRENT_TURN_MESSAGE(current_unit_turn, ''), (600, 125)))
        else:
            self.add(UITextElement(CURRENT_TURN_MESSAGE(current_unit_turn, current_unit_index), (600, 125)))


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


class PlayerUITextStageInformation(UILayout):
    def __init__(self, game_attributes):
        super().__init__()

        self.text_elements = [
            # Player Related UI Information
            PlayerStatInformation(),
            PlayerBottomPanelInformation(game_attributes),
            # Enemy Related UI Information
            EnemyBottomPanelInformation(game_attributes),
            # Stage Related UI Information
            StageUIInformation(),
            StageUIGameModeInformation(),
            StageUnitDebugInformation(),
        ]

    def update_ui_text_stage_information(self, battle_master):
        player = battle_master.friendly_fighters[0]
        current_level = battle_master.level
        current_realm = battle_master.current_stage()
        current_game_mode = battle_master.game_mode
        current_enemy_unit_list = battle_master.enemy_fighters
        current_enemy_unit_number = len(battle_master.enemy_fighters)
        current_alive_enemy_unit_list = len(list(filter(lambda fighter: fighter.alive, battle_master.enemy_fighters)))
        current_unit = battle_master.current_fighter.name
        current_unit_index = (battle_master.current_fighter_index % len(battle_master.enemy_fighters) + 1)
        is_boss_level = battle_master.is_boss_level()

        self.text_elements[0].update(player)
        self.text_elements[1].update(player)
        self.text_elements[2].update(is_boss_level, current_enemy_unit_list)
        self.text_elements[3].update(current_realm, current_level)
        self.text_elements[4].update(current_game_mode)
        self.text_elements[5].update(current_enemy_unit_number, current_alive_enemy_unit_list,
                                     current_unit, current_unit_index, battle_master.is_player_phase())
