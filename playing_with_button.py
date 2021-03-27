from interface.basic_components.basic_button import BasicButton
from constants.basic_images import ultimate_image

import pygame
import sys


# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('quit', True, color)

print(type(ultimate_image))
basic_button = BasicButton(screen, 100, 100, ultimate_image, 50, 50, 'Ultimate', text_color=pygame.Color('White'))
while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    #
    #         # checks if a mouse is clicked
    #     if ev.type == pygame.MOUSEBUTTONDOWN:
    #
    #         # if the mouse is clicked on the
    #         # button the game is terminated
    #         if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
    #             pygame.quit()
    #
    #             # fills the screen with a color
    screen.fill((60, 25, 60))

    basic_button.display(True)
    basic_button.is_hover()
    # basic_button.click_animation()
    if basic_button.is_mouse_clicked():
        print('Clicked')

    # # stores the (x,y) coordinates into
    # # the variable as a tuple
    # mouse = pygame.mouse.get_pos()
    #
    # # if mouse is hovered on a button it
    # # changes to lighter shade
    # if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
    #     pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
    #
    # else:
    #     pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
    #
    #     # superimposing the text onto our button
    # screen.blit(text, (width / 2 + 50, height / 2))

    # updates the frames of the game
    pygame.display.update()


# import sys
# import pygame as pg
#
#
# RED_HIGHLIGHT = (240, 50, 50, 100)
#
# pg.init()
# clock = pg.time.Clock()
# screen = pg.display.set_mode((500,500))
# screen_rect = screen.get_rect()
#
# see_through = pg.Surface((100,100)).convert_alpha()
# see_through.fill(RED_HIGHLIGHT)
# see_through_rect = see_through.get_rect(bottomleft=screen_rect.center)
#
#
# while pg.event.poll().type != pg.QUIT:
#     pg.draw.circle(screen, pg.Color("cyan"), screen_rect.center, 50)
#     screen.blit(see_through, see_through_rect)
#     pg.display.update()
#     clock.tick(60)
#
# pg.quit()
# sys.exit()