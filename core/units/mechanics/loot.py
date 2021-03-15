from random import randint
from core.text.damage_text import DamageText
from constants.sound import *

from core.items.item_generator import ItemGenerator

# Init: Damage Text
damage_text = DamageText()


class LootPool:
    @staticmethod
    def get_loot(hero_player, target, damage_text_group):
        loot_chance = randint(0, 5)

        if not target.is_looted():
            if loot_chance == 0:
                empty_sound.play()
                damage_text.warning(target, f' Empty ', damage_text_group)

            elif loot_chance == 1:
                # Activates potion sound
                health_potion_sound.play()
                hero_player.stash.add_healing_potion(1)
                damage_text.heal(target, f' 1 Healing Potion! ', damage_text_group)

            elif loot_chance == 2:
                eat_sound.play()
                food_healing = 30
                gained_health = hero_player.gain_health(food_healing)
                damage_text.heal(target, f' Found Food! {gained_health} Health ', damage_text_group)

            elif loot_chance == 3:
                # Activates potion sound
                health_potion_sound.play()
                hero_player.stash.add_mana_potion(1)
                damage_text.mana(target, f' 1 Mana Potion! ', damage_text_group)

            elif loot_chance == 4:
                drink_sound.play()
                drink = 10
                gained_mana = hero_player.gain_mana(drink)
                damage_text.mana(target, f' Found Drink {gained_mana} Mana ', damage_text_group)

            elif loot_chance == 5:
                gold = randint(1, 4) + target.level
                hero_player.stash.add_gold(gold)
                gold_sound.play()
                damage_text.cast(target, f' {gold} Gold! ', damage_text_group)

            target.update_looted_status()

        else:
            # Todo: Init with -30y
            damage_text.warning(target, f' ALREADY LOOTED! ', damage_text_group)
            error_sound.play()

    @staticmethod
    def get_loot_boss(hero_player, target, damage_text_group):
        loot_chance = randint(0, 0)
        if not target.is_looted():
            drum_roll_sound.play()
            item_generator = ItemGenerator()
            if loot_chance == 0:
                generated_item = item_generator.get_item(30, 1000)
                new_item = generated_item.get_item_name()
                print(new_item)
                # damage_text.heal(target, f' Espada de Yisus ', damage_text_group)
                damage_text.heal(target, f'{new_item}', damage_text_group)

            # elif loot_chance == 1:
            #     damage_text.heal(target, f' Escudo de Yisus! ', damage_text_group)
            #
            # elif loot_chance == 2:
            #     damage_text.heal(target, f' Armadura de Yisus ', damage_text_group)

            target.update_looted_status()

        else:
            # Todo: Init with -30y
            damage_text.warning(target, f' ALREADY LOOTED! ', damage_text_group)
