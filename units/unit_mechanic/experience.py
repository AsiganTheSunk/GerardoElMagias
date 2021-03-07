from random import randint
from floating_text.damage_text import DamageText
from constants.basic_colors import *


class ExperienceSystem:
    def evaluate_kill(self, hero_player, target, damage_text_group):
        if not target.alive:
            hero_player.experience = hero_player.experience + target.level

            damage_text = DamageText(120, 500, "+EXP!", YELLOW_COLOR)
            damage_text_group.add(damage_text)

            if hero_player.experience >= hero_player.exp_level_break:
                self.level_up(hero_player, damage_text_group)

    def evaluate_group_kill(self, hero_player, target_list, pre_target_list, post_target_list, damage_text_group):
        for index, target_unit in enumerate(post_target_list):
            if pre_target_list[index] is True and post_target_list[index] is False:
                damage_text = DamageText(120, 500, "+EXP!", YELLOW_COLOR)
                damage_text_group.add(damage_text)

                hero_player.experience += target_list[index].level
                if hero_player.experience >= hero_player.exp_level_break:
                    self.level_up(hero_player, damage_text_group)

    @staticmethod
    def level_up(hero_player, damage_text_group):
        hero_player.strength += randint(2, 3)
        hero_player.dexterity += randint(1, 2)
        hero_player.magic += randint(1, 3)
        hero_player.max_hp += randint(5, 8)
        hero_player.max_mp += randint(3, 5)

        hero_player.exp_level_break = round(hero_player.exp_level_break * 1.6)
        hero_player.level += 1

        damage_text = DamageText(400, 400, "LVL UP", RED_COLOR)
        damage_text_group.add(damage_text)
