#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import display
from interface.composed_components.spell_book import UILayout

from interface.composed_components.player_interface_panel import PlayerInterfacePanel
from interface.composed_components.player_interface_text import PlayerInterfaceText
from interface.stage_background import StageBackground


class StageDrawer(PlayerInterfacePanel, PlayerInterfaceText, StageBackground):
    def __init__(self, surface, width, height, panel_width, panel_height, clock, fps):
        StageBackground.__init__(self, surface)
        PlayerInterfacePanel.__init__(self, surface, width, height, panel_width, panel_height)
        PlayerInterfaceText.__init__(self, surface, width, height, panel_width, panel_height)
        self.clock = clock
        self.fps = fps

    def display_caption(self):
        display.set_caption("Las Trepidantes Aventuras de Gerardo EL MAGIAS")

    def display_victory(self):
        self.display_victory_banner()
        self.display_victory_message()

    def display_defeat(self):
        self.display_defeat_banner()
        self.display_defeat_message()

    def update(self, level, hero, enemy_list, scripted_battle, damage_text_group):
        self.clock.tick(self.fps)

        # draw backgrounds
        self.set_stage_background(level)
        self.display_panel_background()
        # draw panel
        self.display_player_information(level, hero)
        self.display_player_bottom_panel_information(hero)

        self.display_enemy_bottom_panel_information(scripted_battle, enemy_list)
        self.display_gold_icon()

        # damage text
        damage_text_group.update()
        damage_text_group.draw(self.surface)

        # draw fighters
        hero.animation_set.update()
        hero.animation_set.draw()
        hero.health_bar.draw(hero.current_hp, hero.max_hp, self.surface)
        hero.mana_bar.draw(hero.current_mp, hero.max_mp, self.surface)
        hero.fury_bar.draw(hero.current_fury, hero.max_fury, self.surface)

        for unit in enemy_list:
            unit.animation_set.update()
            unit.animation_set.draw()
            unit.health_bar.draw(unit.current_hp, unit.max_hp, self.surface)

        self.render_ui_elements(self.ui_elements)

    def render_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    self.surface.blit(ui_element.image, (ui_element.rect.x, ui_element.rect.y))