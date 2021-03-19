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
from pygame import time, display, mouse, quit, init

init()

# Game Engine Constants Imports:
from constants.game_windows import screen_height, screen_width, panel_height
from constants.sound import boss_music, victory_music, battle_music, ultimate_sound, castle_music
import constants.globals

# Game Drawable Instance Imports:
from interface.composed_component.spell_book import open_spell_book
from interface.composed_component.player_interface_panel import StageDrawer

# Game Control Imports:
import constants.globals

# Master Game Engine Imports
from core.units.sound.sound_master import SoundMaster
from core.units.animations.animation_manager import AnimationMaster
from core.game.battle.battle_master import BattleMaster
from core.game.game_modes import GameModes
from game_attributes import GameAttributes

# Game Event Control Import:
from event_control import event_control
from core.text.damage_text import DamageText

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

run_reset = True
action_wait_time = 90

while constants.globals.run:
    if run_reset:
        battle_master.game_mode = GameModes.BATTLE
        constants.globals.action_cooldown = 0
        hero_player.ultimate_status = False
        hero_player.multi_attacks_left = 7
        run_reset = False

        if battle_master.level <= 7:
            if battle_master.is_boss_level():
                game_attributes.sound_mixer.fadeout(1)
                boss_music.play()
            else:
                if not game_attributes.sound_mixer.get_busy():
                    battle_music.play()

        elif battle_master.level > 7:
            if battle_master.is_boss_level():
                game_attributes.sound_mixer.fadeout(1)
                boss_music.play()
            else:
                if not game_attributes.sound_mixer.get_busy():
                   castle_music.play()

    stage_drawer.update(battle_master.level, battle_master.friendly_fighters[0], battle_master.enemy_fighters,
                        battle_master.is_boss_level(), game_attributes.text_sprite)

    if stage_drawer.display_kill_all():
        for target_unit in battle_master.enemy_fighters:
            target_unit.death()
            target_unit.death_animation()

    if stage_drawer.display_health_potion() and battle_master.current_fighter == battle_master.friendly_fighters[0]:
        if hero_player.stash.healing_potions > 0:
            hero_player.next_action = ['use', 'healing_potion']
        else:
            damage_text.warning(hero_player, 'No Healing Potions', game_attributes.text_sprite)

    if stage_drawer.display_mana_potion() and battle_master.current_fighter == battle_master.friendly_fighters[0]:
        if hero_player.stash.mana_potions > 0:
            hero_player.next_action = ['use', 'mana_potion']
        else:
            damage_text.warning(hero_player, 'No Mana Potions', game_attributes.text_sprite)

    if stage_drawer.display_spell_book() and battle_master.current_fighter == battle_master.friendly_fighters[0]:
        battle_master.game_mode = GameModes.SPELLBOOK
    if battle_master.game_mode == GameModes.SPELLBOOK:
        open_spell_book(hero_player, battle_master.enemy_fighters, game_attributes.surface,
                        game_attributes.text_sprite, battle_master)

    if hero_player.has_full_fury() and stage_drawer.display_ultimate():
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
            battle_master.run_fighter_action(game_attributes.text_sprite)

    # Check if all enemies are dead for win condition
    if battle_master.are_enemies_alive():
        battle_master.game_mode = GameModes.VICTORY

    # GameOver Check
    if battle_master.game_mode != GameModes.BATTLE:
        # Victory Check
        if battle_master.game_mode == GameModes.VICTORY:
            if battle_master.is_boss_level():
                boss_music.stop()
                if not game_attributes.sound_mixer.get_busy():
                    victory_music.play()
                stage_drawer.display_victory()

            if stage_drawer.display_next_button():
                if battle_master.is_boss_level():
                    victory_music.stop()
                run_reset = True
                battle_master.next_level()

            mouse.set_visible(True)
            pos = mouse.get_pos()

            for enemy_unit in battle_master.enemy_fighters:
                if enemy_unit.animation_set.rect.collidepoint(pos):
                    # hide mouse
                    mouse.set_visible(False)
                    # show icon
                    stage_drawer.display_bag_mouse(pos)
                    if constants.globals.clicked:
                        hero_player.loot(enemy_unit, game_attributes.text_sprite)
                        constants.globals.clicked = False

        if battle_master.game_mode == GameModes.DEFEAT:
            stage_drawer.display_defeat()

    constants.globals.action_cooldown += 1
    hero_player.next_action = None

    event_control()
    display.update()

quit()
