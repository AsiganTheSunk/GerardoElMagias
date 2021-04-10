#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Stat Messages
LEVEL_MESSAGE = lambda level: f"Nivel: {level}"
EXPERIENCE_MESSAGE = lambda experience, experience_level_break: f"Experiencia: [{experience}/{experience_level_break}]"
STRENGHT_MESSAGE = lambda strength: f"Fuerza: {strength}"
DEXTERITY_MESSAGE = lambda dexterity: f"Destreza: {dexterity}"
MAGIC_MESSAGE = lambda magic: f"Magia: {magic}"
VITALITAD_MESSAGE = lambda vitality: f"Vitalidad: {vitality}"
RESILIENCE_MESSAGE = lambda resilience: f"Resiliencia: {resilience}"
LUCK_MESSAGE = lambda luck: f"Suerte: {luck}"
ATTACK_POWER = lambda attack_power: f"Poder de Ataque: {attack_power}"
ATTACK_RATING = lambda attack_rating: f"Ratio de Ataque: {attack_rating}"
MAGIC_POWER = lambda magic_power: f"Poder Mágico: {magic_power}"

# Stage Level Message
CURRENT_STAGE = lambda stage_realm, stage_level: f"The {stage_realm.title()} Stage Level: {stage_level}"

# Player Messages
PLAYER_HP = lambda current_hp, max_hp: f"HP: {current_hp}/{max_hp}"
PLAYER_MP = lambda current_mp, max_mp: f"MP: {current_mp}/{max_mp}"
PLAYER_FURY = lambda current_fury, max_fury: f"FP: {current_fury}/{max_fury}"
PLAYER_CONSUMABLE = lambda consumable_amount: f"x{consumable_amount}"

# Unit Message
BOSS_UNIT_TITLE_MESSAGE = lambda boss_name: f"{boss_name}"
ENEMY_UNIT_TITLE_MESSAGE = lambda enemy_unit, enemy_index: f"{enemy_unit} {enemy_index}"

# GameMode Message
NEXT_BATTLE_MESSAGE = f"Batalla Siguiente: Pulsa Next"
DEFEAT_MESSAGE = f"Eres un Jodido Noob, Intentalo de Nuevo!"
VICTORY_MESSAGE = f"Recolecta Objetos de los Cadaveres!"

# Debug Unit Message
TOTAL_ENEMIES_MESSAGE = lambda current_enemies, total_enemies: f"Current Enemy Units [ {total_enemies} / {current_enemies}]"
CURRENT_TURN_MESSAGE = lambda current_unit_turn, current_unit_index: f"Current Turn: {current_unit_turn} {current_unit_index}"

