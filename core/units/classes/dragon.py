from core.units.skills.melee import MeleeSpells

from core.units.skills.magic import MagicSpells
from core.units.mechanics.loot import LootPool
from core.units.basic_unit import BasicUnit
from core.units.resources.health_bar import HealthBar
from core.units.resources.stash import Stash
from random import randint
from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText



# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()

# Animation Imports
from core.units.animations.animation_db import DragonSet
from core.units.animations.animation_set import AnimationSet

import constants.globals

class Dragon(BasicUnit, MagicSpells, MeleeSpells):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, health_bar_x, health_bar_y):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        MeleeSpells.__init__(self)
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.stash = Stash(healing_potions=round(self.level / 5), mana_potions=0, gold=0)
        # Bandit Loot
        self.looted_status = False
        self.try_to_consume_health_potion = False
        self.loot_pool = LootPool()
        self.animation_set = AnimationSet(x, y, name, DragonSet)


    def is_looted(self):
        if self.looted_status:
            return True
        return False

    def update_looted_status(self):
        self.looted_status = True

    def attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_attack(self, target, damage_text_group)
        return True

    def use_heal(self, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(12):
            constants.globals.action_cooldown = -30
            self.cast_heal(self, self, damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False

    def use_firestorm(self, target_list, damage_text_group):
        # Consume Mana: Spell Casting
        if self.reduce_mana(15):
            constants.globals.action_cooldown = -30
            # Pre Save State for Enemy List: target_list
            pre_target_list = get_alive_targets_status(target_list)

            # Retrieve State for Enemy List: target_list
            self.cast_firestorm(self, target_list, damage_text_group)

            # Post Save State for Enemy List: target_list
            pos_target_list = get_alive_targets_status(target_list)

            # Evaluate Kills
            self.experience_system.evaluate_group_kill(self, target_list, pre_target_list, pos_target_list,
                                                       damage_text_group)
            return True

        damage_text.warning(self, ' No Enough Mana! ', damage_text_group)
        return False


    def death_animation(self):
        # Activates: Death Animation
        self.animation_set.action = 1
        self.animation_set.reset_frame_index()

    def melee_attack_animation(self):
        # Activates: Melee Attack Animation
        self.animation_set.action = 2
        self.animation_set.reset_frame_index()

    def hurt_animation(self):
        # Activates: Hurt Animation
        self.animation_set.action = 3
        self.animation_set.reset_frame_index()

    def block_animation(self):
        # Activates: Block Animation
        self.animation_set.action = 4
        self.animation_set.reset_frame_index()

    def miss_animation(self):
        # Activates: Miss Animation
        self.animation_set.action = 5
        self.animation_set.reset_frame_index()


    def action(self, target, damage_text_group):
        health_trigger = self.current_hp <= round(self.max_hp * 1)
        if health_trigger:
            i = randint(1, 2)
            if i == 1:
                self.attack(target, damage_text_group)
            elif i == 2:
                self.use_heal(damage_text_group)
            elif i == 3:
                self.use_firestorm(target, damage_text_group)
        else:
            self.attack(target, damage_text_group)