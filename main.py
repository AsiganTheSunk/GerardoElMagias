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
from pygame import time, display, sprite, event, QUIT, MOUSEBUTTONDOWN, mouse, quit, init

# Game Engine Imports:
from interface.basic_components import button
from units.unit_type.hero.player import HeroPlayer
from units.unit_type.bandit.bandit_melee_figher import Bandit
from units.enemy_group import EnemyGroup

# Game Engine Constants Imports
from constants.basic_colors import *
from constants.game_windows import *
from constants.basic_images import *
from constants.basic_fonts import *

# Python Imports:
from random import randint


init()
clock = time.Clock()
fps = 60

screen = display.set_mode((screen_width, screen_height))
display.set_caption("Las trepidantes aventuras de Gerardo EL MAGIAS")

# define game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
animation_cooldown = 0
action_wait_time = 80
clicked = False
game_over = 0
level = 1
update_time = time.get_ticks()




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
    draw_text(f"THE WOODS: STAGE {level}", default_font, RED_COLOR, 310, 25)
    draw_text(f"Exp: {hero_player.experience} / {hero_player.exp_level_break} ", default_font, WHITE_COLOR, 50, 125)
    draw_text(f"STR: {hero_player.strength}", default_font, WHITE_COLOR, 50, 175)
    draw_text(f"DEX: {hero_player.dexterity}", default_font, WHITE_COLOR, 50, 200)
    draw_text(f"MAG: {hero_player.magic}", default_font, WHITE_COLOR, 50, 225)


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
    for index, enemy_fighter in enumerate(enemy_list):
        if level % 4 != 0:
            draw_text(f"Bandit {index + 1} HP: {enemy_fighter.current_hp}", default_font, WHITE_COLOR, tmp[index][0], tmp[index][1])
        else:
            draw_text(f" Boss {index + 1} HP: {enemy_fighter.current_hp}", default_font, WHITE_COLOR, tmp[index][0],
                      tmp[index][1])


# Item Buttons:
potion_button = button.Button(screen, 110, screen_height - bottom_panel + 75, health_potion_img, 64, 64)
mana_potion_button = button.Button(screen, 220, screen_height - bottom_panel + 75, mana_potion_img, 60, 60)
spellbook_button = button.Button(screen, 0, 695, spellbook_img, 100, 100)
ultimate_button = button.Button(screen, 0, 590, ultimate_img, 80, 80)
lightning_spell_button = button.Button(screen, 150, 220, lightning_img, 150, 150)
firestorm_spell_button = button.Button(screen, 165, 410, firestorm_img, 110, 110)
heal_spell_button = button.Button(screen, 500, 220, heal_img, 130, 130)

# Control Buttons:
restart_button = button.Button(screen, 400, 120, restart_img, 100, 100)
next_button = button.Button(screen, 800, 10, next_img, 80, 80)

#BOTON DE PRUEBAS
prueba_button = button.Button(screen, 400, 400, restart_img, 50, 50)




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


damage_text_group = sprite.Group()
hero_player = HeroPlayer(150, 580, "Hero", 1, 90, 30, 12, 9, 8, 2, 1, 1, 115, screen_height - bottom_panel + 50, 290, screen_height - bottom_panel + 50, 90, 510)
enemy_list = []


runreset = True
runintro = False
runshop = False
runbattle = False
run = True

