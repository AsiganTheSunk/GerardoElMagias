from random import randint
from units.unit_class.mage.mage_fighter import MageFighter
from floating_text.damage_text import DamageText
from constants.basic_colors import *


# Init: Damage Text
damage_text = DamageText()


class HealingSpells(MageFighter):
    def cast_heal(self, caster, damage_text_group):
        # Todo: Init proper 150x, 400y
        damage_text.cast(caster, "Heal", damage_text_group)

        base_heal = 1 + randint(0, 10) + (caster.magic * 5)
        if caster.max_hp - caster.current_hp > base_heal:
            heal_amount = base_heal
        else:
            heal_amount = caster.max_hp - caster.current_hp
        caster.current_hp += heal_amount

        # Todo: Init proper 150x, 500y
        damage_text.heal(caster, str(heal_amount) + " Heal ", damage_text_group)
