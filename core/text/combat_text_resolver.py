from core.text.damage_text import DamageText
from core.units.combat.combat_type_resolution import CombatTypeResolution

# Init: Damage Text
damage_text = DamageText()


class CombatTextResolver:
    @staticmethod
    def resolve(target, output_damage, output_type, damage_text_group):
        if output_type is CombatTypeResolution.BLOCKED:
            damage_text.block(target, output_damage, damage_text_group)
        elif output_type is CombatTypeResolution.MISS:
            damage_text.miss(target, output_damage, damage_text_group)
        elif output_type is CombatTypeResolution.CRITICAL_HIT:
            damage_text.critical_hit(target, output_damage, damage_text_group)
        elif output_type is CombatTypeResolution.HIT:
            damage_text.hit(target, output_damage, damage_text_group)
