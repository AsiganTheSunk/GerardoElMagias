from core.units.mechanics.loot import LootPool
from core.units.basic_unit import BasicUnit
from core.units.resources.health_bar import HealthBar
import constants.globals

global ulti_atacks
ulti_atacks = 1

# Skill Imports
from core.units.skills.melee import MeleeSpells

# Animation Imports
from core.units.animations.animation_db import DjinnSet
from core.units.animations.animation_set import AnimationSet


class Djinn(BasicUnit, MeleeSpells):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, health_bar_x, health_bar_y):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        MeleeSpells.__init__(self)

        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        # Bandit Loot
        self.looted_status = False
        self.loot_pool = LootPool()
        self.animation_set = AnimationSet(x, y, name, DjinnSet)
        self.current_fury = 1
        self.fury_status = True
        self.power_of_two_base = 0

    def is_looted(self):
        return self.looted_status

    def update_looted_status(self):
        self.looted_status = True

    def attack(self, target, damage_text_group):
        self.melee_attack_animation()
        self.cast_attack(self, target, damage_text_group)
        return True

    def power_of_two_attack(self, target, damage_text_group, base):
        self.cast_power_of_two_attack
        self.power_of_two_base += 1

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
        self.attack(target, damage_text_group)