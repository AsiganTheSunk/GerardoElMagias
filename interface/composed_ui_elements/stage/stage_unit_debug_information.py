#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.constants.player_messages import CURRENT_TURN_MESSAGE, TOTAL_ENEMIES_MESSAGE


class StageUnitDebugInformation(UILayout):
    def __init__(self):
        super().__init__()
        self.static = False
        self.elements = []

    def update_ui_elements(self, current_enemies, total_enemies, current_unit_turn, current_unit_index, is_player_phase):
        self.reset_ui_elements()
        self.add_ui_element(UITextElement(TOTAL_ENEMIES_MESSAGE(current_enemies, total_enemies), (950, 30)))
        if is_player_phase:
            self.add_ui_element(UITextElement(CURRENT_TURN_MESSAGE(current_unit_turn, ''), (950, 50)))
        else:
            self.add_ui_element(UITextElement(CURRENT_TURN_MESSAGE(current_unit_turn, current_unit_index), (950, 50)))
