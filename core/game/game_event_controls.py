#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import event, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import constants.globals


def event_control():
    for _event in event.get():
        if _event.type == QUIT:
            constants.globals.run_game = False
            constants.globals.run_stage = False

        if _event.type == MOUSEBUTTONDOWN:
            constants.globals.clicked = True

        if _event.type == MOUSEBUTTONUP:
            constants.globals.clicked = False
