from pygame import draw
from constants.basic_colors import *

class ManaBar:
    def __init__(self, x, y, mp, max_mp):
        self.x = x
        self.y = y
        self.mp = mp
        self.max_mp = max_mp

    def draw(self, mp, max_mp, screen):
        # update mana
        self.mp = mp
        self.max_mp = max_mp
        ratio = self.mp / self.max_mp
        draw.rect(screen, GRAY_COLOR, (self.x, self.y, 140, 20))
        draw.rect(screen, BLUE_COLOR, (self.x, self.y, 140 * ratio, 20))
