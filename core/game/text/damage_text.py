#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.basic_colors import *
from core.game.text.combat_text_types import CombatTextTypes


class DamageText:
    @staticmethod
    def critical_hit(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.critical_combat_text('- ' + str(message), RED_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def hit(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text('- ' + str(message), RED_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def cast(target, message, damage_text_group, displacement_x=0, displacement_y=0):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.cast_text(str(message), YELLOW_COLOR, displacement_x, displacement_y)
        damage_text_group.add(floating_text)

    @staticmethod
    def miss(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), WHITE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def block(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), GRAY_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def dodge(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), GRAY_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def resist(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), PURPLE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def heal(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text('+ ' + str(message), GREEN_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def mana(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text('+ ' + str(message), BLUE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def fury(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), ORANGE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def warning(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.critical_combat_text(str(message), LIGHT_ORANGE_COLOR)
        damage_text_group.add(floating_text)
