#!/usr/bin/env python
# -*- coding: utf-8 -*-

LEVEL_MESSAGE = lambda level: f"Nivel: {level}"
EXPERIENCE_MESSAGE = lambda experience, experience_level_break: f"Experiencia: [{experience}/{experience_level_break}]"
STRENGHT_MESSAGE = lambda strength: f"Fuerza: {strength}"
DEXTERITY_MESSAGE = lambda dexterity: f"Destreza: {dexterity}"
MAGIC_MESSAGE = lambda magic: f"Magia: {magic}"
VITALITAD_MESSAGE = lambda vitality: f"Vitalidad: {vitality}"
RESILIENCE_MESSAGE = lambda resilience: f"Resiliencia: {resilience}"
LUCK_MESSAGE = lambda luck: f"Suerte: {luck}"


CURRENT_STAGE = lambda stage_realm, stage_level: f"The {stage_realm.title()} Stage Level: {stage_level}"

PLAYER_HP = lambda current_hp, max_hp: f"HP: {current_hp}/{max_hp}"
PLAYER_MP = lambda current_mp, max_mp: f"MP: {current_mp}/{max_mp}"
PLAYER_FURY = lambda current_fury, max_fury: f"FP: {current_fury}/{max_fury}"

PLAYER_CONSUMABLE = lambda consumable_amount: f"x{consumable_amount}"


BOSS_UNIT_TITLE_MESSAGE = lambda boss_name: f"{boss_name}"
ENEMY_UNIT_TITLE_MESSAGE = lambda enemy_unit, enemy_index: f"{enemy_unit} {enemy_index}"


NEXT_BATTLE_MESSAGE = f"Batalla Siguiente"
DEFEAT_MESSAGE = f"Eres un Jodido Noob, Intentalo de Nuevo!"
VICTORY_MESSAGE = f"Recolecta los Objetos en los Cadaveres!"

TOTAL_ENEMIES_MESSAGE = lambda current_enemies, total_enemies: f"Current Enemy Units [ {current_enemies} / {total_enemies}]"
CURRENT_TURN_MESSAGE = lambda current_unit_turn, current_unit_index: f"Current Turn: {current_unit_turn} {current_unit_index}"

ENEMY_UNIT_PANEL_DATA = [
    [680, lambda panel_height_correction: panel_height_correction + 5],
    [680, lambda panel_height_correction: panel_height_correction + 65],
    [900, lambda panel_height_correction: panel_height_correction + 5],
    [900, lambda panel_height_correction: panel_height_correction + 65],
]
