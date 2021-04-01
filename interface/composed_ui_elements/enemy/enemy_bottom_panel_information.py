#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.constants.player_messages import BOSS_UNIT_TITLE_MESSAGE, ENEMY_UNIT_TITLE_MESSAGE
from interface.constants.enemy_unit_panel_data import ENEMY_UNIT_PANEL_DATA


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
                                   (ENEMY_UNIT_PANEL_DATA[0][0],
                                    ENEMY_UNIT_PANEL_DATA[0][1](self.panel_height_correction))))
        else:
            for enemy_index, enemy_unit in enumerate(enemy_unit_list):
                self.add(UITextElement(ENEMY_UNIT_TITLE_MESSAGE(enemy_unit.name, enemy_index + 1),
                                       (ENEMY_UNIT_PANEL_DATA[enemy_index][0],
                                        ENEMY_UNIT_PANEL_DATA[enemy_index][1](self.panel_height_correction))))