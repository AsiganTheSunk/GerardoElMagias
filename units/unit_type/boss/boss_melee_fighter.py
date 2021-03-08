from units.unit_class.melee.melee_figher import MeleeFighter
from units.unit_mechanic.loot_pool import LootPool
from units.basic_unit import BasicUnit
from units.unit_mechanic.health_bar import HealthBar
from units.unit_resource.stash import Stash
from random import randint
from floating_text.combat_text_resolver import CombatTextResolver
from floating_text.damage_text import DamageText

# Init: Damage Text, CombatTextResolver
damage_text = DamageText()
combat_text_resolver = CombatTextResolver()


class Boss(BasicUnit, MeleeFighter):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, health_bar_x, health_bar_y):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        MeleeFighter.__init__(self)
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        self.stash = Stash(healing_potions=round(self.level / 5), mana_potions=0, gold=0)
        # Bandit Loot
        self.looted_status = False
        self.try_to_consume_health_potion = False
        self.loot_pool = LootPool()

    def update_try_to_consume_health_potion(self):
        self.try_to_consume_health_potion = True

    def has_tried_to_consume_health_potion(self):
        return self.try_to_consume_health_potion is False

    def is_looted(self):
        if self.looted_status:
            return True
        return False

    def update_looted_status(self):
        self.looted_status = True

    def attack(self, target, damage_text_group):
        # Get Damage, Message, Color for current Attack
        output_damage, output_message = self.cast_attack(self)

        # Activates Attack Animation: Bandit -> MeleeFighter
        self.melee_attack()

        # Activates Blocked Animation on Target
        if 'Blocked' in output_message:
            target.block()

        if 'Miss' in output_message:
            # Todo: Get miss animation
            target.block()

        # Activates Hurt/Death Animation on Target
        else:
            if output_damage != 0:
                # Updates current Target Health
                target.reduce_health(output_damage)

                # Updates current Target Fury
                target.gain_fury(output_damage)

                # Activates Hurt Animation: Target
                target.hurt()

                # Evaluate Death: Target
                if target.is_dead():
                    target.death()

        combat_text_resolver.resolve(target, str(output_damage) + output_message, damage_text_group)
        return True

    def use_healing_potion(self, damage_text_group):
        if self.stash.has_healing_potion():
            base_health = 40
            health_interval = randint(0, 10)
            base_health_multiplier = (self.level * 4)
            health_recover = base_health + health_interval + base_health_multiplier

            self.stash.consume_healing_potion()
            self.gain_health(health_recover)

            damage_text.heal(self, str(health_recover), damage_text_group)
            return True

        damage_text.warning(self, 'No Healing Potions', damage_text_group)
        return False