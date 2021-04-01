#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.stage.constants.stage_realms import StageRealms

STAGE_UNIT_REALM_POSITIONS = {
    StageRealms.DUNGEON: [
        (300, 480),
        (700, 370), (825, 450),
        (950, 370), (1075, 450)
    ],
    StageRealms.CASTLE: [
        (300, 480),
        (700, 420), (825, 480),
        (950, 420), (1075, 480)
    ],
    StageRealms.FOREST: [
        (300, 480),
        (650, 475), (775, 500),
        (900, 475), (1025, 500)
    ]
}
