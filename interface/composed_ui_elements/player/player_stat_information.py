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

        self.elements = []

    def add(self, ui_text_element):
        self.elements.append(ui_text_element)

    def reset(self):
        self.elements = []

    def update(self, player):
        self.reset()
        self.add(UITextElement(player.stash.gold, (80, 30), color=YELLOW_COLOR, font=default_font))
        self.add(UITextElement(LEVEL_MESSAGE(player.level), (150, 30)))
        self.add(UITextElement(EXPERIENCE_MESSAGE(player.experience, player.exp_level_break), (150, 50)))
        self.add(UITextElement(STRENGHT_MESSAGE(player.strength), (150, 70)))
        self.add(UITextElement(DEXTERITY_MESSAGE(player.dexterity), (150, 90)))
        self.add(UITextElement(MAGIC_MESSAGE(player.magic), (150, 110)))
        self.add(UITextElement(VITALITAD_MESSAGE(player.vitality), (150, 130)))
        self.add(UITextElement(RESILIENCE_MESSAGE(player.resilience), (150, 150)))
        self.add(UITextElement(LUCK_MESSAGE(player.luck), (150, 170)))
        self.add(UITextElement(ATTACK_POWER(player.attack_power), (150, 190)))
        self.add(UITextElement(ATTACK_RATING(player.attack_rating), (150, 210)))
        self.add(UITextElement(MAGIC_POWER(player.magic_power), (150, 230)))
