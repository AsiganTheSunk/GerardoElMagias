from units.unit_class.melee.melee_figher import MeleeFighter
from units.unit_class.mage.damage_spells import DamageSpells
from units.unit_class.mage.healing_spells import HealingSpells
from units.unit_class.melee.hero_melee_spells import HeroMeleeSpells

from units.basic_unit import BasicUnit
from units.unit_mechanic.health_bar import HealthBar
from units.unit_mechanic.fury_bar import FuryBar
from units.unit_mechanic.mana_bar import ManaBar

from units.unit_resource.stash import Stash
from units.unit_mechanic.experience import ExperienceSystem

from random import randint
from floating_text.damagetext import DamageText
from constants.basic_colors import *


class HeroPlayer(BasicUnit, MeleeFighter):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, healing_potion, magic_potion, gold, health_bar_x, health_bar_y, mana_bar_x, mana_bar_y, fury_bar_x, fury_bar_y):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.mana_bar = ManaBar(mana_bar_x, mana_bar_y, self.current_mp, self.max_mp)
        # self.fury_bar = FuryBar(fury_bar_x, fury_bar_y, self.current_fury, self.max_fury)
        self.stash = Stash(healing_potion, magic_potion, gold)

        self.damage_spells = DamageSpells()
        self.healing_spells = HealingSpells()
        self.hero_spells = HeroMeleeSpells()
        self.experience_system = ExperienceSystem()

        self.experience = 0
        self.exp_level_break = 5

    def attack(self, target, damage_text_group):
        output_damage, output_message, output_color = self.cast_attack(self)

        # Activates Attack Animation: Bandit -> MeleeFighter
        self.unit_animation.melee_attack_animation()

        if output_damage != 0:
            target.current_hp -= output_damage

            # Activates Hurt Animation: Target
            target.hurt()

            if target.current_hp < 1:
                target.death()
                self.experience_system.evaluate_kill(self, target, damage_text_group)

        damage_text = DamageText(target.unit_animation.rect.centerx, target.unit_animation.rect.y, str(output_damage) + output_message, output_color)
        damage_text_group.add(damage_text)
        return True

    def loot(self, target, damage_text_group):
        target.loot_pool.get_loot(self, target, damage_text_group)

    def loot_boss(self, target, damage_text_group):
        target.loot_pool.get_loot_boss(self, target, damage_text_group)

    def use_ultimate(self, target_list, damage_text_group):
        self.hero_spells.cast_ultimate(self, target_list, damage_text_group)
        return True

    def use_fakeultimate(self, target_list, damage_text_group):
        self.hero_spells.cast_ultimate(self, target_list, damage_text_group)
        return True

    def use_firestorm(self, target_list, damage_text_group):
        if self.current_mp >= 15:
            # Consume Mana: Spell Casting
            self.current_mp -= 15

            # Pre Save State for Enemy List: target_list
            pre_target_list = []
            for enemy_unit in target_list:
                if enemy_unit.alive:
                    pre_target_list.append(True)
                else:
                    pre_target_list.append(False)

            # Retrieve State for Enemy List: target_list
            self.damage_spells.cast_firestorm(self, target_list, damage_text_group)

            # Post Save State for Enemy List: target_list
            pos_target_list = []
            for enemy_unit in target_list:
                if enemy_unit.alive:
                    pos_target_list.append(True)
                else:
                    pos_target_list.append(False)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list, damage_text_group)
            return True

        damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, ' No Enough Mana! ', RED_COLOR)
        damage_text_group.add(damage_text)
        return False

    def use_lightning(self, target_list, damage_text_group):
        if self.current_mp >= 20:
            # Consume Mana: Spell Casting
            self.current_mp -= 20

            # Save State for Enemy List: target_list
            pre_target_list = []
            for enemy_unit in target_list:
                if enemy_unit.alive:
                    pre_target_list.append(True)
                else:
                    pre_target_list.append(False)

            self.damage_spells.cast_lightning(self, target_list, damage_text_group)
            # Retrieve State for Enemy List: target_list
            pos_target_list = []
            for enemy_unit in target_list:
                if enemy_unit.alive:
                    pos_target_list.append(True)
                else:
                    pos_target_list.append(False)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list, damage_text_group)
            return True

        damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, ' No Enough Mana! ', RED_COLOR)
        damage_text_group.add(damage_text)
        return False

    def use_heal(self, damage_text_group):
        if self.current_mp >= 12:
            self.current_mp -= 12
            self.healing_spells.cast_heal(self, damage_text_group)
            return True

        damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, ' No Enough Mana! ', RED_COLOR)
        damage_text_group.add(damage_text)
        return False

    def use_healing_potion(self, damage_text_group):
        if self.stash.healing_potions >= 1:
            base_health = 40
            health_interval = randint(0, 10)
            base_health_multiplier = (self.level * 4)
            health_recover = base_health + health_interval + base_health_multiplier

            if self.max_hp - self.current_hp > health_recover:
                heal_amount = health_recover
            else:
                heal_amount = self.max_hp - self.current_hp
            self.current_hp += heal_amount
            self.stash.consume_healing_potion()
            damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, str(heal_amount), GREEN_COLOR)
            damage_text_group.add(damage_text)
            return True

        damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, 'No Healing Potions', RED_COLOR)
        damage_text_group.add(damage_text)
        return False

    def use_mana_potion(self, damage_text_group):
        if self.stash.mana_potions >= 1:
            base_mana = 15
            mana_interval = randint(0, 5)
            base_mana_multiplier = (self.level * 2)
            mana_recover = base_mana + mana_interval + base_mana_multiplier

            if self.max_mp - self.current_mp > mana_recover:
                mana_recovered = mana_recover
            else:
                mana_recovered = self.max_mp - self.current_mp
            self.current_mp += mana_recovered
            self.stash.consume_mana_potion()
            damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, str(mana_recovered), BLUE_COLOR)
            damage_text_group.add(damage_text)
            return True

        damage_text = DamageText(self.unit_animation.rect.centerx, self.unit_animation.rect.y, 'No Healing Potions', RED_COLOR)
        damage_text_group.add(damage_text)
        return False
