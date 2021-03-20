import pygame
from pygame import Color
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN_GRASS = (104, 159, 56)
RED = (255, 0, 0)
TEXTCOLOR = (0, 0, 0)
(width, height) = (500, 500)

running = True
from pygame import font, init, time
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

# https://stackoverflow.com/questions/19117062/how-to-add-text-into-a-pygame-rectangle
# https://stackoverflow.com/questions/32909847/line-styles-in-pygame

class MapGraphNavigator:
    def __init__(self):
        pass

class MapGraphDrawer:
    def __init__(self):
        self.draw_node_list = []
        self.node_pos_list = []

    def display_selector(self):
        starting_pos_x = 100
        step = 120
        starting_pos_y = 250
        pygame.draw.circle(screen, RED, (starting_pos_x, starting_pos_y), 25)

    def create_node(self, x, y):
        return pygame.Rect(x, y, 20, 20)

    def generate_node_pos(self, node_map):
        starting_pos_x = 100
        step = 120
        starting_pos_y = 250
        for index, item in enumerate(node_map):
            self.node_pos_list.append((starting_pos_x, starting_pos_y))
            starting_pos_x += step

    def display_node(self, screen):
        self.draw_node_list = []
        previous = None
        for index, item in enumerate(self.node_pos_list):
            x, y = item
            new_node = self.create_node(x, y)
            self.draw_node_list.append(new_node)
            pygame.draw.rect(screen, Color('LightBlue'), new_node)

            if previous is not None:
                pygame.draw.line(screen, Color('LightBlue'), previous.center, new_node.center, 2)
            previous = new_node

    def check_click(self, mouse):
        for item in self.draw_node_list:
            if item.collidepoint(mouse):
                return item


def debounce_time(last_updated, interval):
    return time.get_ticks() - last_updated >= interval


def main():
    global running, screen
    
    interval = 600
    last_updated = 0

    pygame.init()
    # Define Game Fonts:
    tahoma_font_path = './resources/fonts/Tahoma.ttf'
    interface_font = font.Font(tahoma_font_path, 15)
    interface_font.set_bold(True)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TUFF")
    screen.fill(GREEN_GRASS)
    pygame.display.update()
    clock = pygame.time.Clock()
    rect = pygame.Rect(100, 250, 20, 20)

    map_drawer = MapGraphDrawer()
    map_drawer.generate_node_pos(list_of_nodes)
    map_drawer.display_node(screen)
    while running:
        ev = pygame.event.get()
        screen.fill(GREEN_GRASS)
        map_drawer.display_node(screen)
        pygame.draw.rect(screen, (250, 100, 20), rect)

        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = get_pos_x_y()

                data = map_drawer.check_click((mouse_x, mouse_y))
                if data is not None:
                    rect.x = data.x

            if event.type == pygame.QUIT:
                running = False

        data = map_drawer.check_click(get_pos_x_y())
        if data is not None:
            rect_hover = pygame.Rect(data.x, data.y, 20, 20)
            pygame.draw.rect(screen, (100, 100, 20), rect_hover)

        index_to_draw = -1
        for index, item in enumerate(map_drawer.draw_node_list):
            if data is not None:
                if item.x == data.x:
                    index_to_draw = index
            elif rect.x == item.x:
                index_to_draw = index

        if index_to_draw != -1:
            screen.blit(interface_font.render('[ ' + list_of_nodes[index_to_draw].name + ' ]', True, (255, 0, 0)), (200, 100))
            pygame.display.update()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and debounce_time(last_updated, interval):  # to move left
            rect.x -= 120
            if rect.x < 100:
                rect.x = 100
            last_updated = time.get_ticks()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and debounce_time(last_updated, interval):
            # to move right
            rect.x += 120
            if rect.x > 340:
                rect.x = 340
            last_updated = time.get_ticks()

        if (keys[pygame.K_SPACE] or keys[pygame.K_RETURN]) and debounce_time(last_updated, interval):
            # to move right
            print('Entering', '[ ' + list_of_nodes[index_to_draw].name + ' ]', '....')
            last_updated = time.get_ticks()

        clock.tick(60)
        pygame.display.update()


def get_pos_x_y():
    pos = pygame.mouse.get_pos()
    return pos


def draw_circle():
    pos = get_pos_x_y()
    pygame.draw.circle(screen, BLUE, pos, 20)


if __name__ == '__main__':
    main()
