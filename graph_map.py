import pygame
from pygame import Color
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN_GRASS = (104, 159, 56)
RED = (255, 0, 0)
TEXTCOLOR = (0, 0, 0)
(width, height) = (500, 500)

running = True

from graph_generator import MapGraphGenerator

stage_list = ['Shop', 'Forest', 'Castle']

map_graph_generator = MapGraphGenerator()
list_of_nodes = map_graph_generator.generate_main_map(stage_list)

# for index, item in enumerate(list_of_nodes):
#     print('Index:', index, 'Current Node:', item.name)
#     if item.previous_node is not None:
#         print('Previous Node:', item.previous_node.name)
#     if item.next_node is not None:
#         print('Next Node:', item.next_node.name)
#     if item.right_alternative_path_node is not None:
#         print('Alt. Right Node:', item.right_alternative_path_node.name)
#         if item.right_alternative_path_node.previous_node is not None:
#             print('Alt. Right Previous Node:', item.right_alternative_path_node.previous_node.name)
#         if item.right_alternative_path_node.next_node is not None:
#             print('Alt. Right Next Node:', item.right_alternative_path_node.next_node.name)
#         if item.right_alternative_path_node.dungeon_node is not None:
#             print('Dungeon Alt. Node:', item.right_alternative_path_node.dungeon_node.name)
#             if item.right_alternative_path_node.dungeon_node.next_node is not None:
#                 print('Alt. Shop Portal Node:', item.right_alternative_path_node.dungeon_node.next_node.name)
#     if item.dungeon_node is not None:
#         print('Dungeon Node:', item.dungeon_node.name)
#         if item.dungeon_node.next_node is not None:
#             print('Shop Portal Node:', item.dungeon_node.next_node.name)
#     print('-------' * 8)


class MapGraphNavigator:
    def __init__(self):
        pass


class MapGraphDrawer:
    def __init__(self):
        self.draw_node_list = []

    def display_node(self, screen, node_map):
        starting_pos_x = 40
        starting_pos_y = 40
        for index, item in enumerate(node_map):
            print('Index:', index, 'Current Node:', item.name)

            if item.previous_node is not None:
                print('Previous Node:', item.previous_node.name)
            if item.next_node is not None:
                print('Next Node:', item.next_node.name)
            pygame.draw.circle(screen, BLUE, (starting_pos_x, starting_pos_y), 20)
            pygame.display.update()
            starting_pos_x = starting_pos_x * 2
            starting_pos_y = starting_pos_y * 2
        pass

    # def addRect(self):
    #     self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
    #     pygame.display.update()
    #
    # def addText(self):
    #     self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
    #     pygame.display.update()


def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TUFF")
    screen.fill(GREEN_GRASS)
    pygame.display.update()

    map_drawer = MapGraphDrawer()
    map_drawer.display_node(screen, list_of_nodes)
    while running:

        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                drawCircle()
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle():
    pos=getPos()
    pygame.draw.circle(screen, BLUE, pos, 20)


if __name__ == '__main__':
    main()