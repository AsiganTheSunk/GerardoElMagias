from floating_text.damage_text import DamageText

# Init: Damage Text
damage_text = DamageText()


class CombatTextResolver:
    @staticmethod
    def resolve(target, message, damage_text_group):
        if 'Blocked' in message:
            damage_text.block(target, message, damage_text_group)
        elif 'Miss' in message:
            damage_text.miss(target, message, damage_text_group)
        elif 'Critical' in message:
            damage_text.critical_hit(target, message, damage_text_group)
        elif 'Hit' in message:
            damage_text.hit(target, message, damage_text_group)
        elif 'Resist' in message:
            damage_text.resist(target, message, damage_text_group)
