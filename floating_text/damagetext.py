from pygame import init, sprite
from constants.basic_fonts import combat_font

init()


class DamageText(sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        sprite.Sprite.__init__(self)
        self.image = combat_font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        # move damage text up
        self.rect.y -= 1
        # delete after counter
        self.counter += 1
        if self.counter > 50:
            self.kill()