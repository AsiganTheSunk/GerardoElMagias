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

from pygame import time, display, sprite, event, QUIT, MOUSEBUTTONDOWN, mouse, quit

# Game Engine Imports:
from interface.basic_component import button
from core.units.classes.player import HeroPlayer
from core.units.enemy_group import EnemyGroup

# Game Engine Constants Imports
from constants.basic_colors import *
from constants.game_windows import *
from constants.basic_images import *
from constants.basic_fonts import *
from core.game.battle.scripted_enemies import scripted_enemy

# Python Imports:
from random import randint
from constants.sound import *
import constants.globals

from event_control import Event_Control

init()
mixer.pre_init(44100, -16, 2, 4096)
clock = time.Clock()
fps = 60

screen = display.set_mode((screen_width, screen_height))
display.set_caption("Las trepidantes aventuras de Gerardo EL MAGIAS")

# define game variables
action_wait_time = 90
game_over = 0
level = 17
bosslevel = 1
update_time = time.get_ticks()


def setup_battle(target_list, hero_player):
    clock.tick(fps)

    # draw backgrounds
    draw_bg_forest()

    # draw panel
    draw_stage()
    draw_panel()

    # damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # draw fighters
    hero_player.unit_animation.update()
    hero_player.draw(screen)
    hero_player.health_bar.draw(hero_player.current_hp, hero_player.max_hp, screen)
    hero_player.mana_bar.draw(hero_player.current_mp, hero_player.max_mp, screen)
    hero_player.fury_bar.draw(hero_player.current_fury, hero_player.max_fury, screen)

    for target_unit in target_list:
        target_unit.update()
        target_unit.draw(screen)
        target_unit.health_bar.draw(target_unit.current_hp, target_unit.max_hp, screen)


# create function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# functions for drawing backgrounds
def draw_bg_forest():
    screen.blit(background_forest, (0, 0))


def draw_bg_castle():
    screen.blit(background_castle, (0, 0))


def draw_stage():
    draw_text(f"Oro: {hero_player.stash.gold}", default_font, YELLOW_COLOR, 50, 20)
    draw_text(f"LVL: {hero_player.level}", default_font, WHITE_COLOR, 50, 100)
    draw_text(f"Exp: {hero_player.experience} / {hero_player.exp_level_break} ", default_font, WHITE_COLOR, 50, 125)
    draw_text(f"STR: {hero_player.strength}", default_font, WHITE_COLOR, 50, 175)
    draw_text(f"DEX: {hero_player.dexterity}", default_font, WHITE_COLOR, 50, 200)
    draw_text(f"MAG: {hero_player.magic}", default_font, WHITE_COLOR, 50, 225)
    if level <= 7:
        draw_text(f"THE WOODS: STAGE {level}", default_font, RED_COLOR, 310, 25)
    else:
        draw_text(f"THE CASTLE: STAGE {level - 7}", default_font, RED_COLOR, 310, 25)


def draw_debug_panel(_current_fighter, _total_fighters):
    draw_text(f"Total fighters: {_total_fighters}", default_font, YELLOW_COLOR, 600, 100)
    draw_text(f"Current fighter: {_current_fighter}", default_font, YELLOW_COLOR, 600, 125)


