#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pygame import mouse, transform, Surface, time, SRCALPHA, font, Color, surfarray, draw, display, Rect
from interface.ui_elements.ui_element import UIElement
from numpy import array


class UIButton(UIElement):
	def __init__(self, ui_identifier, x, y, image, image_width, image_height):
		super().__init__()
		self.ui_identifier = ui_identifier

		self.x = x
		self.y = y

		self.image_width = image_width
		self.image_height = image_height

		# Create a grey image instead of doing it on loading button, cause this causes slow down
		self.image = transform.scale(image, (self.image_width, self.image_height))
		self.clicked_image = transform.scale(image, (self.image_width - 2, self.image_height - 2))
		self.inactive_image = self.grayscale(self.image)
		self.inactive_clicked_image = self.grayscale(self.clicked_image)

		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

		self.clicked = False
		self.mouse_over = False

	def on_click(self, callback):
		self.events['click'] = callback

	def on_key_bind(self, callback):
		self.events['key_bind'] = callback

	def render(self):
		if not self.active:
			if self.clicked:
				return self.inactive_clicked_image, (self.rect.x + 2, self.rect.y + 2)
			return self.inactive_image, (self.rect.x, self.rect.y)
		else:
			if self.clicked:
				return self.clicked_image, (self.rect.x + 2, self.rect.y + 2)
			return self.image, (self.rect.x, self.rect.y)

	@staticmethod
	def grayscale(img):
		arr = surfarray.array3d(img)
		# Luminosity Filter
		avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
		arr = array([[[avg, avg, avg] for avg in col] for col in avgs])
		return surfarray.make_surface(arr)
