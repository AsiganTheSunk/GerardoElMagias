#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import display
from interface.elements.ui_layout import UILayout

from interface.composed_elements.player_interface_panel import PlayerInterfacePanel
from interface.composed_elements.player_interface_text import PlayerInterfaceText
from core.game.stage.stage_background_selector import StageBackgroundSelector
from core.game.stage.render.stage_unit_effects_renderer import StageUnitEffectsRenderer


class StageRenderer(PlayerInterfacePanel, PlayerInterfaceText, StageBackgroundSelector, StageUnitEffectsRenderer):
    def __init__(self, surface, width, height, panel_width, panel_height, clock, fps, animation_master):
        StageBackgroundSelector.__init__(self, surface)
        StageUnitEffectsRenderer.__init__(self, animation_master)
        PlayerInterfacePanel.__init__(self, surface, width, height, panel_width, panel_height)
        PlayerInterfaceText.__init__(self, surface, width, height, panel_width, panel_height)
        self.clock = clock
        self.fps = fps

    @staticmethod
    def display_caption():
        display.set_caption("Las Trepidantes Aventuras de Gerardo EL MAGIAS")

    def display_victory(self):
        self.display_victory_banner()
        self.display_victory_message()

    def display_defeat(self):
        self.display_defeat_banner()
        self.display_defeat_message()

    def update(self, level, hero, enemy_list, scripted_battle, text_sprite, battle_master):
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
        text_sprite.update()
        text_sprite.draw(self.surface)

        # draw units
        battle_master.stage_unit_renderer.render_units()

        # draw effects: in front of units
        self.update_effects()

        self.render_ui_elements(self.ui_elements)

    def render_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    self.surface.blit(ui_element.image, (ui_element.rect.x, ui_element.rect.y))