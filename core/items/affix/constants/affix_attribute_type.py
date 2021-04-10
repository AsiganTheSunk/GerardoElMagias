#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class AffixAttributeType(Enum):
    STRENGTH = 'Fuerza'
    MAGIC = 'Magia'
    DEXTERITY = 'Destreza'
    HEALTH = 'Vida'
    MANA = 'Mana'
    FURY = 'Furia'
    BLOCK_CHANCE = "Probabilidad de bloqueo"
    ARMOR = "Armadura"
    LIFE_LEECH = "Robo de vida"
    MANA_LEECH = "Robo de mana"
    MAXIMUM_WEAPON_DAMAGE = "Daño Máximo"
    MAX_ULTIMATE_STRIKES = "Ataques del ultimate"



