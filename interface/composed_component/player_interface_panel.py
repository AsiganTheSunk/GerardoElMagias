from interface.basic_components.button import Button
from constants.basic_images import skull_image, spellbook_image, \
    health_potion_image, mana_potion_image, restart_image, ultimate_image, next_button_image, gold_image, \
    background_forest, background_castle, panel_image

from constants.basic_colors import YELLOW_COLOR, WHITE_COLOR, RED_COLOR
from constants.basic_fonts import default_font
import pygame as pg
# (self, surface, x, y, image, size_x, size_y)


class PlayerInterfacePanel:
    def __init__(self, surface, width, height, panel_width, panel_height):
        self.surface = surface
        self.width = width
        self.height = height
        self.panel_width = panel_width
        self.panel_height = panel_height

        # Consumable Buttons:
        self.health_potion_button = \
            Button(self.surface, 0, self.height - self.panel_height + 150, health_potion_image, 64, 64)
        self.mana_potion_button = \
            Button(self.surface, 85, self.height - self.panel_height + 150, mana_potion_image, 60, 60)

        # SpellBook Button:
        self.spell_book_button = Button(self.surface, 0, 695, spellbook_image, 100, 100)

        # Skill Buttons:
        self.ultimate_button = Button(self.surface, 400, 120, ultimate_image, 100, 100)

        # Kill All Button:
        self.kill_all_button = Button(self.surface, 40, 260, skull_image, 60, 60)

        # Mouse Pointer:
        # self.mouse_pointer =

        self.next_button = Button(self.surface, 800, 10, next_button_image, 80, 80)

        # Gold Icon:
        self.surface.blit(gold_image, (20, 20))

        # Panel Background
        self.panel_background_image = panel_image

    def display_mana_potion(self):
        return self.mana_potion_button.draw()

    def display_health_potion(self):
        return self.health_potion_button.draw()

    def display_spell_book(self):
        # SpellBook Button:
        return self.spell_book_button.draw()

    def display_kill_all(self):
        # Kill All Button:
        return self.kill_all_button.draw()

    @staticmethod
    def gradientRect(window, left_colour, right_colour, target_rect):
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        colour_rect = pg.Surface((2, 2))  # tiny! 2x2 bitmap
        pg.draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
        pg.draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
        colour_rect = pg.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
        window.blit(colour_rect, target_rect)  # paint it

    def display_panel_background(self):
        w, h = pg.display.get_surface().get_size()
        self.gradientRect(self.surface, pg.Color("SteelBlue"), pg.Color("RoyalBlue"), pg.Rect(2, h / 2 + self.panel_height, w-4, self.panel_height))

        rect = pg.Rect(1, h / 2 + self.panel_height + 1, w-2, self.panel_height)
        pg.draw.rect(self.surface, pg.Color("DimGray"), rect, 3)

        rect = pg.Rect(1, h / 2 + self.panel_height + 1, w/6, self.panel_height)
        pg.draw.rect(self.surface, pg.Color("DimGray"), rect, 3)

        rect = pg.Rect(w - w/2+2, h / 2 + self.panel_height + 1, w - w/2, self.panel_height)
        pg.draw.rect(self.surface, pg.Color("DimGray"), rect, 3)

        rect = pg.Rect(w - w/2+2, h / 2 + self.panel_height + 1, w - w/2, self.panel_height)
        pg.draw.rect(self.surface, pg.Color("Black"), rect, 1)

        rect = pg.Rect(1, h / 2 + self.panel_height + 1, w/6, self.panel_height)
        pg.draw.rect(self.surface, pg.Color("Black"), rect, 1)

        rect = pg.Rect(1, h / 2 + self.panel_height + 1, w-2, self.panel_height)
        pg.draw.rect(self.surface, pg.Color("Black"), rect, 1)


class StageBackground:
    def __init__(self, surface):
        self.surface = surface

        self.forest_background_image = background_forest
        self.forest_background = None

        self.castle_background_image = background_castle
        self.castle_background = None

    def set_stage_background(self, level):
        # draw backgrounds
        if level <= 7:
            self.surface.blit(self.forest_background_image, (0, 0))
        if level > 7:
            self.surface.blit(self.castle_background_image, (0, 0))


class PlayerInterfaceText:
    def __init__(self, surface, width, height, panel_width, panel_height):
        self.surface = surface
        self.width = width
        self.height = height
        self.panel_width = panel_width
        self.panel_height = panel_height

    # create function for drawing text
    def display_text(self, text, font, color, x, y):
        font_surface = font.render(text, True, color)
        self.surface.blit(font_surface, (x, y))

    def display_player_information(self, player):
        self.display_text(f"{player.stash.gold}", default_font, YELLOW_COLOR, 80, 30)
        self.display_text(f"Nivel: {player.level}", default_font, WHITE_COLOR, 50, 100)
        self.display_text(f"Experiencia: [ {player.experience}/{player.exp_level_break} ]", default_font, WHITE_COLOR, 50, 125)
        self.display_text(f"Fuerza: {player.strength}", default_font, WHITE_COLOR, 50, 175)
        self.display_text(f"Agilidad: {player.dexterity}", default_font, WHITE_COLOR, 50, 200)
        self.display_text(f"Poder Mágico: {player.magic}", default_font, WHITE_COLOR, 50, 225)

    def display_stage_information(self, level):
        if level <= 7:
            self.display_text(f"THE WOODS: STAGE {level}", default_font, RED_COLOR, 310, 25)
        else:
            self.display_text(f"THE CASTLE: STAGE {level - 7}", default_font, RED_COLOR, 310, 25)

    def display_debug_information(self, _current_fighter, _total_fighters):
        self.display_text(f"Total fighters: {_total_fighters}", default_font, YELLOW_COLOR, 600, 100)
        self.display_text(f"Current fighter: {_current_fighter}", default_font, YELLOW_COLOR, 600, 125)

    def display_player_bottom_panel_information(self, player):
        # show hero stats
        self.display_text(f"  HP: {player.current_hp} / {player.max_hp}      "
                  f"MP: {player.current_mp} / {player.max_mp}",
                  default_font, WHITE_COLOR, 99, self.height - self.panel_height + 10)

        # show number of pots
        self.display_text(f"x{player.stash.healing_potions}", default_font, WHITE_COLOR, 60,
                  self.height - self.panel_height + 170)
        # show number of lightnings
        self.display_text(f"x{player.stash.mana_potions}", default_font, WHITE_COLOR, 140,
                  self.height - self.panel_height + 170)

    def display_enemy_bottom_panel_information(self, scripted_battle, level, enemy_list):
        # draw name and health of enemies
        ENEMY_TEXT_POS_0 = [480, self.height - self.panel_height + 5]
        ENEMY_TEXT_POS_1 = [480, self.height - self.panel_height + 65]
        ENEMY_TEXT_POS_2 = [700, self.height - self.panel_height + 5]
        ENEMY_TEXT_POS_3 = [700, self.height - self.panel_height + 65]

        tmp = [ENEMY_TEXT_POS_0, ENEMY_TEXT_POS_1, ENEMY_TEXT_POS_2, ENEMY_TEXT_POS_3]

        if scripted_battle[level]:
            self.display_text(f" The Boss HP: {enemy_list[0].current_hp}",
                              default_font, WHITE_COLOR, tmp[0][0], tmp[0][1])
        else:
            for index, enemy_fighter in enumerate(enemy_list):
                self.display_text(f"{enemy_fighter.name} HP: {enemy_fighter.current_hp}",
                                  default_font, WHITE_COLOR, tmp[index][0], tmp[index][1])
