#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.text.damage_text import DamageText

damage_text = DamageText()


class ExperienceSystem:
    def evaluate_kill(self, hero_player, target, damage_text_group):
        if not target.alive:
            hero_player.experience = hero_player.experience + target.level

            # Todo: Move init position for the text, 120x, 500y
            damage_text.cast(hero_player, "+EXP!", damage_text_group)

            if hero_player.experience >= hero_player.exp_level_break:
                self.level_up(hero_player, damage_text_group)

    def evaluate_group_kill(self, hero_player, target_list, pre_target_list, post_target_list, damage_text_group):
        for index, target_unit in enumerate(post_target_list):
            if pre_target_list[index] is True and post_target_list[index] is False:

                # Todo: Move init position for the text 120x, 500y
                damage_text.cast(hero_player, "+EXP!", damage_text_group)

                hero_player.experience += target_list[index].level
                if hero_player.experience >= hero_player.exp_level_break:
                    self.level_up(hero_player, damage_text_group)

    @staticmethod
    def level_up(hero_player, damage_text_group):
        hero_player.strength += randint(2, 3)
        hero_player.dexterity += randint(1, 2)
        hero_player.magic += randint(1, 3)
        i = randint(6,10)
        hero_player.max_hp += i
        hero_player.current_hp += i
        i = randint(3, 5)
        hero_player.max_mp += i
        hero_player.current_mp += i

        hero_player.exp_level_break = round(hero_player.exp_level_break * 1.6)
        hero_player.level += 1

        damage_text.warning(hero_player, "LVL UP", damage_text_group)
