#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import font, mouse, init, draw, display, Color, time, event as pygame_event, QUIT, key
init()

from graph_generator import MapGraphGenerator, BasicNodeProperties
from stage_map_navigator import MapGraphNavigator, MapGraphDrawer

# https://stackoverflow.com/questions/19117062/how-to-add-text-into-a-pygame-rectangle
# https://stackoverflow.com/questions/32909847/line-styles-in-pygame

main_line_forest = [
    BasicNodeProperties(1, 5, [], ['Bandit'], []),
    BasicNodeProperties(2, 6, [5], ['Bandit'], ['Chief Bandit']),
    BasicNodeProperties(2, 8, [5], ['Bandit'], ['Chief Bandit']),
    BasicNodeProperties(3, 4, [1, 3], ['Bandit'], ['Chief Bandit', 'Djinn']),
]

main_line_castle = [
    BasicNodeProperties(1, 5, [], ['Esqueleteiro'], []),
    BasicNodeProperties(2, 6, [5], ['Esqueleteiro'], ['Chief Esqueleteiro']),
    BasicNodeProperties(3, 4, [1, 3], ['Esqueleteiro'], ['Chief Esqueleteiro', 'Djinn']),
]

map_generator = MapGraphGenerator()
full_world_map = map_generator.generate_world_map(['Forest', 'Castle'], [main_line_forest, main_line_castle])

screen = display.set_mode((1024, 576))
map_graph_navigator = MapGraphNavigator(screen, full_world_map, 0)

clock = time.Clock()
clock.tick(60)


def main():
    running = True
    # Define Game Fonts:
    tahoma_font_path = '../../../../resources/fonts/Tahoma.ttf'
    interface_font = font.Font(tahoma_font_path, 15)
    interface_font.set_bold(True)

    display.set_caption("Game Map Graph")

    screen.fill(Color('DarkOliveGreen4'))
    display.update()

    running = True

    while running:
        screen.fill(Color('DarkOliveGreen4'))
        map_graph_navigator.display()


        display.update()

        # Did the user click the window close button?
        for event in pygame_event.get():
            if event.type == QUIT:
                running = False



    # Done! Time to quit.
    quit()


if __name__ == '__main__':
    main()
