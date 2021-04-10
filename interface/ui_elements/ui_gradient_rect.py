from pygame import Color, Surface, transform, draw
from interface.ui_elements.ui_element import UIElement
from interface.ui_elements.ui_rect import UIRect


class UIGradientRect(UIElement):
    def __init__(self, x, y, width, height, left_colour=Color("SteelBlue"), right_color=Color("RoyalBlue")):
        super().__init__()
        self.rect = UIRect(x, y, width, height)
        self.left_color = left_colour
        self.right_color = right_color
        self.gradient_rect = self.get_gradient_rect()

    def render(self):
        return self.gradient_rect, (self.rect.x, self.rect.y)

    def get_gradient_rect(self):
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        colour_rect = Surface((2, 2))  # tiny! 2x2 bitmap
        draw.line(colour_rect, self.left_color, (0, 0), (0, 1))  # left colour line
        draw.line(colour_rect, self.right_color, (1, 0), (1, 1))  # right colour line
        return transform.smoothscale(colour_rect, (self.rect.width, self.rect.width))
