#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

# button category
from interface.ui_elements.ui_element import UIElement


class UIButton(UIElement):
	def __init__(self, id, x, y, image, size_x, size_y):
		super().__init__()
		self.id = id
		self.image = pygame.transform.scale(image, (size_x, size_y))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def on_click(self, callback):
		self.events['click'] = callback

	def render(self):
		return self.image
