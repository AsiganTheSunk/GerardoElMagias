#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from core.game.game_event_control import event_controller
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_rect import UIRect


class PlayerInterfaceRenderer:
    def __init__(self, surface):
        self.surface = surface
        self.ui_elements = []

    def add(self, element):
        self.ui_elements.append(element)
        event_controller.add_subscriber(element)
        if isinstance(element, UILayout):
            for sub_element in element.elements:
                event_controller.add_subscriber(sub_element)

    def render_interface(self):
        self.render_ui_elements(self.ui_elements)

    def render_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    self.blit(ui_element)

    def blit(self, ui_element):
        if isinstance(ui_element, UIRect):
            draw.rect(self.surface, *ui_element.render())
        else:
            self.surface.blit(*ui_element.render())
