#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from core.game.text.damage_text import DamageText
from core.items.equipement.equipment_generator import EquipmentGenerator
from core.units.enemy.djinn.djinn import Djinn
from core.units.enemy.bone.bone_wizard import BoneWizard
from core.units.enemy.bandit.bandit_chief import BanditChief
from core.units.enemy.bandit.bandit import Bandit
from core.units.enemy.dragon.small_dragon import SmallDragon
from core.units.enemy.dragon.dragon import Dragon
from core.units.enemy.lizard.lizard import Lizard
from core.units.enemy.demon.demon import Demon
from core.items.consumable.db.consumable_db import BREAD, LARGE_BREAD, DRINK, LARGE_DRINK
from logger.logger_master import LoggerMaster
from logger.constants.logger_level_type import LoggingLevelType

# Init: Damage Text
damage_text = DamageText()


class LootMaster:
    def __init__(self, sound_master):
        self.loot_master_logger = LoggerMaster(self.__class__.__name__, LoggingLevelType.DEBUG.value)
        self.sound_master = sound_master

    def loot(self, caster, target, text_sprite):
        if type(target) is Bandit or type(target) is BoneWizard or type(target) is Lizard:
            self.roll_basic_loot(caster, target, text_sprite)
        elif type(target) is BanditChief or type(target) is SmallDragon \
                or type(target) is Djinn or type(target) is Dragon or type(target) is Demon:
            self.roll_boss_loot(caster, target, text_sprite)

    def roll_basic_loot(self, caster, target, text_sprite):
        loot_chance = randint(0, 5)

        if not target.is_looted():
            if loot_chance == 0:
                self.sound_master.play_item_fx_sound('empty')
                damage_text.warning(target, f'Empty!', text_sprite)
                self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__} '
                                                          f'Receiving Nothing')

            elif loot_chance == 1:
                self.sound_master.play_item_fx_sound('health_potion')
                caster.stash.add_healing_potion(1)
                damage_text.warning(target, f'x1 Health Potion Found!', text_sprite)
                self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__} '
                                                          f'Receiving Health Potion')

            elif loot_chance == 2:
                self.sound_master.play_item_fx_sound('health_potion')
                caster.stash.add_mana_potion(1)
                damage_text.warning(target, f'x1 Mana Potion Found!', text_sprite)
                self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__} '
                                                          f'Receiving Mana Potion')

            elif loot_chance == 3:
                quality_roll = randint(0, 50)
                if quality_roll > target.level:
                    damage_text.warning(target, f'Food Found!', text_sprite)
                    BREAD.consume(caster, text_sprite)
                    self.sound_master.play_item_fx_sound('eat')
                    self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__} '
                                                              f'Receiving Bread')
                else:
                    damage_text.warning(target, f'Large Food Found!', text_sprite)
                    LARGE_BREAD.consume(caster, text_sprite)
                    self.sound_master.play_item_fx_sound('eat')
                    self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__} '
                                                              f'Receiving Large Bread')

            elif loot_chance == 4:
                quality_roll = randint(0, 50)
                if quality_roll > target.level:
                    damage_text.warning(target, f'Drink Found!', text_sprite)
                    DRINK.consume(caster, text_sprite)
                    self.sound_master.play_item_fx_sound('drink')
                    self.sound_master.play_item_fx_sound('eat')
                    self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__}'
                                                              f' Receiving Drink')
                else:
                    damage_text.warning(target, f'Large Drink Found!', text_sprite)
                    LARGE_DRINK.consume(caster, text_sprite)
                    self.sound_master.play_item_fx_sound('drink')
                    self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__}'
                                                              f' Receiving Large Drink')

            elif loot_chance == 5:
                gold = randint(1, 9) + target.level
                caster.stash.add_gold(gold)
                damage_text.cast(target, f'{gold} Gold Found!', text_sprite)
                self.sound_master.play_item_fx_sound('gold')
                self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__}'
                                                          f' Receiving {gold} Gold')

            target.update_looted_status()
        else:
            self.loot_error(target, text_sprite)

    def roll_boss_loot(self, caster, target, text_sprite):
        item_generator = EquipmentGenerator()
        if not target.is_looted():
            self.sound_master.play_item_fx_sound('drum_roll')
            # Todo: Proper setup for loot boss, based on level
            roll_item = item_generator.get_item(30, 1000)
            item_name = roll_item.get_item_name()
            damage_text.heal(target, f'{item_name}', text_sprite)
            self.loot_master_logger.log_debug_message(f'Player Loots {target.__class__.__name__}'
                                                      f' Receiving {item_name.title()}')
            target.update_looted_status()
        else:
            self.loot_error(target, text_sprite)

    def loot_error(self, target, text_sprite):
        # Todo: Init with -30y
        damage_text.warning(target, f'ALREADY LOOTED!', text_sprite)
        self.sound_master.play_item_fx_sound('error')
