#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import font


# Fonts:
tahoma_font_path = './resources/fonts/Tahoma.ttf'
verdana_font_path = './resources/fonts/Verdana.ttf'

# Pygame Fonts:
default_font = font.Font(tahoma_font_path, 26)
interface_font = font.Font(tahoma_font_path, 15)

# Combat Fonts:
combat_text_font = font.Font(verdana_font_path, 32)

cast_text_font = font.Font(verdana_font_path, 26)
cast_text_font.set_italic(True)

critical_combat_text_font = font.Font(verdana_font_path, 34)
critical_combat_text_font.set_bold(True)

