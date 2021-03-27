#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game.text.damage_text import DamageText

damage_text = DamageText()


class ExperienceSystem:
    def evaluate_kill(self, hero_player, target, damage_text_group):
        if not target.alive:
            hero_player.experience_to_gain = hero_player.experience_to_gain + target.level

            # Todo: Move init position for the text, 120x, 500y
            damage_text.cast(hero_player, "+EXP!", damage_text_group)


    def evaluate_group_kill(self, hero_player, target_list, pre_target_list, post_target_list, damage_text_group):
        for index, target_unit in enumerate(post_target_list):
            if pre_target_list[index] is True and post_target_list[index] is False:

                # Todo: Move init position for the text 120x, 500y
                damage_text.cast(hero_player, "+EXP!", damage_text_group)
                hero_player.experience_to_gain += target_list[index].level
