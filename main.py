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
from event_control import event_control

# InitGame Import:
from game_attributes import GameAttributes

from core.units.sound.sound_master import SoundMaster

sound_master = SoundMaster()

# Initializing InitGame & Stage Drawer
game_attributes = GameAttributes(time.Clock(), 60, screen_width, screen_height)
animation_master = AnimationMaster(game_attributes.surface)
stage_drawer = StageDrawer(game_attributes.surface, screen_width, screen_height, 0, panel_height,
                           game_attributes.clock, game_attributes.fps)

stage_drawer.display_caption()

# fst True es un filler que no se lee nunca
scripted_battle = [True, False, False, False, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, True]
hero_player = HeroPlayer(150, 580, "Hero", 1, 90, 30, 12, 9, 8, 2, 1, 1,
                         190, screen_height - panel_height + 20,
                         190, screen_height - panel_height + 40,
                         190, screen_height - panel_height + 40, animation_master)
enemy_list = []

runreset = True
action_wait_time = 90
level = 0
bosslevel = 1
total_fighters = 0


while constants.globals.run:
    while runreset:
        level += 1
        constants.globals.game_over = 0
        number_of_strikes = 0
        animation_cooldown = 0
        constants.globals.action_cooldown = 0
        constants.globals.current_fighter = 1
        constants.globals.ultimate_status = False 

        if scripted_battle[level]:
            game_attributes.sound_mixer.fadeout(1)
            enemy_list = scripted_enemy(bosslevel, animation_master)
            total_fighters = len(enemy_list) + 1
            bosslevel += 1
            boss_music.play()

        else:
            enemy_group = EnemyGroup(animation_master)
            enemy_list = enemy_group.generate_enemy(level, bosslevel)
            total_fighters = len(enemy_list) + 1
            if level <= 7:
                if not game_attributes.sound_mixer.get_busy():
                    battle_music.play()

            if level > 7:
                if not game_attributes.sound_mixer.get_busy():
                    castle_music.play()

        runreset = False
        constants.globals.runbattle = True

    while constants.globals.runbattle:
        # reset action variables
        attack = False
        mana_potion = False
        potion = False
        target = None
        loot = False

        stage_drawer.update(level, hero_player, enemy_list, scripted_battle, game_attributes.text_sprite)

        if stage_drawer.display_kill_all():
            for target_unit in enemy_list:
                target_unit.death()
                target_unit.death_animation()

        if stage_drawer.display_health_potion():
            potion = True
        if stage_drawer.display_mana_potion():
            mana_potion = True
        if stage_drawer.display_spell_book():
            constants.globals.game_over = 2

        if hero_player.current_fury == 100:
            if stage_drawer.display_ultimate() and constants.globals.current_fighter == 1 and constants.globals.action_cooldown >= action_wait_time:
                # Todo: activar animacion pre-ulti
                constants.globals.ultimate_status = True
                ultimate_sound.play()
                hero_player.reset_fury()
                constants.globals.action_cooldown = -25

        if constants.globals.game_over == 0:
            # make sure mouse is visible
            mouse.set_visible(True)
            pos = mouse.get_pos()
            for count, enemy_unit in enumerate(enemy_list):
                if enemy_unit.animation_set.rect.collidepoint(pos):
                    # hide mouse
                    mouse.set_visible(False)
                    # show icon
                    stage_drawer.display_sword_mouse(pos)
                    if constants.globals.clicked and enemy_unit.alive:
                        attack = True
                        target = enemy_list[count]

            # Player Actions
            if hero_player.alive:
                if constants.globals.current_fighter == 1:
                    constants.globals.action_cooldown += 1
                    if constants.globals.action_cooldown >= action_wait_time:
                        # Use: Melee Attack
                        if attack and target is not None:
                            hero_player.attack(target, game_attributes.text_sprite)

                        # Use: Healing Potion
                        if potion:
                            hero_player.use_healing_potion(game_attributes.text_sprite)

                        # Use: Mana Potion
                        if mana_potion:
                            hero_player.use_mana_potion(game_attributes.text_sprite)

                        # Use: Ultimate Spell
                        # Todo: Convert Use talking action_cooldown, current_fighter and action_wait_time into account
                        if constants.globals.ultimate_status:
                            hero_player.use_ultimate(enemy_list, game_attributes.text_sprite)
            else:
                constants.globals.game_over = -1

            # Enemy action
            for count, enemy_unit in enumerate(enemy_list):
                if constants.globals.current_fighter == 2 + count:
                    if enemy_unit.alive:
                        constants.globals.action_cooldown += 1
                        if constants.globals.action_cooldown >= action_wait_time:
                            enemy_unit.action(hero_player, game_attributes.text_sprite)
                    else:
                        constants.globals.current_fighter += 1

            # Reset Turn
            if constants.globals.current_fighter > total_fighters:
                constants.globals.current_fighter = 1

        # Check if all enemies are dead for win condition
        alive_enemies = 0
        for enemy_unit in enemy_list:
            if enemy_unit.alive:
                alive_enemies += 1
        if alive_enemies == 0:
            constants.globals.game_over = 1

        # Gameover Check
        if constants.globals.game_over != 0:

            # Condicion de Victoria
            if constants.globals.game_over == 1:
                if scripted_battle[level]:
                    boss_music.stop()
                    if not game_attributes.sound_mixer.get_busy():
                        victory_music.play()
                    stage_drawer.display_victory()

                    if stage_drawer.display_next_button():
                        constants.globals.game_over = 0
                        runreset = True
                        constants.globals.runbattle = False
                        victory_music.stop()
                else:
                    stage_drawer.display_victory_message()
                    if stage_drawer.display_next_button():
                        runreset = True
                        constants.globals.runbattle = False

                # LOOT PHASE
                mouse.set_visible(True)
                pos = mouse.get_pos()
                for count, enemy_unit in enumerate(enemy_list):
                    # if sprite.spritecollide(enemy_unit.animation_set.image,
                    #                         stage_drawer.sword_pointer.mouse_pointer_image, False, sprite.collide_mask):
                    if enemy_unit.animation_set.rect.collidepoint(pos):
                        # hide mouse
                        mouse.set_visible(False)
                        # show icon
                        stage_drawer.display_bag_mouse(pos)
                        if constants.globals.clicked:
                            target = enemy_list[count]

                            # Todo: Create a proper function
                            hero_player.loot(target, game_attributes.text_sprite)
                            constants.globals.clicked = False

            if constants.globals.game_over == -1:
                stage_drawer.display_defeat()

            if constants.globals.game_over == 2:
                open_spell_book(hero_player, enemy_list, game_attributes.surface, game_attributes.text_sprite)

        event_control()
        display.update()

quit()