# function for drawing panel
def draw_panel():
    # draw FF panel
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    # show hero stats
    draw_text(f"  HP: {hero_player.current_hp} / {hero_player.max_hp}      "
              f"MP: {hero_player.current_mp} / {hero_player.max_mp}",
              default_font, WHITE_COLOR, 99, screen_height - bottom_panel + 10)

    # show number of pots
    draw_text(f"{hero_player.stash.healing_potions}", default_font, WHITE_COLOR, 100, screen_height - bottom_panel + 85)
    # show number of lightnings
    draw_text(f"{hero_player.stash.mana_potions}", default_font, WHITE_COLOR, 210, screen_height - bottom_panel + 85)

    # draw name and health of enemies
    ENEMY_TEXT_POS_0 = [480, screen_height - bottom_panel + 5]
    ENEMY_TEXT_POS_1 = [480, screen_height - bottom_panel + 65]
    ENEMY_TEXT_POS_2 = [700, screen_height - bottom_panel + 5]
    ENEMY_TEXT_POS_3 = [700, screen_height - bottom_panel + 65]

    tmp = [ENEMY_TEXT_POS_0, ENEMY_TEXT_POS_1, ENEMY_TEXT_POS_2, ENEMY_TEXT_POS_3]

    if scripted_battle[level]:
        draw_text(f" The Boss HP: {enemy_list[0].current_hp}", default_font, WHITE_COLOR, tmp[0][0], tmp[0][1])
    else:
        for index, enemy_fighter in enumerate(enemy_list):
            draw_text(f"Bandit {index + 1} HP: {enemy_fighter.current_hp}", default_font, WHITE_COLOR, tmp[index][0],
                      tmp[index][1])


# Item Buttons:
potion_button = button.Button(screen, 110, screen_height - bottom_panel + 75, health_potion_img, 64, 64)
mana_potion_button = button.Button(screen, 220, screen_height - bottom_panel + 75, mana_potion_img, 60, 60)
spellbook_button = button.Button(screen, 0, 695, spellbook_img, 100, 100)

lightning_spell_button = button.Button(screen, 150, 220, lightning_img, 150, 150)
firestorm_spell_button = button.Button(screen, 165, 410, firestorm_img, 110, 110)
heal_spell_button = button.Button(screen, 500, 220, heal_img, 130, 130)

# Control Buttons:
restart_button = button.Button(screen, 400, 120, restart_img, 100, 100)
next_button = button.Button(screen, 800, 10, next_img, 80, 80)

# Ultimate Button
ultimate_button = button.Button(screen, 400, 400, ultimate_img, 50, 50)

# Kill Button
kill_button = button.Button(screen, 40, 260, skull_image, 60, 60)


def draw_bgintro():
    screen.blit(background_intro, (0, 0))


def setup_shop():
    damage_text_group.update()
    damage_text_group.draw(screen)
    clock.tick(fps)
    draw_text("Magias y embrujos", default_font, WHITE_COLOR, 360, 140)
    screen.blit(shop_image, (120, 190))


def setup_battle(target_list, hero_player):
    clock.tick(fps)

    # draw backgrounds
    if level <=7:
        draw_bg_forest()
    if level > 7:
        draw_bg_castle()

    # draw panel
    draw_stage()
    draw_panel()

    # damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # draw fighters
    hero_player.animation_set.update()
    hero_player.animation_set.draw(screen)
    hero_player.health_bar.draw(hero_player.current_hp, hero_player.max_hp, screen)
    hero_player.mana_bar.draw(hero_player.current_mp, hero_player.max_mp, screen)
    hero_player.fury_bar.draw(hero_player.current_fury, hero_player.max_fury, screen)

    for target_unit in target_list:
        target_unit.animation_set.update()
        target_unit.animation_set.draw(screen)
        target_unit.health_bar.draw(target_unit.current_hp, target_unit.max_hp, screen)


# el primer True es un filler que no se lee nunca
scripted_battle = [True, False, False, False, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, True]

damage_text_group = sprite.Group()
hero_player = HeroPlayer(150, 580, "Hero", 1, 90, 30, 12, 9, 8, 2, 1, 1, 115, screen_height - bottom_panel + 50, 290, screen_height - bottom_panel + 50, 90, 510)
enemy_list = []

runreset = True
runshop = False

total_fighters = 0

