from pygame import font, mouse, init, draw, display, Color, time
init()

from graph_generator import MapGraphGenerator, BasicNodeProperties
from stage_map_navigator import MapGraphNavigator, MapGraphDrawer

# https://stackoverflow.com/questions/19117062/how-to-add-text-into-a-pygame-rectangle
# https://stackoverflow.com/questions/32909847/line-styles-in-pygame

main_line_forest = [
    BasicNodeProperties(1, 5, [], ['Bandit'], []),
    BasicNodeProperties(2, 6, [5], ['Bandit'], ['Chief Bandit']),
    BasicNodeProperties(3, 4, [1, 3], ['Bandit'], ['Chief Bandit', 'Djinn']),
]

main_line_castle = [
    BasicNodeProperties(1, 5, [], ['Esqueleteiro'], []),
    BasicNodeProperties(2, 6, [5], ['Esqueleteiro'], ['Chief Esqueleteiro']),
    BasicNodeProperties(3, 4, [1, 3], ['Esqueleteiro'], ['Chief Esqueleteiro', 'Djinn']),
]

map_generator = MapGraphGenerator()
normal_world = map_generator.generate_world_map(['Forest', 'Castle'], [main_line_forest, main_line_castle])
list_of_nodes = ['Forest', 'Castle', 'Desert', 'Tombs']


def main():
    running = True
    # Define Game Fonts:
    tahoma_font_path = './resources/fonts/Tahoma.ttf'
    interface_font = font.Font(tahoma_font_path, 15)
    interface_font.set_bold(True)
    display.set_caption("TUFF")

    screen = display.set_mode((1280, 720))
    screen.fill(Color('DarkOliveGreen4'))
    display.update()
    clock = time.Clock()

    map_graph_navigator = MapGraphNavigator(screen)
    map_graph_navigator.map_drawer.generate_node_pos(list_of_nodes)

    while running:
        map_graph_navigator.display()
        map_graph_navigator.stage_node_mouse_over()
        map_graph_navigator.stage_node_header_information()
        map_graph_navigator.navigate()

        clock.tick(60)
        display.update()


if __name__ == '__main__':
    main()
