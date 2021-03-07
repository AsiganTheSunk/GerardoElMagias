#!/usr/bin/env python

from floating_text.combat_text_types import CombatTextTypes


class DamageText:
    @staticmethod
    def critical_hit(target, message, message_color, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text(message, message_color)
        damage_text_group.add(floating_text)

    @staticmethod
    def hit(target, message, message_color, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.combat_text(message, message_color)
        damage_text_group.add(floating_text)

    @staticmethod
    def cast(target, message, message_color, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text(message, message_color)
        damage_text_group.add(floating_text)

    @staticmethod
    def miss(target, message, message_color, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text(message, message_color)
        damage_text_group.add(floating_text)

    @staticmethod
    def dodge(target, message, message_color, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text(message, message_color)
        damage_text_group.add(floating_text)

    @staticmethod
    def resist(target, message, message_color, damage_text_group):
        floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
        floating_text.critical_combat_text(message, message_color)
        damage_text_group.add(floating_text)



