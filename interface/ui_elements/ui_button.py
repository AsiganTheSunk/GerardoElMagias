#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mouse, transform, Surface, time, SRCALPHA, font, Color, surfarray, draw, display, Rect
from interface.ui_elements.ui_element import UIElement


class UIButton(UIElement):
	def __init__(self, ui_identifier, x, y, image, image_width, image_height):
		super().__init__()
		self.ui_identifier = ui_identifier

		self.x = x
		self.y = y

		self.image_width = image_width
		self.image_height = image_height

		self.image = transform.scale(image, (self.image_width, self.image_height))
		self.clicked_image = transform.scale(image, (self.image_width - 2, self.image_height - 2))

		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

		self.clicked = False

	def on_click(self, callback):
		self.events['click'] = callback

	def on_mouse_over(self, callback):
		self.events['mouse_over'] = callback

	def on_key_bind(self, callback):
		self.events['keybind'] = callback

	def render(self):
		if self.clicked:
			return self.clicked_image, (self.rect.x + 2, self.rect.y + 2)
		return self.image, (self.rect.x, self.rect.y)
