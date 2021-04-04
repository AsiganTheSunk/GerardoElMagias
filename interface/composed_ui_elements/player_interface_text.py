#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_layout import UILayout
from interface.composed_ui_elements.player.player_bottom_panel_information import PlayerBottomPanelInformation
from interface.composed_ui_elements.player.player_stat_information import PlayerStatInformation
from interface.composed_ui_elements.enemy.enemy_bottom_panel_information import EnemyBottomPanelInformation
from interface.composed_ui_elements.stage.stage_ui_information import StageUIInformation
from interface.composed_ui_elements.stage.stage_ui_game_mode_information import StageUIGameModeInformation
from interface.composed_ui_elements.stage.stage_unit_debug_information import StageUnitDebugInformation


class PlayerUITextStageInformation(UILayout):
    def __init__(self, game_attributes):
        super().__init__()

        self.ui_text_elements = [
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

    def update_ui_text_elements(self, battle_master):
        # Unpack BattleMaster Data
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

        self.ui_text_elements[0].update(player)
        self.ui_text_elements[1].update(player)
        self.ui_text_elements[2].update(is_boss_level, current_enemy_unit_list)
        self.ui_text_elements[3].update(current_realm, current_level)
        self.ui_text_elements[4].update(current_game_mode)
        self.ui_text_elements[5].update(current_enemy_unit_number, current_alive_enemy_unit_list,
                                        current_unit, current_unit_index, battle_master.is_player_phase())
