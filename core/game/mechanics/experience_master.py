#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.text.damage_text import DamageText
from core.game.battle.combat.combat_utils import get_alive_targets_status
from logger.logger_master import LoggerMaster
from logger.constants.logger_level_type import LoggingLevelType
from random import randint

damage_text = DamageText()


class ExperienceMaster:
    def __init__(self, player):
        self.experience_master_logger = LoggerMaster('ExperienceMaster', LoggingLevelType.DEBUG.value)

        self.player = player
        self.experience = 0
        self.exp_level_break = 5

        self.experience_to_gain = 0
        self.previous_exp = 0

    def next_experience_level_break(self):
        self.exp_level_break = round(self.exp_level_break * 1.3)
        self.experience_master_logger.log_debug_message(f'Next Level Break will be {self.exp_level_break}')

    def has_enough_experience(self):
        return self.experience >= self.exp_level_break

    def gain_experience(self):
        self.experience += self.experience_to_gain
        self.experience_to_gain = 0
        if self.has_enough_experience():
            self.experience_master_logger.log_debug_message(f'Player Has Enough Experience to Level Up')
            self.level_up()
            self.experience_master_logger.log_debug_message(f'Player Has {self.experience} Left')
            self.gain_experience()

    def level_up(self):
        strength_raise = randint(2, 3)
        dexterity_raise = randint(1, 2)
        magic_raise = randint(1, 3)
        vitality_raise = randint(2, 4)
        resilience_raise = randint(1, 2)
        luck_raise = randint(1, 2)

        self.level_up_stats(strength_raise, dexterity_raise, magic_raise, vitality_raise, resilience_raise, luck_raise)

        self.previous_exp = self.experience
        self.experience = self.previous_exp - self.exp_level_break
        self.next_experience_level_break()
        self.player.level += 1

    def level_up_stats(self, strength_raise, dexterity_raise, magic_raise, vitality_raise, resilience_raise, luck_raise):
        self.player.strength += strength_raise
        self.player.dexterity += dexterity_raise
        self.player.magic += magic_raise
        self.player.vitality += vitality_raise
        self.player.resilience += resilience_raise
        self.player.luck += luck_raise

        # This will be used when changing equipment to recover the raw value for the hero.
        self.player.raw_strength += strength_raise
        self.player.raw_dexterity += dexterity_raise
        self.player.raw_magic += magic_raise
        self.player.raw_vitality += vitality_raise
        self.player.raw_resilience += resilience_raise
        self.player.raw_luck += luck_raise

        self.player.attack_power = self.player.strength * 1
        self.player.attack_rating = self.player.dexterity * 1
        self.player.magic_power = self.player.magic * 1

        # calculate max hp and max mp
        self.player.max_hp = self.player.vitality * 3
        self.player.current_hp = self.player.current_hp + vitality_raise * 3
        self.player.max_mp = self.player.magic * 2 + self.player.resilience
        self.player.current_mp = self.player.current_mp + magic_raise * 2 + resilience_raise

    def evaluate_kill(self, target, text_sprite):
        if not target.alive:
            self.experience_to_gain += target.level
            damage_text.cast(self.player, "+EXP!", text_sprite)
            self.experience_master_logger.log_debug_message(f'Player Kills {target.__class__.__name__} '
                                                            f'and Gains +{target.level} XP')

    def evaluate_group_kill(self, target_list, pre_target_list, post_target_list, text_sprite):
        for index, target_unit in enumerate(post_target_list):
            if pre_target_list[index] is True and post_target_list[index] is False:
                self.experience_to_gain += target_list[index].level
                self.experience_master_logger.log_debug_message(f'Player Kills {target_list[index].__class__.__name__} '
                                                                f'and Gains +{target_list[index].level} XP')
                damage_text.cast(self.player, "+EXP!", text_sprite)
