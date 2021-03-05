from units.unit_class.melee.melee_figher import MeleeFighter
from units.unit_mechanic.loot_pool import LootPool
from units.basic_unit import BasicUnit
from units.unit_mechanic.health_bar import HealthBar
from floating_text.damagetext import DamageText


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
        output_damage, output_message, output_color = self.cast_attack(self)

        # Activates Attack Animation: Bandit -> MeleeFighter
        self.unit_animation.melee_attack_animation()

        if output_damage != 0:
            target.current_hp -= output_damage

            ###PERAS meter en funcion fury?

            fury_gained = round(output_damage*1,5)
            if fury_gained + target.current_fury >= 100:
                target.current_fury = 100
            else:
                target.current_fury += fury_gained



            # Activates Hurt Animation: Target
            target.hurt()

            if target.current_hp < 1:
                target.death()

        damage_text = DamageText(target.unit_animation.rect.centerx, target.unit_animation.rect.y, str(output_damage) + output_message, output_color)
        damage_text_group.add(damage_text)
        return True
