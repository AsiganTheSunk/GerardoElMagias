#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mixer
from core.units.sound.sound_db import SOUND_POOL
from core.game.game_modes import GameModes


class ClassSound:
    def __init__(self, class_name, sounds):
        self.class_name = class_name
        self.sounds = sounds

        self.attack_sound = sounds['fx']['attacks']['hit_cut']
        self.critical_attack_sound = sounds['fx']['attacks']['critical_hit_cut']
        self.hurt_sound = None
        self.block_sound = sounds['fx']['attacks']['miss']
        self.miss_sound = sounds['fx']['attacks']['miss']


class ConsumableSounds:
    def __init__(self, sounds):
        self.consume_health_potion = sounds['fx']['items']['health_potion']
        self.consume_mana_potion = sounds['fx']['items']['health_potion']
        self.consume_drink = sounds['fx']['items']['drink']
        self.consume_food = sounds['fx']['items']['eat']


class MenuSounds:
    def __init__(self, sounds):
        self.advance_click_sound = None
        self.return_click_sound = None
        self.navigate_menu_sound = None


class CommonStageSounds:
    def __init__(self, sounds):
        self.gold_loot_sound = sounds['fx']['items']['gold']
        self.error_loot_sound = sounds['fx']['items']['error']
        self.roll_loot_sound = sounds['fx']['items']['drum_roll']

        self.empty_loot_sound = sounds['fx']['items']['empty']
        self.victory_sound = sounds['music']['background']['victory']
        # self.defeat_sound = sounds['music']['background']['defeat']


class StageSounds(CommonStageSounds, ConsumableSounds, MenuSounds):
    def __init__(self, stage_name, sounds):
        self.stage_name = stage_name
        CommonStageSounds.__init__(self, sounds)
        ConsumableSounds.__init__(self, sounds)
        MenuSounds.__init__(self, sounds)

        self.background_boss_sound = sounds['music']['background']['boss']
        self.background_sound = sounds['music']['background'][stage_name.lower()]


class StageSoundSelector:
    def __init__(self, sounds):
        self.list_of_stages = {
            'forest': StageSounds('forest', sounds),
            'castle': StageSounds('castle', sounds)
        }
        self.current_stage = None

    def select_sound(self, level):
        if level <= 7:
            self.set_stage_sounds('forest')
        elif level > 7:
            self.set_stage_sounds('castle')

    def set_stage_sounds(self, stage_name):
        self.current_stage = self.list_of_stages[stage_name]

    def get_stage_sounds(self):
        return self.current_stage


class SoundMaster:
    def __init__(self):
        self.muted = True
        self.sound_mixer = mixer
        self.sound_mixer.init()
        self.sound_mixer.pre_init(44100, -16, 2, 4096)

        sound_loader = SoundLoader(self.sound_mixer)
        self.sounds = sound_loader.sounds
        self.sound_effects = SoundEffects()
        self.stage_sound_selector = StageSoundSelector(self.sounds)

        self.current_playing_sound = None
        self.previous_game_mode = None

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
                if self.sound_mixer.get_busy():
                    self.sound_mixer.fadeout(1)
                    self.current_playing_sound.stop()

    def update_play_sound(self, current_sound):
        if self.muted:
            pass
        if not self.sound_mixer.get_busy():
            self.current_playing_sound = current_sound
            current_sound.play()

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
        # self.defeat_sound_play(game_mode)

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
            # self.stop_previous_sound()
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


class SoundEffects:
    def stop(self, sound):
        pass

    def play(self, sound):
        pass

    def fadeout(self, sound):
        pass

    def fadein(self, sound):
        pass


class SoundLoader:
    def __init__(self, sound_mixer):
        self.sound_mixer = sound_mixer
        self.sounds = dict()
        self.load_sound_sets()

    def load_sound_sets(self):
        print('[ Loading Sound Resources ]:')
        print('-------' * 10)
        sound_type = dict()
        # For Each AnimationSet present in AnimationSets: Environment, Skills, Units
        for sound_resource_type in SOUND_POOL:
            # Load Each Animation Resource present in the Animation to be displayed
            # print('Sound_Type:', sound_resource_type.value)
            sound_subtype = dict()
            for index, sound_set in enumerate(SOUND_POOL[sound_resource_type]):
                # print('Sound_SubType:',sound_set.value)
                sound_resource = dict()
                for sound in SOUND_POOL[sound_resource_type][sound_set]:
                    sound_resource[sound.sound_name] = self.load_resource(sound_resource_type.value,
                                                                          sound_set.value, sound.sound_name,
                                                                          sound.file_extension, sound.volume)
                sound_subtype[sound_set.value.lower()] = sound_resource
            sound_type[sound_resource_type.value.lower()] = sound_subtype
        print('\n', 'Done.')
        self.sounds = sound_type
        import pprint

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.sounds)

    def load_resource(self, resource_type, sound_set, sound_name, sound_file_extension, sound_volume):
        # print(f"> resources/sound/{resource_type.lower()}/{sound_set.lower()}/
        # {sound_name.lower()}.{sound_file_extension.value}")
        sound_resource = self.sound_mixer.Sound(
            f"resources/sound/{resource_type.lower()}/{sound_set.lower()}/"
            f"{sound_name.lower()}.{sound_file_extension.value}")
        sound_resource.set_volume(sound_volume)
        return sound_resource



