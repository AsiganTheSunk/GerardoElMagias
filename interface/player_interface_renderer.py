#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.game_event_control import event_controller
from pygame import draw
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.ui_elements.ui_button import UIButton
from interface.ui_elements.ui_rect import UIRect
from interface.ui_elements.ui_gradient_rect import UIGradientRect
from interface.ui_elements.ui_transparent_rect import UITransparentRect


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

    def render_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    if isinstance(ui_element, UITextElement) or isinstance(ui_element, UIButton):
                        ui_surface_element, ui_element_position = ui_element.render()
                        self.surface.blit(ui_surface_element, ui_element_position)

                    elif isinstance(ui_element, UIRect):
                        color, x, y, width, height, border_size = ui_element.render()
                        draw.rect(self.surface, color, (x, y, width, height), border_size)

                    elif isinstance(ui_element, UITransparentRect):
                        alpha_surface, x, y = ui_element.render()
                        self.surface.blit(alpha_surface, (x, y))

                    elif isinstance(ui_element, UIGradientRect):
                        gradient_surface, x, y = ui_element.render()
                        self.surface.blit(gradient_surface, (x, y))
                    else:
                        self.surface.blit(ui_element.image, (ui_element.rect.x, ui_element.rect.y))
