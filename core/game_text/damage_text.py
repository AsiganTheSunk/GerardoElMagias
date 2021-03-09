#!/usr/bin/env python

from constants.basic_colors import *
from core.game_text.combat_text_types import CombatTextTypes


class DamageText:
    @staticmethod
    def critical_hit(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text('- ' + message, RED_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def hit(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text('- ' + message, RED_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def cast(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.cast_text(message, YELLOW_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def miss(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text(message, WHITE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def block(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text(message, GRAY_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def dodge(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text(message, GRAY_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def resist(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text(message, PURPLE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def heal(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text('+ ' + message, GREEN_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def mana(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text('+ ' + message, BLUE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def fury(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text(message, ORANGE_COLOR)
        damage_text_group.add(floating_text)

    @staticmethod
    def warning(target, message, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text(message, LIGHT_ORANGE_COLOR)
        damage_text_group.add(floating_text)
