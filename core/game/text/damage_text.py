#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.game_colors import RED_COLOR, YELLOW_COLOR, WHITE_COLOR, GRAY_COLOR, PURPLE_COLOR, \
    GREEN_COLOR, BLUE_COLOR, ORANGE_COLOR, LIGHT_ORANGE_COLOR
from core.game.text.combat_text_types import CombatTextTypes


class DamageText:
    @staticmethod
    def critical_hit(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.critical_combat_text('- ' + str(message), RED_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def hit(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text('- ' + str(message), RED_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def cast(target, message, text_sprite, displacement_x=0, displacement_y=0):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.cast_text(str(message), YELLOW_COLOR, displacement_x, displacement_y)
        text_sprite.add(floating_text)

    @staticmethod
    def miss(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), WHITE_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def block(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), GRAY_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def dodge(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), GRAY_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def resist(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), PURPLE_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def heal(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text('+ ' + str(message), GREEN_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def mana(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text('+ ' + str(message), BLUE_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def fury(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.combat_text(str(message), ORANGE_COLOR)
        text_sprite.add(floating_text)

    @staticmethod
    def warning(target, message, text_sprite):
        floating_text = CombatTextTypes(target.animation_set.rect.centerx, target.animation_set.rect.y, 'move_up')
        floating_text.critical_combat_text(str(message), LIGHT_ORANGE_COLOR)
        text_sprite.add(floating_text)
