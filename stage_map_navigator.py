from pygame import font, init, time, key, mouse, draw, Color, Rect, event as pygame_events, MOUSEBUTTONUP, \
    QUIT, K_LEFT, K_a, K_RIGHT, K_d, K_SPACE, K_RETURN, display


class MapGraphDrawer:
    def __init__(self, surface):
        self.surface = surface
        self.draw_node_list = []
        self.node_pos_list = []

    def draw_circle(self):
        draw.circle(self.surface, Color('Blue'), mouse.get_pos(), 20)

    def display_selector(self):
        starting_pos_x = 100
        step = 120
        starting_pos_y = 250
        draw.circle(self.surface, Color('Red'), (starting_pos_x, starting_pos_y), 25)

    def create_node(self, x, y):
        return Rect(x, y, 20, 20)

    def generate_node_pos(self, node_map):
        starting_pos_x = 100
        step = 120
        starting_pos_y = 250
        for _ in node_map:
            self.node_pos_list.append((starting_pos_x, starting_pos_y))
            starting_pos_x += step

    def display_node(self):
        self.draw_node_list = []
        previous = None
        for index, item in enumerate(self.node_pos_list):
            x, y = item
            new_node = self.create_node(x, y)
            self.draw_node_list.append(new_node)
            draw.rect(self.surface, Color('LightBlue'), new_node)

            if previous is not None:
                draw.line(self.surface, Color('LightBlue'), previous.center, new_node.center, 2)
            previous = new_node

    def check_click(self):
        for item in self.draw_node_list:
            if item.collidepoint(mouse.get_pos()):
                return item


def debounce_time(last_updated, interval=600):
    return time.get_ticks() - last_updated >= interval


list_of_nodes = ['Forest', 'Castle', 'Desert', 'Tombs']


class MapGraphNavigator:
    def __init__(self, surface):
        self.map_font_path = './resources/fonts/Tahoma.ttf'
        self.map_font = font.Font(self.map_font_path, 15)
        self.map_font.set_bold(True)
        self.last_updated = 0
        self.rect = Rect(100, 250, 20, 20)
        self.surface = surface

        self.map_drawer = MapGraphDrawer(surface)

    def navigate(self):
        keys = key.get_pressed()
        ev = pygame_events.get()
        for event in ev:
            if event.type == MOUSEBUTTONUP:
                data = self.map_drawer.check_click()
                if data is not None:
                    self.rect.x = data.x

            if event.type == QUIT:
                running = False

        if (keys[K_a] or keys[K_LEFT]) and debounce_time(self.last_updated):  # to move left
            self.rect.x -= 120
            if self.rect.x < 100:
                self.rect.x = 100
            self.last_updated = time.get_ticks()

        if (keys[K_d] or keys[K_RIGHT]) and debounce_time(self.last_updated):
            # to move right
            self.rect.x += 120
            if self.rect.x > 340:
                self.rect.x = 340
            self.last_updated = time.get_ticks()

        if (keys[K_SPACE] or keys[K_RETURN]) and debounce_time(self.last_updated):
            # to move right
            # print('Entering', '[ ' + list_of_nodes[index_to_draw].name + ' ]', '....')
            print('Entering', '[ Stage ]', '....')
            self.last_updated = time.get_ticks()

    def display(self):
        self.map_drawer.display_node()
        draw.rect(self.surface, (250, 100, 20), self.rect)

    def stage_node_mouse_over(self):
        data = self.map_drawer.check_click()
        if data is not None:
            rect_hover = Rect(data.x, data.y, 20, 20)
            draw.rect(self.surface, (100, 100, 20), rect_hover)

    def stage_node_header_information(self):
        data = self.map_drawer.check_click()
        index_to_draw = -1
        for index, item in enumerate(self.map_drawer.draw_node_list):
            if data is not None:
                if item.x == data.x:
                    index_to_draw = index
            elif self.rect.x == item.x:
                index_to_draw = index

        if index_to_draw != -1:
            # screen.blit(self.map_font.render('[ ' + list_of_nodes[index_to_draw].name + ' ]', True, (255, 0, 0)), (200, 100))
            self.surface.blit(self.map_font.render('[ Stage ]', True, (255, 0, 0)), (200, 100))
            display.update()
    #
    # def navigate(self):
    #     ev = pygame.event.get()
    #     self.map_drawer.display_node(screen)
