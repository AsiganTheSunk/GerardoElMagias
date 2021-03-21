#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame Imports:
from pygame import mouse


# Game Engine Constants Imports:

from constants.sound import ultimate_sound
import constants.globals

# Game Drawable Instance Imports:
from interface.composed_component.spell_book import open_spell_book

# Game Control Imports:
import constants.globals

# Master Game Engine Imports
from core.game.game_modes import GameModes

from core.text.damage_text import DamageText


# Init DamageText
damage_text = DamageText()


def reset(run_reset, hero_player):
    if run_reset:
        constants.globals.action_cooldown = 0
        hero_player.ultimate_status = False
        hero_player.multi_attacks_left = 7
    return False


def kill_switch(battle_master, stage_drawer):
    if stage_drawer.display_kill_all():
        for target_unit in battle_master.enemy_fighters:
            if target_unit.alive:
                target_unit.death()
                target_unit.death_animation()


def resolve_player_interface_actions(hero_player, battle_master, stage_drawer, game_attributes, action_wait_time):
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


def resolve_player_loot(hero_player, battle_master, stage_drawer, game_attributes, previous_mouse_collision):
    if battle_master.game_mode is GameModes.VICTORY:
        for enemy_unit in battle_master.enemy_fighters:
            if enemy_unit.animation_set.mouse_collision():
                previous_mouse_collision = True
                stage_drawer.display_bag_mouse()
                if constants.globals.clicked:
                    hero_player.loot(enemy_unit, game_attributes.text_sprite)
                    constants.globals.clicked = False

            if previous_mouse_collision is True and not enemy_unit.animation_set.mouse_collision():
                previous_mouse_collision = False
                mouse.set_visible(True)

    return previous_mouse_collision


def resolve_player_attack(hero_player, battle_master, stage_drawer, previous_mouse_collision):
    if battle_master.game_mode is GameModes.BATTLE or battle_master.game_mode is GameModes.BOSS_BATTLE:
        for enemy_unit in battle_master.enemy_fighters:
            if enemy_unit.animation_set.mouse_collision():
                previous_mouse_collision = True
                stage_drawer.display_sword_mouse()
                if constants.globals.clicked and enemy_unit.alive:
                    hero_player.next_action = ('attack', enemy_unit)

            if previous_mouse_collision is True and not enemy_unit.animation_set.mouse_collision():
                previous_mouse_collision = False
                mouse.set_visible(True)

    return previous_mouse_collision


def resolve_combat(battle_master, action_wait_time, game_attributes):
    if battle_master.game_mode is GameModes.BATTLE or battle_master.game_mode is GameModes.BOSS_BATTLE:
        if constants.globals.action_cooldown >= action_wait_time:
            battle_master.run_fighter_action(game_attributes.text_sprite)


def resolve_defeat(battle_master, stage_drawer):
    # Defeat Check
    if battle_master.game_mode is GameModes.DEFEAT:
        stage_drawer.display_defeat()


def resolve_victory(run_reset, battle_master, stage_drawer):
    # Victory Check
    if battle_master.game_mode is GameModes.VICTORY:
        stage_drawer.display_victory()

        if stage_drawer.display_next_button():
            run_reset = True
            battle_master.next_level()
    return run_reset


def update_victory_status(battle_master):
    # Check if all enemies are dead for win condition
    if battle_master.are_enemies_alive():
        battle_master.game_mode = GameModes.VICTORY