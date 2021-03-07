from units.unit_class.melee.melee_figher import MeleeFighter
from units.unit_mechanic.loot_pool import LootPool
from units.basic_unit import BasicUnit
from units.unit_mechanic.health_bar import HealthBar
from floating_text.combat_text_types import CombatTextTypes


class Bandit(BasicUnit, MeleeFighter):
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic, health_bar_x, health_bar_y):
        BasicUnit.__init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic)
        MeleeFighter.__init__(self)
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.current_hp, self.max_hp)
        # Bandit Loot
        self.looted_status = False
        self.loot_pool = LootPool()

    def is_looted(self):
        if self.looted_status:
            return True
        return False

    def update_looted_status(self):
        self.looted_status = True

    def attack(self, target, damage_text_group):
        # Get Damage, Message, Color for current Attack
        output_damage, output_message, output_color = self.cast_attack(self)

        # Activates Attack Animation: Bandit -> MeleeFighter
        self.unit_animation.melee_attack_animation()

        # Activates Blocked Animation on Target
        if 'BLOCKED !' in output_message:
            target.unit_animation.block_animation()

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

        if ' Critical ' in output_message:
            floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
            floating_text.critical_combat_text(str(output_damage) + output_message, output_color)
            damage_text_group.add(floating_text)

        else:
            floating_text = CombatTextTypes(target.unit_animation.rect.centerx, target.unit_animation.rect.y, 'move_up')
            floating_text.combat_text(str(output_damage) + output_message, output_color)
            damage_text_group.add(floating_text)
        return True
