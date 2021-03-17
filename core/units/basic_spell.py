class BasicSpell:
    def __init__(self, caster, target, name):
        if caster is not None:
            # Basic Unit Target Coordinates x,y
            self.caster_x = caster.animation_set.rect.x
            self.caster_y = caster.animation_set.rect.y

        # Basic Unit Target Coordinates x,y
        self.target_x = target.animation_set.rect.x
        self.target_y = target.animation_set.rect.y

        # Basic Unit Name
        self.name = name
