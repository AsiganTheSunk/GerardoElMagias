#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import display
from interface.elements.ui_layout import UILayout

from interface.composed_elements.player_interface_panel import PlayerInterfacePanel
from interface.composed_elements.player_interface_text import PlayerUITextStageInformation
from core.game.stage.stage_background_selector import StageBackgroundSelector
from core.game.stage.render.stage_unit_effects_renderer import StageUnitEffectsRenderer
from interface.elements.ui_text_element import UITextElement


# game_attributes.surface, game_attributes.screen_width, game_attributes.screen_height, 0, game_attributes.panel_height, game_attributes.clock, game_attributes.fps, animation_master

class StageRenderer(PlayerInterfacePanel, PlayerUITextStageInformation, StageBackgroundSelector, StageUnitEffectsRenderer):
    def __init__(self, battle_master, game_attributes, animation_master):
        self.battle_master = battle_master
        self.game_attributes = game_attributes
        self.animation_master = animation_master

        StageBackgroundSelector.__init__(self, game_attributes.surface)
        StageUnitEffectsRenderer.__init__(self, animation_master)
        PlayerUITextStageInformation.__init__(self, battle_master, game_attributes)

        PlayerInterfacePanel.__init__(self, game_attributes.surface,
                                      game_attributes.screen_width, game_attributes.screen_height,
                                      0, game_attributes.panel_height)

        self.clock = self.game_attributes.clock
        self.fps = self.game_attributes.fps

    @staticmethod
    def display_caption():
        display.set_caption("Las Trepidantes Aventuras de Gerardo EL MAGIAS")

    def display_victory(self):
        self.display_victory_banner()
        # self.display_victory_message()

    def display_defeat(self):
        self.display_defeat_banner()
        # self.display_defeat_message()

    def update(self, level, hero, enemy_list, scripted_battle, text_sprite, battle_master):
        self.clock.tick(self.fps)

        # draw backgrounds
        self.set_stage_background(level)
        self.display_panel_background()
        # draw panel

        # self.display_player_information(level, hero)
        # self.display_player_bottom_panel_information(hero)
        #
        # self.display_enemy_bottom_panel_information(scripted_battle, enemy_list)
        self.display_gold_icon()

        # damage text
        text_sprite.update()
        text_sprite.draw(self.surface)

        # draw units
        battle_master.stage_unit_renderer.render_units()

        # draw effects: in front of units
        self.update_effects()

        self.render_text_ui_elements(self.player_ui_text_stage_information_elements)
        self.render_ui_elements(self.ui_elements)

    def render_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    print(type(ui_element))
                    if type(ui_element) is UITextElement:
                        print("entra aqui")
                        ui_surface_element, ui_element_position = ui_element.render()
                        self.surface.blit(ui_surface_element, ui_element_position)
                    else:
                        print('entra aqui')
                        self.surface.blit(ui_element.image, (ui_element.rect.x, ui_element.rect.y))

    def render_text_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    ui_surface_element, ui_element_position = ui_element.render()
                    self.surface.blit(ui_surface_element, ui_element_position)
