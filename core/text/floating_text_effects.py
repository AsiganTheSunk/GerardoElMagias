from pygame import init, sprite, transform, time, display, Color, Surface, SRCALPHA, BLEND_RGBA_MULT
from math import sin, cos, radians


init()


class FloatingTextEffects(sprite.Sprite):
    def __init__(self, x, y, animation_type):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.animation_type = animation_type
        self.update_time = time.get_ticks()
        self.counter = 0
        self.fade_out_counter = 0
        self.theta = 180

    def update(self):
        if self.animation_type == 'move_down':
            self.move_down()
        elif self.animation_type == 'move_up':
            self.move_up()
        elif self.animation_type == 'move_up_diagonal_left':
            self.move_up()
        elif self.animation_type == 'move_up_diagonal_right':
            self.move_up()
        elif self.animation_type == 'mover_arc_right':
            pass
        elif self.animation_type == 'mover_arc_left':
            pass

    def move_up_diagonal_left(self):
        # move damage text up
        self.rect.y += 1
        self.rect.x -= 1
        # delete after counter
        self.counter += 1
        fade_out_counter = 0
        if self.counter > 60:
            self.kill()

        if self.counter > 20:
            self.fade_out_counter += 6
            self.image.set_alpha(300 - self.fade_out_counter)

    def move_up_diagonal_right(self):
        # move damage text up
        self.rect.y += 1
        self.rect.x += 1
        # delete after counter
        self.counter += 1
        fade_out_counter = 0
        if self.counter > 60:
            self.kill()

        if self.counter > 20:
            self.fade_out_counter += 6
            self.image.set_alpha(300 - self.fade_out_counter)

    def move_up(self):
        # move damage text up
        self.rect.y -= 1
        # delete after counter
        self.counter += 1
        if self.counter > 60:
            self.kill()

        if self.counter > 20:
            self.fade_out_counter += 6
            self.image.set_alpha(300 - self.fade_out_counter)

    def move_down(self):
        # move damage text up
        self.rect.y += 1
        # delete after counter
        self.counter += 1
        fade_out_counter = 0
        if self.counter > 60:
            self.kill()

        if self.counter > 20:
            self.fade_out_counter += 6
            self.image.set_alpha(300 - self.fade_out_counter)

    def move_arc_left(self):
        # Todo: This does not work as intended, text stays static
        radius = 100
        print(radius * cos(radians(self.theta)), radius * sin(radians(self.theta)))
        self.rect.x += radius * cos(radians(self.theta))
        self.rect.y -= radius * sin(radians(self.theta))

        # delete after counter
        self.theta += 100
        self.counter += 1
        if self.counter > 60:
            self.kill()

        if self.counter > 20:
            self.fade_out_counter += 6
            self.image.set_alpha(300 - self.fade_out_counter)

    def move_arc_right(self):
        pass
