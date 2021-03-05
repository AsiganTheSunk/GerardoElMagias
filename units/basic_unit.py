from units.unit_animation import UnitAnimation


class BasicUnit:
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic):

        # Basic Unit Coordinates x,y
        self.x = x
        self.y = y

        # Basic Unit Name
        self.name = name

        # Basic Unit Stats
        self.level = level
        self.max_fury = 100
        self.current_fury = 0
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mp = max_mp
        self.current_mp = self.max_mp
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.intellect = 1

        # Basic Unit Status
        self.alive = True

        self.unit_animation = UnitAnimation(self.x, self.y, self.name)

    def death(self):
        self.current_hp = 0
        self.alive = False
        self.unit_animation.death_animation()

    def hurt(self):
        self.unit_animation.hurt_animation()

    def dodge(self):
        self.unit_animation.dodge_animation()

    def idle(self):
        self.unit_animation.idle_animation()

    def update(self):
        self.unit_animation.update()

    def draw(self, screen):
        self.unit_animation.draw(screen)