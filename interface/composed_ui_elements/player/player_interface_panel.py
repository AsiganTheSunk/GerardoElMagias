#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_images import gold_image, sword_image, loot_image, \
    victory_banner_image, defeat_banner_image
from pygame import Color, Rect, transform, Surface, mouse
from pygame import display, draw

from interface.ui_elements.ui_image import UIImage
from interface.ui_elements.ui_rect import UIRect
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_gradient_rect import UIGradientRect


class MouseBag(UIImage):
    def __init__(self):
        x, y = mouse.get_pos()
        mouse.set_visible(False)
        super().__init__(loot_image, x, y)

    def render(self):
        return self.image, self.x, self.y


class MouseSword(UIImage):
    def __init__(self):
        x, y = mouse.get_pos()
        mouse.set_visible(False)
        super().__init__(sword_image, x, y)

    def render(self):
        return self.image, self.x, self.y


class PlayerInterfacePanel(UILayout):
    def __init__(self, game_attributes):
        super().__init__()
        self.game_attributes = game_attributes
        self.surface = self.game_attributes.surface

        self.gold_image = gold_image

        self.victory_banner_image = victory_banner_image
        self.defeat_banner_image = defeat_banner_image

        w, h = display.get_surface().get_size()
        w = w
        h = h + 188

        self.add_ui_element(UIGradientRect(2, h / 2 + self.game_attributes.panel_height, w - 4,
                                           self.game_attributes.panel_height))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w - 2,
                                   self.game_attributes.panel_height, 3, Color("DimGray")))
        self.add_ui_element(UIRect(w - w / 3 + 2, h / 2 + self.game_attributes.panel_height + 1, w - w / 2,
                                   self.game_attributes.panel_height, 3, Color("DimGray")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w / 3,
                                   self.game_attributes.panel_height, 3, Color("DimGray")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w / 5,
                                   self.game_attributes.panel_height, 3, Color("DimGray")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w / 10,
                                   self.game_attributes.panel_height, 3, Color("DimGray")))
        self.add_ui_element(UIRect(w - w / 3 + 2, h / 2 + self.game_attributes.panel_height + 1, w - w / 2,
                                   self.game_attributes.panel_height, 1, Color("Black")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w / 3,
                                   self.game_attributes.panel_height, 1, Color("Black")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w / 5,
                                   self.game_attributes.panel_height, 1, Color("Black")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w / 10,
                                   self.game_attributes.panel_height, 1, Color("Black")))
        self.add_ui_element(UIRect(1, h / 2 + self.game_attributes.panel_height + 1, w - 2,
                                   self.game_attributes.panel_height, 1, Color("Black")))

        self.add_ui_element(UIImage(gold_image, 20, 20))

    def display_bag_mouse(self):
        mouse_bag = MouseBag()
        image, x, y = mouse_bag.render()
        self.surface.blit(image, (x, y))

    def display_defeat_banner(self):
        UIImage(defeat_banner_image, 380, 50)
        self.surface.blit(defeat_banner_image, (380, 50))

    def display_victory_banner(self):
        UIImage(victory_banner_image, 380, 50)
        self.surface.blit(self.victory_banner_image, (350, 50))

    def display_sword_mouse(self):
        mouse_bag = MouseSword()
        image, x, y = mouse_bag.render()
        self.surface.blit(image, (x, y))

    def display_gold_icon(self):
        gold_icon = UIImage(gold_image, 20, 20)
        # image, x, y = gold_icon.render()
        self.surface.blit(gold_image, (20, 20))

    def display_panel_background(self):
        pass