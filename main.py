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
from pygame import time, display, sprite, mouse, quit, init
init()

# Game Engine Imports:
from core.units.classes.player import HeroPlayer
from core.units.enemy_group import EnemyGroup

# Game Engine Constants Imports:
from constants.sound import boss_music, victory_music, battle_music, ultimate_sound, castle_music
from constants.game_windows import screen_height, screen_width, panel_height
from core.game.battle.scripted_enemies import scripted_enemy
from core.units.animations.animation_manager import AnimationMaster


# Game Drawable Instance Imports:
from interface.composed_component.spell_book import open_spell_book
from interface.composed_component.player_interface_panel import StageDrawer

# Game Control Imports:
import constants.globals

from core.units.sound.sound_master import SoundMaster
from core.units.animations.animation_manager import AnimationMaster

# Game Engine Imports:
from interface.basic_components import button
from core.game.battle.battle_master import BattleMaster
from core.game.game_modes import GameModes

# Game Engine Constants Imports
from constants.basic_colors import *
from constants.game_windows import *
from constants.basic_images import *
from constants.basic_fonts import *

# Python Imports:
from constants.sound import *
import constants.globals

from event_control import event_control

from interface.composed_component.spellbook import open_spellbook

sound_master = SoundMaster()

# Initializing InitGame & Stage Drawer
game_attributes = GameAttributes(time.Clock(), 60, screen_width, screen_height)
animation_master = AnimationMaster(game_attributes.surface)
stage_drawer = StageDrawer(game_attributes.surface, screen_width, screen_height, 0, panel_height,
                           game_attributes.clock, game_attributes.fps)

stage_drawer.display_caption()
battle_master = BattleMaster()
damage_text_group = sprite.Group()
hero_player = battle_master.get_hero()

runreset = True
action_wait_time = 90

while constants.globals.run:
    if runreset:
        battle_master.game_mode = GameModes.BATTLE
        constants.globals.action_cooldown = 0
        runreset = False
        constants.globals.number_of_strikes = 0

        # reset action variables
    loot = False
    stage_drawer.update(battle_master.level, battle_master.friendly_fighters, battle_master.enemy_fighters, battle_master.is_boss_level(battle_master.level), game_attributes.text_sprite)

    if stage_drawer.display_kill_all():
        for target_unit in battle_master.enemy_fighters:
            target_unit.death()
            target_unit.death_animation()

    if stage_drawer.display_health_potion():
        hero_player.next_action = ['use', 'healing_potion']
    if stage_drawer.display_mana_potion():
        hero_player.next_action = ['use', 'mana_potion']
    if stage_drawer.display_spell_book():
        constants.globals.game_over = 2
    if battle_master.game_mode == GameModes.SPELLBOOK:
        open_spell_book(hero_player, battle_master.enemy_fighters, game_attributes.surface, game_attributes.text_sprite)

    if hero_player.current_fury == 100 and stage_drawer.display_ultimate():
        if battle_master.current_fighter == hero_player and constants.globals.action_cooldown >= action_wait_time:
            # Todo: activar animacion pre-ulti
            hero_player.ultimate_status = True
            ultimate_sound.play()
            hero_player.reset_fury()
            constants.globals.action_cooldown = -25

    if battle_master.game_mode == GameModes.BATTLE:
        # make sure mouse is visible
        mouse.set_visible(True)
        pos = mouse.get_pos()
        for enemy_unit in battle_master.enemy_fighters:
            if enemy_unit.animation_set.rect.collidepoint(pos):
                # hide mouse
                mouse.set_visible(False)
                # show icon
                stage_drawer.display_sword_mouse(pos)
                if constants.globals.clicked and enemy_unit.alive:
                    hero_player.next_action = ('attack', enemy_unit)

        if constants.globals.action_cooldown >= action_wait_time:
            battle_master.run_fighter_action(damage_text_group)
            # Check if all enemies are dead for win condition

    alive_enemies = len(battle_master.get_alive_enemies())
    if alive_enemies == 0:
        battle_master.game_mode = GameModes.VICTORY

        # Gameover Check
    if battle_master.game_mode != GameModes.BATTLE:

        # Condicion de Victoria
        if battle_master.game_mode == GameModes.VICTORY:
            if battle_master.is_boss_level(battle_master.level):
                boss_music.stop()
                if not game_attributes.sound_mixer.get_busy():
                    victory_music.play()
                stage_drawer.display_victory()

            if stage_drawer.display_next_button():
                if battle_master.is_boss_level(battle_master.level):
                    victory_music.stop()
                runreset = True
                battle_master.next_level()

                # LOOT PHASE
            mouse.set_visible(True)
            pos = mouse.get_pos()

            for enemy_unit in battle_master.enemy_fighters:
                if enemy_unit.animation_set.rect.collidepoint(pos):
                    # hide mouse
                    mouse.set_visible(False)
                    # show icon
                    stage_drawer.display_bag_mouse(pos)
                    if constants.globals.clicked:

                        # Todo: Create a proper function
                        if battle_master.is_boss_level(battle_master.level):
                            hero_player.loot_boss(enemy_unit, damage_text_group)
                        else:
                            hero_player.loot(enemy_unit, damage_text_group)
                        constants.globals.clicked = False

        if battle_master.game_mode == GameModes.DEFEAT:
            stage_drawer.display_defeat()

    constants.globals.action_cooldown += 2
    hero_player.next_action = None

    event_control()

    display.update()

quit()
