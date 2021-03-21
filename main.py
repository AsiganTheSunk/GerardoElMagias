#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Father Karras and AsiganTheSunk"
__copyright__ = "Copyright 2021, Gerardo El Magias"

__credits__ = ["Father Karras", "AsiganTheSunk", "GRAN CALAVERA", "Pechuza"]
__version__ = "0.1a"
__maintainer__ = "Father Karras, AsiganTheSunk and GRAN CALAVERA"
__email__ = ""
__status__ = "Development"

# Hide Support Message, this must be placed before pygame init Import
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Pygame Init Import:
from pygame import init

init()

# Game Engine Import:
from game_engine import GameEngine


game = GameEngine()
game.run()


