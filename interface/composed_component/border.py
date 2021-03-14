import sys
import pygame as pg

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pg.Surface((2, 2))                                   # tiny! 2x2 bitmap
    pg.draw.line(colour_rect, left_colour,  (0, 0), (0, 1))            # left colour line
    pg.draw.line(colour_rect, right_colour, (1, 0), (1 ,1))            # right colour line
    colour_rect = pg.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
    window.blit(colour_rect, target_rect)                                    # paint it

pg.init()
screen = pg.display.set_mode((1000, 1000))
screen_rect = screen.get_rect()


# rect = pg.Rect(0, 0, 100, 300)
# rect.center = screen_rect.center
# pg.draw.rect(screen, pg.Color("tomato"), rect, 8)
# pg.display.flip()
# #gradientRect(screen, (0, 255, 0), (0, 100, 0), pg.Rect(100, 100, 100, 50))
# gradientRect(screen, pg.Color("grey"), pg.Color("white"), pg.Rect(200, 100, 101, 300))
# pg.display.flip()

w, h = pg.display.get_surface().get_size()
rect = pg.Rect(0, 0, w-6, 300)
rect.center = screen_rect.center
pg.draw.rect(screen, pg.Color("tomato"), rect, 8)
pg.display.flip()
#gradientRect(screen, (0, 255, 0), (0, 100, 0), pg.Rect(100, 100, 100, 50))
gradientRect(screen, pg.Color("lightblue"), pg.Color("darkblue"), pg.Rect(5, h/2 + 190, w-10, 300))
pg.display.flip()

while pg.event.poll().type != pg.QUIT:
    pass

pg.quit()
sys.exit()
