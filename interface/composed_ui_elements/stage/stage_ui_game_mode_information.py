#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.constants.player_messages import NEXT_BATTLE_MESSAGE, DEFEAT_MESSAGE, VICTORY_MESSAGE
from core.game.constants.game_modes import GameModes
from constants.game_fonts import default_font
from constants.game_colors import LIGHT_ORANGE_COLOR


class StageUIGameModeInformation(UILayout):
    def __init__(self):
        super().__init__()
        self.static = False

    def update_ui_elements(self, game_mode):
        self.reset_ui_elements()
        if game_mode is GameModes.VICTORY:
            self.add_ui_element(UITextElement(VICTORY_MESSAGE, (435, 70), font=default_font, color=LIGHT_ORANGE_COLOR))
            self.add_ui_element(UITextElement(NEXT_BATTLE_MESSAGE, (470, 450), font=default_font, color=LIGHT_ORANGE_COLOR))
        elif game_mode is GameModes.DEFEAT:
            self.add_ui_element(UITextElement(DEFEAT_MESSAGE, (440, 70), font=default_font, color=LIGHT_ORANGE_COLOR))
        else:
            self.reset_ui_elements()
