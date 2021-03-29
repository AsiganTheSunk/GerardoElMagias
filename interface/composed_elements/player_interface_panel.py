#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_images import gold_image, sword_image, loot_image, \
    victory_banner_image, defeat_banner_image

from pygame import Color, Rect, display, draw, transform, Surface, mouse
from core.game.game_event_control import event_controller
from interface.elements.ui_layout import UILayout


class PlayerInterfacePanel:
    def __init__(self, surface, width, height, panel_width, panel_height):
        self.surface = surface
        self.width = width
        self.height = height
        self.panel_width = panel_width
        self.panel_height = panel_height
        self.ui_elements = []

        self.sword_pointer = sword_image
        self.loot_pointer = loot_image

        self.gold_image = gold_image

        self.victory_banner_image = victory_banner_image
        self.defeat_banner_image = defeat_banner_image

    def add(self, element):
        self.ui_elements.append(element)
        event_controller.add_subscriber(element)
        if isinstance(element, UILayout):
            for sub_element in element.elements:
                event_controller.add_subscriber(sub_element)

    def display_bag_mouse(self):
        mouse.set_visible(False)
        self.surface.blit(self.loot_pointer, mouse.get_pos())

    def display_defeat_banner(self):
        self.surface.blit(defeat_banner_image, (380, 50))

    def display_victory_banner(self):
        self.surface.blit(self.victory_banner_image, (350, 50))

    def display_sword_mouse(self):
        mouse.set_visible(False)
        self.surface.blit(self.sword_pointer,  mouse.get_pos())

    def display_gold_icon(self):
        self.surface.blit(gold_image, (20, 20))

    @staticmethod
    def gradient_rect(window, left_colour, right_colour, target_rect):
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        colour_rect = Surface((2, 2))  # tiny! 2x2 bitmap
        draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
        draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
        colour_rect = transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
        window.blit(colour_rect, target_rect)  # paint it

    def display_panel_background(self):
        w, h = display.get_surface().get_size()
        w = w
        h = h + 188
        self.gradient_rect(self.surface, Color("SteelBlue"), Color("RoyalBlue"),
                           Rect(2, h / 2 + self.panel_height, w-4, self.panel_height))

        rect = Rect(1, h / 2 + self.panel_height + 1, w-2, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/5, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(w - w/2 + 2, h / 2 + self.panel_height + 1, w - w/2, self.panel_height)
        draw.rect(self.surface, Color("DimGray"), rect, 3)

        rect = Rect(w - w/2 + 2, h / 2 + self.panel_height + 1, w - w/2, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

        rect = Rect(1, h / 2 + self.panel_height + 1, w/5, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)

        rect = Rect(1, h / 2 + self.panel_height + 1, w-2, self.panel_height)
        draw.rect(self.surface, Color("Black"), rect, 1)
