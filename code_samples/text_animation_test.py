import pygame as pg
from constants.basic_fonts import combat_text_font

def main():
    clock = pg.time.Clock()
    screen = pg.display.set_mode((640, 480))
    font = combat_text_font
    blue = pg.Color('royalblue')
    orig_surf = font.render('Enter your text', True, blue)
    txt_surf = orig_surf.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        if alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            alpha = max(alpha-4, 0)
            txt_surf = orig_surf.copy()  # Don't modify the original text surf.
            # Fill alpha_surf with this color to set its alpha value.
            alpha_surf.fill((255, 255, 255, alpha))
            # To make the text surface transparent, blit the transparent
            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

        screen.fill((30, 30, 100))
        screen.blit(txt_surf, (110, 100))
        pg.display.flip()
        clock.tick(30)

main()