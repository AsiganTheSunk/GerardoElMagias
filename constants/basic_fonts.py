#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import font, init

init()

# Define Game Fonts:
default_font = font.SysFont("Tahoma", 26)
combat_text_font = font.SysFont("Verdana", 32)

cast_text_font = font.SysFont("Verdana", 32, True, True)
critical_combat_text_font = font.SysFont("Verdana", 34, True)

