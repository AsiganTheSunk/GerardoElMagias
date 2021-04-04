#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.constants.player_messages import LEVEL_MESSAGE, EXPERIENCE_MESSAGE, STRENGHT_MESSAGE, \
    DEXTERITY_MESSAGE, MAGIC_MESSAGE, VITALITAD_MESSAGE, RESILIENCE_MESSAGE, LUCK_MESSAGE, \
    ATTACK_POWER, ATTACK_RATING, MAGIC_POWER
from constants.game_fonts import default_font
from constants.game_colors import YELLOW_COLOR


class PlayerStatInformation(UILayout):
    def __init__(self):
        super().__init__()
        self.static = False

    def update_ui_elements(self, player):
        self.reset_ui_elements()
        self.add_ui_element(UITextElement(player.stash.gold, (80, 30), color=YELLOW_COLOR, font=default_font))
        self.add_ui_element(UITextElement(LEVEL_MESSAGE(player.level), (150, 30)))
        self.add_ui_element(UITextElement(EXPERIENCE_MESSAGE(player.experience, player.exp_level_break), (150, 50)))
        self.add_ui_element(UITextElement(STRENGHT_MESSAGE(player.strength), (150, 70)))
        self.add_ui_element(UITextElement(DEXTERITY_MESSAGE(player.dexterity), (150, 90)))
        self.add_ui_element(UITextElement(MAGIC_MESSAGE(player.magic), (150, 110)))
        self.add_ui_element(UITextElement(VITALITAD_MESSAGE(player.vitality), (150, 130)))
        self.add_ui_element(UITextElement(RESILIENCE_MESSAGE(player.resilience), (150, 150)))
        self.add_ui_element(UITextElement(LUCK_MESSAGE(player.luck), (150, 170)))
        self.add_ui_element(UITextElement(ATTACK_POWER(player.attack_power), (150, 190)))
        self.add_ui_element(UITextElement(ATTACK_RATING(player.attack_rating), (150, 210)))
        self.add_ui_element(UITextElement(MAGIC_POWER(player.magic_power), (150, 230)))
