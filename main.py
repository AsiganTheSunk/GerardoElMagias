#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Father Karras and AsiganTheSunk"
__copyright__ = "Copyright 2021, Gerardo El Magias"

__credits__ = ["Father Karras", "AsiganTheSunk"]
__version__ = "0.1a"
__maintainer__ = "Father Karras and AsiganTheSunk"
__email__ = ""
__status__ = "Development"

# Pygame Imports:
from pygame import time, display, sprite, mouse, quit, init
init()
# Game Engine Imports:
from interface.basic_components import button
from core.units.classes.player import HeroPlayer
from core.units.enemy_group import EnemyGroup

# Game Engine Constants Imports
from constants.basic_colors import *
from constants.game_windows import *
from constants.basic_images import *
from constants.basic_fonts import *
from core.game.battle.scripted_enemies import scripted_enemy

# Python Imports:
from constants.sound import *
import constants.globals
from event_control import event_control
from interface.composed_component.spellbook import open_spellbook
from interface.composed_component.player_interface_panel import StageDrawer


mixer.pre_init(44100, -16, 2, 4096)
clock = time.Clock()
fps = 60

screen = display.set_mode((screen_width, screen_height))
display.set_caption("Las trepidantes aventuras de Gerardo EL MAGIAS")

update_time = time.get_ticks()

# Stage Drawer
stage_drawer = StageDrawer(screen, screen_width, screen_height, 0, panel_height, clock, fps)

# fst True es un filler que no se lee nunca
scripted_battle = [True, False, False, False, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, True]

damage_text_group = sprite.Group()
hero_player = HeroPlayer(150, 580, "Hero", 1, 90, 30, 12, 9, 8, 2, 1, 1, 115, screen_height - panel_height + 50, 290, screen_height - panel_height + 50, 90, 510)
enemy_list = []

runreset = True
action_wait_time = 90
level = 0
bosslevel = 1


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
            mixer.fadeout(1)
            enemy_list = scripted_enemy(bosslevel)
            total_fighters = len(enemy_list) + 1
            bosslevel += 1
            boss_music.play()

        else:
            enemy_group = EnemyGroup()
            enemy_list = enemy_group.generate_enemy(level, bosslevel)
            total_fighters = len(enemy_list) + 1
            if level <= 7:
                if not mixer.get_busy():
                    battle_music.play()

            if level > 7:
                if not mixer.get_busy():
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

        stage_drawer.update(level, hero_player, enemy_list, scripted_battle, damage_text_group)

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
                    screen.blit(sword_image, pos)
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
                            hero_player.attack(target, damage_text_group)

                        # Use: Healing Potion
                        if potion:
                            hero_player.use_healing_potion(damage_text_group)

                        # Use: Mana Potion
                        if mana_potion:
                            hero_player.use_mana_potion(damage_text_group)

                        # Use: Ultimate Spell
                        # Todo: Convert Use talking action_cooldown, current_fighter and action_wait_time into account
                        if constants.globals.ultimate_status:
                            hero_player.use_ultimate(enemy_list, damage_text_group)
            else:
                constants.globals.game_over = -1

            # Enemy action
            for count, enemy_unit in enumerate(enemy_list):
                if constants.globals.current_fighter == 2 + count:
                    if enemy_unit.alive:
                        constants.globals.action_cooldown += 1
                        if constants.globals.action_cooldown >= action_wait_time:
                            enemy_unit.action(hero_player, damage_text_group)
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
                    if not mixer.get_busy():
                        victory_music.play()
                    screen.blit(victory_banner_image, (180, 50))
                    stage_drawer.display_next_battle_message()

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
                    if enemy_unit.animation_set.rect.collidepoint(pos):
                        # hide mouse
                        mouse.set_visible(False)
                        # show icon
                        screen.blit(loot_image, pos)
                        if constants.globals.clicked:
                            target = enemy_list[count]

                            # Todo: Create a proper function
                            if scripted_battle[level]:
                                hero_player.loot_boss(target, damage_text_group)
                            else:
                                hero_player.loot(target, damage_text_group)
                            constants.globals.clicked = False

            if constants.globals.game_over == -1:
                screen.blit(defeat_banner_image, (180, 50))
                stage_drawer.display_defeat_message()

            if constants.globals.game_over == 2:
                open_spellbook(hero_player, enemy_list, screen, damage_text_group)


        event_control()

        display.update()

quit()
