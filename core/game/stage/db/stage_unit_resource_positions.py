# !/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class StageUnitMatrix(Enum):
    PLAYER = 0      # Player Resource Position Index
    ENEMY_00 = 1    # Enemy 00 Resource Position Index
    ENEMY_01 = 2    # Enemy 01 Resource Position Index
    ENEMY_10 = 3    # Enemy 10 Resource Position Index
    ENEMY_11 = 4    # Enemy 11 Resource Position Index


STAGE_UNIT_UI_RESOURCE_POSITIONS = [
    [
        (440, lambda stage_unit_height_correction: stage_unit_height_correction + 20),
        (440, lambda stage_unit_height_correction: stage_unit_height_correction + 40),
        (440, lambda stage_unit_height_correction: stage_unit_height_correction + 35)
    ],
    [
        (870, lambda stage_unit_height_correction: stage_unit_height_correction + 20)
    ],
    [
        (870, lambda stage_unit_height_correction: stage_unit_height_correction + 80)
    ],
    [
        (1070, lambda stage_unit_height_correction: stage_unit_height_correction + 20)
    ],
    [
        (1070, lambda stage_unit_height_correction: stage_unit_height_correction + 80)
    ]
]