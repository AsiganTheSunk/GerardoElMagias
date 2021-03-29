#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class UnitAnimationType(Enum):
    IDLE = 'Idle'
    ATTACK = 'Attack'
    HURT = 'Hurt'
    DEATH = 'Death'
    BLOCK = 'Block'
    MISS = 'Miss'
    SHADOWBOLT = "ShadowBolt"
    MATERIALIZE = "Materialize"


