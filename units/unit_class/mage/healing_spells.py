from random import randint
from units.unit_class.mage.mage_fighter import MageFighter
from floating_text.damagetext import DamageText
from constants.basic_colors import *


class HealingSpells(MageFighter):
    def cast_heal(self, caster, damage_text_group):
        damage_text = DamageText(150, 400, "Heal", GREEN_COLOR)
        damage_text_group.add(damage_text)

        base_heal = 1 + randint(0, 10) + (caster.magic * 5)
        if caster.max_hp - caster.current_hp > base_heal:
            heal_amount = base_heal
        else:
            heal_amount = caster.max_hp - caster.current_hp
        caster.current_hp += heal_amount
        damage_text = DamageText(150, 500, str(heal_amount), GREEN_COLOR)
        damage_text_group.add(damage_text)


