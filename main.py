#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Father Karras and AsiganTheSunk"
__copyright__ = "Copyright 2021, Gerardo El Magias"

__credits__ = ["Father Karras", "AsiganTheSunk"]
__version__ = "0.1a"
__maintainer__ = "Father Karras and AsiganTheSunk"
__email__ = ""
__status__ = "Development"

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Pygame Imports:
from pygame import time, display, quit, init

init()

# Game Engine Constants Imports:
from constants.game_windows import screen_height, screen_width, panel_height
import constants.globals

# Game Drawable Instance Imports:
from interface.composed_component.player_interface_panel import StageDrawer

# Game Control Imports:
import constants.globals

# Master Game Engine Imports
from core.units.sound.sound_master import SoundMaster
from core.units.animations.animation_manager import AnimationMaster
from core.game.battle.battle_master import BattleMaster
from game_attributes import GameAttributes

# Game Event Control Import:
from event_control import event_control
from core.text.damage_text import DamageText
from main_stages import reset, kill_switch, resolve_defeat, resolve_victory, resolve_combat, \
    resolve_player_loot, resolve_player_interface_actions, resolve_player_attack, update_victory_status

# Initializing InitGame & Stage Drawer
damage_text = DamageText()
game_attributes = GameAttributes(time.Clock(), 60, screen_width, screen_height)
animation_master = AnimationMaster(game_attributes.surface)
sound_master = SoundMaster()
stage_drawer = StageDrawer(game_attributes.surface, screen_width, screen_height, 0, panel_height,
                           game_attributes.clock, game_attributes.fps)

stage_drawer.display_caption()
battle_master = BattleMaster(animation_master)
hero_player = battle_master.get_hero()
current_stage = None
run_reset = True
action_wait_time = 90
previous_mouse_collision = False


while constants.globals.run:
    # Music
    sound_master.stage_selector_sound.select_sound(battle_master.level)
    sound_master.background_play(battle_master.game_mode)

    run_reset = reset(run_reset, hero_player)

    stage_drawer.update(battle_master.level, battle_master.friendly_fighters[0], battle_master.enemy_fighters,
                        battle_master.is_boss_level(), game_attributes.text_sprite)

    # Display KillSwitch
    kill_switch(battle_master, stage_drawer)

    # Resolve Sword Display and Loot Display and Resolution
    previous_mouse_collision = \
        resolve_player_loot(hero_player, battle_master, stage_drawer, game_attributes, previous_mouse_collision)
    previous_mouse_collision = \
        resolve_player_attack(hero_player, battle_master, stage_drawer, previous_mouse_collision)

    # Resolve Click Attack
    resolve_player_interface_actions(hero_player, battle_master, stage_drawer, game_attributes, action_wait_time)
    # Resolve Enemy or Player Combat
    resolve_combat(battle_master, action_wait_time, game_attributes)

    update_victory_status(battle_master)
    run_reset = resolve_victory(run_reset, battle_master, stage_drawer)
    resolve_defeat(battle_master, stage_drawer)

    constants.globals.action_cooldown += 1
    hero_player.next_action = None
    event_control()
    display.update()

quit()
