from core.game_units.unit_class.melee.melee_figher import MeleeFighter
from core.game_units.basic_unit import BasicUnit
from core.game_units.unit_mechanic.health_bar import HealthBar
from core.game_units.unit_mechanic.mana_bar import ManaBar
from core.game_units.unit_resource.stash import Stash

from core.game_units.unit_class.mage.damage_spells import DamageSpells
from core.game_units.unit_class.mage.healing_spells import HealingSpells
from core.game_units.unit_class.melee.hero_melee_spells import HeroMeleeSpells

from core.game_units.unit_mechanic.fury_bar import FuryBar
from core.game_units.unit_mechanic.experience import ExperienceSystem
from random import randint
from core.game_text.combat_text_resolver import CombatTextResolver
from core.game_text.damage_text import DamageText
from core.game_units.unit_mechanic.utils import get_alive_targets_status


# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class HeroPlayer(BasicUnit, MeleeFighter):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, healing_potion, magic_potion, gold, health_bar_x, health_bar_y, mana_bar_x, mana_bar_y, fury_bar_x, fury_bar_y):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.mana_bar = ManaBar(mana_bar_x, mana_bar_y, self.current_mp, self.max_mp)
        self.fury_bar = FuryBar(fury_bar_x, fury_bar_y, self.current_fury, self.max_fury)
        self.stash = Stash(healing_potion, magic_potion, gold)

        self.damage_spells = DamageSpells()
        self.healing_spells = HealingSpells()
        self.hero_spells = HeroMeleeSpells()
        self.experience_system = ExperienceSystem()

        self.experience = 0
        self.exp_level_break = 5

    def attack(self, target, damage_text_group):
        output_damage, output_message = self.cast_attack(self)

        # Activates Attack Animation: Bandit -> MeleeFighter
        self.melee_attack()

        # Activates Blocked Animation on Target
        if 'Blocked' in output_message:
            # Todo: Update Animation to proper block animation
            target.block()

        # Activates Miss Animation on Target
        elif 'Miss' in output_message:
            # Todo: Rename or Change block to miss animation frame for consistency purposes
            target.block()

        # Activates Hurt/Death Animation on Target
        else:
            if output_damage != 0:
                target.reduce_health(output_damage)

                # Activates Hurt Animation: Target
                target.hurt()

                # Evaluate Death: Target
                if target.is_dead():
                    target.death()
                    # Gain XP
                    self.experience_system.evaluate_kill(self, target, damage_text_group)

        combat_text_resolver.resolve(target, str(output_damage) + output_message, damage_text_group)
        return True

    def loot(self, target, damage_text_group):
        target.loot_pool.get_loot(self, target, damage_text_group)

    def loot_boss(self, target, damage_text_group):
        target.loot_pool.get_loot_boss(self, target, damage_text_group)

    def use_ultimate(self, number_of_strikes, target_list, damage_text_group,
                     action_cooldown, action_wait_time, current_fighter, ultimate_status):

        if number_of_strikes == 0:
            damage_text.cast(self, "Senda de los 7 Golpes", damage_text_group)

        return self.hero_spells.cast_path_of_the_seven_strikes(self, number_of_strikes, target_list, damage_text_group,
                                                               action_cooldown, action_wait_time, current_fighter,
                                                               ultimate_status)

    def use_firestorm(self, target_list, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):

            # Pre Save State for Enemy List: target_list
            pre_target_list = get_alive_targets_status(target_list)

            # Retrieve State for Enemy List: target_list
            self.damage_spells.cast_firestorm(self, target_list, damage_text_group)

            # Post Save State for Enemy List: target_list
            pos_target_list = get_alive_targets_status(target_list)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list, damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False

    def use_lightning(self, target_list, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(20):
            # Save State for Enemy List: target_list
            pre_target_list = get_alive_targets_status(target_list)

            self.damage_spells.cast_lightning(self, target_list, damage_text_group)
            # Retrieve State for Enemy List: target_list
            pos_target_list = get_alive_targets_status(target_list)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list, damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False

    def use_heal(self, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            self.healing_spells.cast_heal(self, damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False

    def use_healing_potion(self, damage_text_group):
        if self.stash.has_healing_potion():
            base_health = 40
            health_interval = randint(0, 10)
            base_health_multiplier = (self.level * 4)
            health_recover = base_health + health_interval + base_health_multiplier

            self.stash.consume_healing_potion()
            gained_health = self.gain_health(health_recover)

            damage_text.heal(self, str(gained_health), damage_text_group)
            return True

        damage_text.warning(self, 'No Healing Potions', damage_text_group)
        return False

    def use_mana_potion(self, damage_text_group):
        if self.stash.has_mana_potion():
            base_mana = 15
            mana_interval = randint(0, 5)
            base_mana_multiplier = (self.level * 2)
            mana_recover = base_mana + mana_interval + base_mana_multiplier

            self.stash.consume_mana_potion()
            gained_mana = self.gain_mana(mana_recover)

            damage_text.mana(self, str(gained_mana), damage_text_group)
            return True

        damage_text.warning(self, 'No Mana Potions', damage_text_group)
        return False
