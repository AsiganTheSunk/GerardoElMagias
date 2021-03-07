import pygame
import os

class Puff(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        try:
            self.imagePuff = pygame.image.load(os.path.join("Images", "puff.tga")).convert()
        except:
            raise (UserWarning, "Unable to find Puff image")
        self.imagePuff.set_colorkey((0,0,255))

        self.image = self.imagePuff
        self.rect = self.image.get_rect()
        self.x = self.screen.get_width()/3
        self.y = self.screen.get_height()/3+10
        self.rect.center = (self.x, self.y)

        self.lifespan = 60
        self.speed = 1
        self.count = 0
        self.angle = 0

    def update(self):
        self.calcPos()
        self.rect.center = self.x, self.y
        self.transform()
        if self.count > self.lifespan:
            self.kill()

    def calcPos(self):
        self.x -= 5
        self.y = self.y

    def transform(self):
        self.count += 1.1
        self.angle += self.count*25
        self.newTrans = pygame.transform.scale(self.copyImage, (400,400))
        self.newRect = self.newTrans.get_rect()
        self.newRect.center = self.rect.center