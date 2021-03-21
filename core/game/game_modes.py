#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class GameModes(Enum):
    BATTLE = 0
    BOSS_BATTLE = 1
    VICTORY = 2
    DEFEAT = 3
    SPELLBOOK = 4