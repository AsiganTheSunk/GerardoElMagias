#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.sound.sound_resource import SoundResource
from core.game.sound.constants.sound_type import SoundType
from core.game.sound.constants.sound_fx_sub_type import SoundFxSubType
from core.game.sound.constants.sound_file_extension import SoundFileExtension
from core.game.sound.constants.sound_music_sub_type import SoundMusicSubType


SOUND_POOL = {
    SoundType.FX: {
        SoundFxSubType.ATTACKS: [
            SoundResource('hit_cut', SoundFileExtension.WAV, 0.1),
            SoundResource('hit_cut_boss', SoundFileExtension.WAV, 0.1),
            SoundResource('block', SoundFileExtension.WAV, 0.1),
            SoundResource('miss', SoundFileExtension.WAV, 0.1),
            SoundResource('critical_hit', SoundFileExtension.WAV, 0.07),
            SoundResource('ultimate', SoundFileExtension.WAV, 0.1),
            SoundResource('ultimate_up', SoundFileExtension.WAV, 0.1)
        ],
        SoundFxSubType.SPELLS: [
            SoundResource('lightning_spell', SoundFileExtension.WAV, 0.1),
            SoundResource('firestorm_spell', SoundFileExtension.WAV, 0.1),
            SoundResource('heal_spell', SoundFileExtension.WAV, 0.1),
            SoundResource('earth_shock_spell', SoundFileExtension.WAV, 0.1),
        ],
        SoundFxSubType.ITEMS: [
            SoundResource('gold', SoundFileExtension.WAV, 0.15),
            SoundResource('health_potion', SoundFileExtension.WAV, 0.15),
            SoundResource('drink', SoundFileExtension.WAV, 0.15),
            SoundResource('eat', SoundFileExtension.WAV, 0.15),
            SoundResource('empty', SoundFileExtension.WAV, 0.15),
            SoundResource('error', SoundFileExtension.WAV, 0.12),
            SoundResource('drum_roll', SoundFileExtension.WAV, 0.1)
        ],
    },
    SoundType.MUSIC: {
        SoundMusicSubType.BACKGROUND: [
            SoundResource('boss', SoundFileExtension.MP3, 0.07),
            SoundResource('forest', SoundFileExtension.MP3, 0.07),
            SoundResource('victory', SoundFileExtension.MP3, 0.1),
            SoundResource('castle', SoundFileExtension.MP3, 0.1),
            SoundResource('dungeon', SoundFileExtension.MP3, 0.2),
        ]
    }
}


