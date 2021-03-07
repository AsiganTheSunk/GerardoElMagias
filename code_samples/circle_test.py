import pygame as pg
from pygame.math import Vector2


class Agent(pg.sprite.Sprite):
    def __init__(self, pos, *groups):
        super(Agent, self).__init__(*groups)
        self.radius = 25
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        pg.draw.circle(self.image, pg.Color('dodgerblue4'),
                       (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 0
        self.angular_speed = 0
        self.pos = Vector2(pos)
        # If you add this vector to the center pos, you get a point
        # on the circumference of the circle.
        self.front = Vector2(0, -self.radius)  # Pointing upward.
        # Just rotate the front vector by -90 and 90 degrees to get
        # the left and right vectors. `rotate` returns a new vector.
        self.left = self.front.rotate(-90)
        self.right = self.front.rotate(90)

    def update(self):
        # Use the front vector as the velocity.
        self.pos += self.front.normalize() * self.speed
        self.rect.center = self.pos

        if self.angular_speed != 0:
            self.rotate()

    def rotate(self):
        """Rotate the front vector and use it to update the other two."""
        self.front.rotate_ip(self.angular_speed)
        self.left = self.front.rotate(-90)
        self.right = self.front.rotate(90)

    def draw_vectors(self, screen):
        """Draw the three vectors."""
        pg.draw.circle(screen, (0, 240, 50), list(map(int, self.pos+self.front)), 3)
        pg.draw.circle(screen, (240, 0, 50), list(map(int, self.pos+self.left)), 3)
        pg.draw.circle(screen, (240, 240, 0), list(map(int, self.pos+self.right)), 3)
        pg.draw.line(screen, (0, 240, 50), self.pos, self.pos+self.front, 2)
        pg.draw.line(screen, (240, 0, 50), self.pos, self.pos+self.left, 2)
        pg.draw.line(screen, (240, 240, 0), self.pos, self.pos+self.right, 2)


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    agent = Agent((100, 300), all_sprites)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    agent.speed = 5
                elif event.key == pg.K_a:
                    agent.angular_speed = -10
                elif event.key == pg.K_d:
                    agent.angular_speed = 10
            elif event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    agent.speed = 0
                elif event.key == pg.K_a:
                    agent.angular_speed = 0
                elif event.key == pg.K_d:
                    agent.angular_speed = 0

        all_sprites.update()

        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        agent.draw_vectors(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()