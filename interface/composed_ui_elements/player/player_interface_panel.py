#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_images import gold_image, sword_image, loot_image, \
    victory_banner_image, defeat_banner_image
from pygame import Color, Rect, transform, Surface, mouse
from pygame import display, draw

from interface.ui_elements.ui_image import UIImage


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


class PlayerInterfacePanel:
    def __init__(self, game_attributes):
        self.game_attributes = game_attributes
        self.surface = self.game_attributes.surface
        self.width = self.game_attributes.screen_width
        self.height = self.game_attributes.screen_height
        self.panel_height = self.game_attributes.panel_height

        self.elements = []

        self.gold_image = gold_image

        self.victory_banner_image = victory_banner_image
        self.defeat_banner_image = defeat_banner_image

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
        UIImage(gold_image, 20, 20)
        self.surface.blit(gold_image, (20, 20))

    def display_panel_background(self):
        w, h = display.get_surface().get_size()
        w = w
        h = h + 188
        self.gradient_rect(self.surface, Color("SteelBlue"), Color("RoyalBlue"),
                           Rect(2, h / 2 + self.panel_height, w-4, self.panel_height))

        rect = Rect(1, h / 2 + self.panel_height + 1, w-2, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/3, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(w - w/3 + 2, h / 2 + self.panel_height + 1, w - w/2, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/5, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/10, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(w - w/3 + 2, h / 2 + self.panel_height + 1, w - w/2, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/3, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/5, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/10, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

        rect = Rect(1, h / 2 + self.panel_height + 1, w-2, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

    @staticmethod
    def gradient_rect(surface, left_colour, right_colour, target_rect):
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        colour_rect = Surface((2, 2))  # tiny! 2x2 bitmap
        draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
        draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
        colour_rect = transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
        surface.blit(colour_rect, target_rect)  # paint it