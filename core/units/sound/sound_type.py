from enum import Enum


class SoundFileExtension(Enum):
    MP3 = 'mp3'
    WAV = 'wav'


class SoundType(Enum):
    FX = 'Fx'
    MUSIC = 'Music'


class SoundMusicSubType(Enum):
    BACKGROUND = 'Background'
    # MENU = 'Menu'


class SoundFxSubType(Enum):
    ATTACKS = 'Attacks'
    ITEMS = 'Items'
    SPELLS = 'Spells'