while constants.globals.run:
    while runreset:
        level += 1
        game_over = 0
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
            if level <= 7:
                enemy_group = EnemyGroup()
                enemy_list = enemy_group.generate_enemy(level)
                total_fighters = len(enemy_list) + 1
                if not mixer.get_busy():
                    battle_music.play()

            if level > 7:
                enemy_group = EnemyGroup()
                enemy_list = enemy_group.generate_enemy(level)
                total_fighters = len(enemy_list) + 1
                if not mixer.get_busy():
                    castle_music.play()

        runreset = False
        constants.globals.runbattle = True



    while runshop:
        setup_shop()
        if next_button.draw():
            runshop = False
            constants.globals.runbattle = True

        if lightning_spell_button.draw():
            if hero_player.use_lightning(enemy_list, damage_text_group):
                lightning_spell_1_sound.play()
                runshop = False
                constants.globals.runbattle = True

        if firestorm_spell_button.draw():
            if hero_player.use_firestorm(enemy_list, damage_text_group):
                i = randint(0, 1)
                if i == 0:
                    firestorm_spell_1_sound.play()
                if i == 1:
                    firestorm_spell_2_sound.play()
                runshop = False
                constants.globals.runbattle = True

        if heal_spell_button.draw():
            if hero_player.use_heal(damage_text_group):
                heal_spell_1_sound.play()
                runshop = False
                constants.globals.runbattle = True

        for _event in event.get():
            if _event.type == QUIT:
               constants.globals.run = False
               runshop = False

        display.update()

    while constants.globals.runbattle:
        # reset action variables
        attack = False
        mana_potion = False
        potion = False
        target = None
        loot = False

        setup_battle(enemy_list, hero_player)
        # draw_debug_panel(current_fighter, total_fighters)

        if kill_button.draw():
            for target_unit in enemy_list:
                target_unit.death()
                target_unit.death_animation()

        if potion_button.draw():
            potion = True
        if mana_potion_button.draw():
            mana_potion = True
        if spellbook_button.draw():
            runshop = True
            constants.globals.runbattle = False

        if hero_player.current_fury == 100:
            if ultimate_button.draw() and constants.globals.current_fighter == 1 and constants.globals.action_cooldown >= action_wait_time:
                #TODO activar animacion pre-ulti
                constants.globals.ultimate_status = True
                ultimate_sound.play()
                hero_player.reset_fury()
                constants.globals.action_cooldown = -25

        if game_over == 0:
            # make sure mouse is visible
            mouse.set_visible(True)
            pos = mouse.get_pos()
            for count, enemy_unit in enumerate(enemy_list):
                if enemy_unit.animation_set.rect.collidepoint(pos):
                    # hide mouse
                    mouse.set_visible(False)
                    # show icon
                    screen.blit(sword_img, pos)
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
                game_over = -1

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
            game_over = 1

        # Gameover Check
        if game_over != 0:
            # Condicion de Victoria
            if game_over == 1:
                if scripted_battle[level]:
                    boss_music.stop()
                    if not mixer.get_busy():
                        victory_music.play()
                    screen.blit(victory_img, (180, 50))
                    draw_text(f" Next Battle ", default_font, RED_COLOR, 630, 30)

                    if next_button.draw():
                        game_over = 0
                        runreset = True
                        constants.globals.runbattle = False
                        victory_music.stop()
                else:
                    draw_text(f" STAGE CLEARED ", default_font, RED_COLOR, 330, 250)
                    draw_text(f" GET YOUR LOOT! ", default_font, RED_COLOR, 330, 300)
                    draw_text(f" Next Battle ", default_font, RED_COLOR, 630, 30)

                    if next_button.draw():
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
                        screen.blit(loot_img, pos)
                        if constants.globals.clicked:
                            target = enemy_list[count]

                            # Todo: Create a proper function
                            if scripted_battle[level]:
                                hero_player.loot_boss(target, damage_text_group)
                            else:
                                hero_player.loot(target, damage_text_group)
                            constants.globals.clicked = False

            if game_over == -1:
                screen.blit(defeat_img,(180, 50))
                draw_text(f" YOU ARE A NOOB ", default_font, RED_COLOR, 340, 350)

        Event_Control()

        display.update()

quit()
