#!/usr/bin/env python
# -*- coding: utf-8 -*-

STAGE_UNIT_UI_DATA_POSITIONS = [
    [
        (270, lambda stage_data_height_correction: stage_data_height_correction + 20),
        (270, lambda stage_data_height_correction: stage_data_height_correction + 40),
        (270, lambda stage_data_height_correction: stage_data_height_correction + 40)
    ],
    [
        (800, lambda stage_data_height_correction: stage_data_height_correction + 5)
    ],
    [
        (800, lambda stage_data_height_correction: stage_data_height_correction + 65)
    ],
    [
        (900, lambda stage_data_height_correction: stage_data_height_correction + 5)
    ],
    [
        (900, lambda stage_data_height_correction: stage_data_height_correction + 65)
    ]
]
