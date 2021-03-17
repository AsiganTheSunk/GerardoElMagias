#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Father Karras and AsiganTheSunk"
__copyright__ = "Copyright 2021, Gerardo El Magias"

__credits__ = ["Father Karras", "AsiganTheSunk", "GRAN CALAVERA", "Señor Pechuza"]
__version__ = "0.1a"
__maintainer__ = "Father Karras and AsiganTheSunk"
__email__ = ""
__status__ = "Development"

# Pygame Imports:
from pygame import time, display, sprite, mouse, quit, init

init()

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

mixer.pre_init(44100, -16, 2, 4096)
clock = time.Clock()
fps = 60

screen = display.set_mode((screen_width, screen_height))
display.set_caption("Las trepidantes aventuras de Gerardo EL MAGIAS")

update_time = time.get_ticks()

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
    draw_text(f"{hero_player.stash.gold}", default_font, YELLOW_COLOR, 80, 30)
    draw_text(f"LVL: {hero_player.level}", default_font, WHITE_COLOR, 50, 100)
    draw_text(f"Exp: {hero_player.experience} / {hero_player.exp_level_break} ", default_font, WHITE_COLOR, 50, 125)
    draw_text(f"STR: {hero_player.strength}", default_font, WHITE_COLOR, 50, 175)
    draw_text(f"DEX: {hero_player.dexterity}", default_font, WHITE_COLOR, 50, 200)
    draw_text(f"MAG: {hero_player.magic}", default_font, WHITE_COLOR, 50, 225)
    if battle_master.level <= 7:
        draw_text(f"THE WOODS: STAGE {battle_master.level}", default_font, RED_COLOR, 310, 25)
    else:
        draw_text(f"THE CASTLE: STAGE {battle_master.level - 7}", default_font, RED_COLOR, 310, 25)


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

    if battle_master.is_boss_level(battle_master.level):
        draw_text(f" The Boss HP: {battle_master.enemy_fighters[0].current_hp}", default_font, WHITE_COLOR, tmp[0][0],
                  tmp[0][1])
    else:
        for index, enemy_fighter in enumerate(battle_master.enemy_fighters):
            draw_text(f"{enemy_fighter.name} HP: {enemy_fighter.current_hp}", default_font, WHITE_COLOR, tmp[index][0],
                      tmp[index][1])


def setup_battle(enemies, friendlies):
    hero = friendlies[0]
    clock.tick(fps)

    # draw backgrounds
    if battle_master.level <= 7:
        draw_bg_forest()
    if battle_master.level > 7:
        draw_bg_castle()

        # draw panel
    draw_stage()
    draw_panel()
    screen.blit(oro_img, (20, 20))

    # damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # draw fighters
    hero.animation_set.update()
    hero.animation_set.draw(screen)
    hero.health_bar.draw(hero.current_hp, hero.max_hp, screen)
    hero.mana_bar.draw(hero.current_mp, hero.max_mp, screen)
    hero.fury_bar.draw(hero.current_fury, hero.max_fury, screen)

    for target_unit in enemies:
        target_unit.animation_set.update()
        target_unit.animation_set.draw(screen)
        target_unit.health_bar.draw(target_unit.current_hp, target_unit.max_hp, screen)


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

    setup_battle(battle_master.enemy_fighters, battle_master.friendly_fighters)

    if kill_button.draw():
        for target_unit in battle_master.enemy_fighters:
            target_unit.death()
            target_unit.death_animation()

    if potion_button.draw():
        hero_player.next_action = ['use', 'healing_potion']
    if mana_potion_button.draw():
        hero_player.next_action = ['use', 'mana_potion']
    if spellbook_button.draw():
        battle_master.game_mode = GameModes.SPELLBOOK
    if battle_master.game_mode == GameModes.SPELLBOOK:
        open_spellbook(hero_player, battle_master.enemy_fighters, screen, damage_text_group,
                       battle_master)  # esto es to cutre
    if hero_player.current_fury == 100 and ultimate_button.draw():
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
                mouse.set_visible(False)
                # show icon
                screen.blit(sword_img, pos)
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
                if not mixer.get_busy():
                    victory_music.play()
                screen.blit(victory_img, (180, 50))
                draw_text(f" Next Battle ", default_font, RED_COLOR, 630, 30)
            else:
                draw_text(f" STAGE CLEARED ", default_font, RED_COLOR, 330, 250)
                draw_text(f" GET YOUR LOOT! ", default_font, RED_COLOR, 330, 300)
                draw_text(f" Next Battle ", default_font, RED_COLOR, 630, 30)

            if next_button.draw():
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
                    screen.blit(loot_img, pos)
                    if constants.globals.clicked:

                        # Todo: Create a proper function
                        if battle_master.is_boss_level(battle_master.level):
                            hero_player.loot_boss(enemy_unit, damage_text_group)
                        else:
                            hero_player.loot(enemy_unit, damage_text_group)
                        constants.globals.clicked = False

        if battle_master.game_mode == GameModes.DEFEAT:
            screen.blit(defeat_img, (180, 50))
            draw_text(f" YOU ARE A NOOB ", default_font, RED_COLOR, 340, 350)

    constants.globals.action_cooldown += 2
    hero_player.next_action = None

    event_control()

    display.update()

quit()
