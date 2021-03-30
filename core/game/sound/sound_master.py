#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mixer
from core.game.constants.game_modes import GameModes
from core.game.stage.stage_sound_selector import StageSoundSelector
from core.game.sound.sound_loader import SoundLoader
from core.game.sound.sound_effects import SoundEffects


class SoundMaster:
    def __init__(self):
        self.muted = True
        self.sound_mixer = mixer
        self.sound_mixer_music = mixer.music
        self.sound_mixer_music.set_volume(0.1)
        self.sound_mixer.pre_init(44100, -16, 2, 4096)

        sound_loader = SoundLoader(self.sound_mixer)
        self.sounds = sound_loader.sounds
        self.sound_effects = SoundEffects()
        self.stage_sound_selector = StageSoundSelector(self.sounds)

        self.current_music_playing = None
        self.previous_game_mode = None

    def play_unit_fx_sound(self, unit_fx_sound):
        self.sounds['fx']['attacks'][unit_fx_sound].play()

    def play_item_fx_sound(self, item_fx_sound):
        self.sounds['fx']['items'][item_fx_sound].play()
        
    def play_spell_fx_sound(self, spell_fx_sound):
        self.sounds['fx']['spells'][spell_fx_sound].play()

    def set_stage_sounds(self, stage_name):
        self.stage_sound_selector.set_stage_sounds(stage_name)

    def get_stage_sounds(self):
        return self.stage_sound_selector.current_stage

    def stop_previous_sound(self, game_mode):
        if self.previous_game_mode is None:
            self.previous_game_mode = game_mode
        else:
            if game_mode is not self.previous_game_mode:
                self.previous_game_mode = game_mode
                if self.sound_mixer_music.get_busy():
                    self.sound_mixer_music.fadeout(1)

    def update_play_sound(self, current_music):
        if self.muted:
            pass
        if not self.sound_mixer_music.get_busy():
            self.current_music_playing = current_music
            self.sound_mixer_music.load(current_music.get_sound_path())
            self.sound_mixer_music.play()

    def background_play(self, game_mode):
        # Background Sound Procedure
        self.background_sound_play(game_mode)

        # Background Boss Sound
        self.boss_sound_play(game_mode)
        # Menu Interactions:

        # Sound Effects

        # Mouse Interactions:

        # Victory Defeat Sound Procedures
        self.victory_sound_play(game_mode)

    def background_sound_play(self, game_mode):
        background_stage_sound = self.stage_sound_selector.current_stage.background_sound
        if game_mode is GameModes.BATTLE:
            self.stop_previous_sound(game_mode)
            self.update_play_sound(background_stage_sound)

    def victory_sound_play(self, game_mode):
        victory_sound = self.stage_sound_selector.current_stage.victory_sound
        if game_mode is GameModes.VICTORY:
            self.stop_previous_sound(game_mode)
            self.update_play_sound(victory_sound)

    def defeat_sound_play(self, game_mode):
        defeat_sound = self.stage_sound_selector.current_stage.defeat_sound
        if game_mode is GameModes.DEFEAT:
            self.update_play_sound(defeat_sound)

    def boss_sound_play(self, game_mode):
        background_boss_music = self.stage_sound_selector.current_stage.background_boss_sound
        if game_mode is GameModes.BOSS_BATTLE:
            self.stop_previous_sound(game_mode)
            self.update_play_sound(background_boss_music)

    def loot_click(self, mouse_collision):
        if mouse_collision:
            pass

    def stop_all_sounds(self):
        pass
