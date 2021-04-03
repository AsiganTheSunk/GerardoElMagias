#!/usr/bin/env python
# -*- coding: utf-8 -*-


class UIElement:
	def __init__(self):
		self.active = True
		self.hidden = False
		self.events = {}
