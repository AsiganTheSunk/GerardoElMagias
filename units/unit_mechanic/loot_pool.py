from random import randint
from floating_text.damage_text import DamageText
from constants.basic_colors import *


class LootPool:
    @staticmethod
    def get_loot(hero_player, target, damage_text_group):
        loot_message = f' Empty '
        loot_color = WHITE_COLOR
        loot_chance = randint(0, 5)

        if not target.is_looted():
            if loot_chance == 0:
                pass

            elif loot_chance == 1:
                loot_color = GREEN_COLOR
                loot_message = f' +1 Healing Potion! '
                hero_player.stash.add_healing_potion(1)

            elif loot_chance == 2:
                loot_color = GREEN_COLOR
                loot_message = f' Found Food: +30 HEALTH! '

                food_healing = 30
                hero_player.gain_health(food_healing)

            elif loot_chance == 3:
                loot_color = BLUE_COLOR
                loot_message = f' +1 Mana Potion! '
                hero_player.stash.add_mana_potion(1)

            elif loot_chance == 4:
                loot_color = BLUE_COLOR
                loot_message = f' Found Drink: +10 MANA! '
                drink = 10
                hero_player.gain_mana(drink)

            elif loot_chance == 5:
                gold = randint(1, 4) + target.level
                loot_color = YELLOW_COLOR
                loot_message = f' {gold} Gold! '
                hero_player.stash.add_gold(gold)

            target.update_looted_status()

        else:
            loot_color = RED_COLOR
            loot_message = f' ALREADY LOOTED! '

        damage_text = DamageText(target.unit_animation.rect.centerx, target.unit_animation.rect.y - 30, loot_message, loot_color)
        damage_text_group.add(damage_text)

    @staticmethod
    def get_loot_boss(hero_player, target, damage_text_group):
        loot_message = f' Empty '
        loot_color = WHITE_COLOR
        loot_chance = randint(0, 2)

        if not target.is_looted():
            if loot_chance == 0:
                loot_color = GREEN_COLOR
                loot_message = f' Espada de Yisus '

            elif loot_chance == 1:
                loot_color = GREEN_COLOR
                loot_message = f' Escudo de Yisus! '

            elif loot_chance == 2:
                loot_color = GREEN_COLOR
                loot_message = f' Armadura de Yisus '

        else:
            loot_color = RED_COLOR
            loot_message = f' ALREADY LOOTED! '

        damage_text = DamageText(target.unit_animation.rect.centerx, target.unit_animation.rect.y - 30, loot_message, loot_color)
        damage_text_group.add(damage_text)