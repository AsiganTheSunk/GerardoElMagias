#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.constants.player_messages import PLAYER_HP, PLAYER_MP, PLAYER_FURY, PLAYER_CONSUMABLE
from constants.game_fonts import default_font, small_interface_font


class PlayerBottomPanelInformation(UILayout):
    def __init__(self, game_attributes):
        super().__init__()
        self.game_attributes = game_attributes
        self.panel_height_correction = self.game_attributes.screen_height - self.game_attributes.panel_height
        self.static = False

    def update_ui_elements(self, player):
        self.reset_ui_elements()
        self.add_ui_element(UITextElement(PLAYER_HP(player.current_hp, player.max_hp),
                                          (530, self.panel_height_correction + 18)))
        self.add_ui_element(UITextElement(PLAYER_MP(player.current_mp, player.max_mp),
                                          (530, self.panel_height_correction + 37), font=small_interface_font))
        self.add_ui_element(UITextElement(PLAYER_FURY(player.current_fury, player.max_fury),
                                          (530, self.panel_height_correction + 52), font=small_interface_font))
        self.add_ui_element(UITextElement(PLAYER_CONSUMABLE(player.stash.healing_potions),
                                          (330, self.panel_height_correction + 85)))
        self.add_ui_element(UITextElement(PLAYER_CONSUMABLE(player.stash.mana_potions),
                                          (400, self.panel_height_correction + 85)))



