from random import randint
from units.unit_class.mage.mage_fighter import MageFighter
from units.unit_mechanic.utils import get_alive_targets
from floating_text.combat_text_resolver import CombatTextResolver
from floating_text.damage_text import DamageText

# Init: Damage Text
combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


class DamageSpells(MageFighter):
    def cast_aoe_spell(self, caster, basic_spell_attributes, target_list, damage_text_group):
        for count, target_unit in enumerate(target_list):

            # Basic Spell Attributes: minimum, maximum, multiplier
            base_damage = randint(basic_spell_attributes[0], basic_spell_attributes[1])
            base_multiplier = basic_spell_attributes[2]

            output_damage, output_message = \
                self.cast_spell(caster.magic, base_damage, base_multiplier)

            if target_unit.alive:
                target_unit.reduce_health(output_damage)
                target_unit.hurt()

                if target_unit.is_dead():
                    target_unit.death()

            combat_text_resolver.resolve(target_unit, str(output_damage) + output_message, damage_text_group)

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

