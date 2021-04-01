#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_colors import RED_COLOR
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.constants.player_messages import CURRENT_STAGE
from constants.game_fonts import default_font


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
        self.add(UITextElement(CURRENT_STAGE(stage_realm.value, stage_level), (490, 25), color=RED_COLOR, font=default_font))
