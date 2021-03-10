from random import randint
from core.units.combat.mage_formulas import MageFighter
from core.units.unit_mechanic.utils import get_alive_targets
from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText

# Init: Damage Text
combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


class MagicSpells(MageFighter):
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



    def cast_firestorm(self, caster, target_list, damage_text_group):
        # Basic Spell Attributes: minimum, maximum, multiplier
        basic_spell_attributes = [0, 20, 3]
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            damage_text.cast(caster, " Firestorm! ", damage_text_group)
            self.cast_aoe_spell(caster, basic_spell_attributes, alive_enemy, damage_text_group)

    def cast_lightning(self, caster, target_list, damage_text_group):
        # Basic Spell Attributes: minimum, maximum, multiplier
        basic_spell_attributes = [0, 50, 1]
        alive_enemy = get_alive_targets(target_list)

        if len(alive_enemy) > 0:
            damage_text.cast(caster, " Lightning Bolt! ", damage_text_group)
            self.cast_aoe_spell(caster, basic_spell_attributes, target_list, damage_text_group)