while run:
    while runreset:
        ###PERAS
        number_of_strikes = 1
        animation_cooldown = 0
        action_cooldown = 0
        runreset = False
        runbattle = True
        # fakeultimate = False
        ultimate = False

        if level % 4 != 0:
            enemy_group = EnemyGroup()
            enemy_list = enemy_group.generate_enemy(level)
            total_fighters = len(enemy_list) + 1
        else:
            total_fighters = 2
            enemy_list = [Bandit(500, 555, "The Boss", 10, 214, 50, 21, 3, 0, 490, (screen_height - bottom_panel + 40))]
            total_fighters = len(enemy_list) + 1


    while runintro:
        screen.blit(background_intro, (0, 0))
        display.update()
        for _event in event.get():
            if _event.type == QUIT:
               run = False
               runintro = False
            if _event.type == MOUSEBUTTONDOWN:
                runintro = False
                runreset = True


    while runshop:
        setup_shop()
        if next_button.draw():
            runshop = False
            runbattle = True

        if lightning_spell_button.draw():
            if hero_player.use_lightning(enemy_list, damage_text_group):
                current_fighter += 1
                action_cooldown = 0
                runshop = False
                runbattle = True

        if firestorm_spell_button.draw():
            if hero_player.use_firestorm(enemy_list, damage_text_group):
                current_fighter += 1
                action_cooldown = 0
                runshop = False
                runbattle = True

        if heal_spell_button.draw():
            if hero_player.use_heal(damage_text_group):
                current_fighter += 1
                action_cooldown = 0
                runshop = False
                runbattle = True

        for _event in event.get():
            if _event.type == QUIT:
               run = False
               runshop = False

        display.update()

    while runbattle:

        # reset action variables
        ###PERAS
        mana_potion = False
        attack = False
        potion = False
        target = None
        loot = False

        setup_battle(enemy_list, hero_player)
        #draw_debug_panel(current_fighter, total_fighters)

        if ultimate_button.draw():
            ultimate = True
        if potion_button.draw():
            potion = True
        if mana_potion_button.draw():
            mana_potion = True
        if spellbook_button.draw():
            runshop = True
            runbattle = False

        if hero_player.current_fury == 100:
            if prueba_button.draw():
                ultimate = True
                hero_player.reset_fury()

        if game_over == 0:
            # make sure mouse is visible
            mouse.set_visible(True)
            pos = mouse.get_pos()
            for count, enemy_unit in enumerate(enemy_list):
                if enemy_unit.unit_animation.rect.collidepoint(pos):
                    # hide mouse
                    mouse.set_visible(False)
                    # show icon
                    screen.blit(sword_img, pos)
                    if clicked and enemy_unit.alive:
                        attack = True
                        target = enemy_list[count]
            #player action
            if hero_player.alive:
                if current_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        # Use: Melee Attack
                        if attack and target is not None:
                            if hero_player.attack(target, damage_text_group):
                                current_fighter += 1
                                action_cooldown = 0

                        # Use: Healing Potion
                        if potion:
                            if hero_player.use_healing_potion(damage_text_group):
                                current_fighter += 1
                                action_cooldown = 0

                        # Use: Mana Potion
                        if mana_potion:
                            if hero_player.use_mana_potion(damage_text_group):
                                current_fighter += 1
                                action_cooldown = 0

                        # Use: Ultimate Spell
                        if ultimate:
                            # if hero_player.use_ultimate(enemy_list, damage_text_group):
                            #     current_fighter += 1
                            #     action_cooldown = 0

                            if number_of_strikes <= 5:
                                for count, target_unit in enumerate(enemy_list):
                                    if action_cooldown >= action_wait_time:

                                        hero_player.attack(enemy_list[randint(0, len(enemy_list)) - 1], damage_text_group)
                                        number_of_strikes = number_of_strikes + 1
                                        #hace la animacion de ataque más rapido
                                        action_cooldown = 55

                            else:
                                number_of_strikes = 1
                                ultimate = False
                                current_fighter += 1
                                # la siguiente accion dl enemigo tardará un poco más después del ultimate
                                action_cooldown = -25
            else:
                game_over = -1

            # Enemy action
            for count, enemy_unit in enumerate(enemy_list):
                if current_fighter == 2 + count:
                    if enemy_unit.alive:
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            # Attack
                            enemy_unit.attack(hero_player, damage_text_group)
                            current_fighter += 1
                            action_cooldown = 0
                    else:
                        current_fighter += 1

            # Reset Turn
            if current_fighter > total_fighters:
                current_fighter = 1

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
                screen.blit(victory_img, (180, 50))
                draw_text(f" Next Battle ", default_font, RED_COLOR, 630, 30)
                ### PERAS correr aquí la funcion de experiencia y ganar nivel
                if next_button.draw():
                    current_fighter = 1
                    game_over = 0
                    action_cooldown = 0
                    runreset = True
                    runbattle = False
                    level += 1

                # LOOT PHASE
                # ADD COOLDOWN BEFORE LOOT
                animation_cooldown += 1
                mouse.set_visible(True)
                pos = mouse.get_pos()
                for count, enemy_unit in enumerate(enemy_list):
                    if enemy_unit.unit_animation.rect.collidepoint(pos):
                        # hide mouse
                        mouse.set_visible(False)
                        # show icon
                        screen.blit(loot_img, pos)
                        if clicked and animation_cooldown >= 30:
                            animation_cooldown = 0
                            target = enemy_list[count]

                            # Todo: Create a proper function
                            if level % 4 == 0:
                                hero_player.loot_boss(target, damage_text_group)
                            else:
                                hero_player.loot(target, damage_text_group)

            if game_over == -1:
                screen.blit(defeat_img,(180, 50))
                draw_text(f" YOU ARE A NOOB ", default_font, RED_COLOR, 340, 350)

        for _event in event.get():
            if _event.type == QUIT:
                run = False
                runbattle = False
            if _event.type == MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False

        display.update()

quit()
