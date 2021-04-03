#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import display, draw
from interface.ui_elements.ui_layout import UILayout
from interface.ui_elements.ui_text_element import UITextElement
from interface.composed_ui_elements.player.player_interface_panel import PlayerInterfacePanel
from interface.composed_ui_elements.player_interface_text import PlayerUITextStageInformation
from selector.stage_background_selector import StageBackgroundSelector
from core.game.stage.render.stage_unit_effects_renderer import StageUnitEffectsRenderer
from constants.game_images import skull_button_image, spell_book_button_image, kill_button_image, \
    health_potion_image, mana_potion_image, ultimate_image, next_button_image, whirlwind_image
from interface.ui_elements.ui_text_button import UITextButton
from interface.ui_elements.ui_button import UIButton
from interface.ui_elements.ui_rect import UIRect


class StageRenderer(PlayerInterfacePanel, PlayerUITextStageInformation,
                    StageBackgroundSelector, StageUnitEffectsRenderer):
    def __init__(self, battle_master, game_attributes, animation_master):
        self.battle_master = battle_master
        self.game_attributes = game_attributes
        self.animation_master = animation_master

        StageBackgroundSelector.__init__(self, game_attributes.surface)
        StageUnitEffectsRenderer.__init__(self, animation_master)
        PlayerUITextStageInformation.__init__(self, game_attributes)

        PlayerInterfacePanel.__init__(self, game_attributes.surface, game_attributes.screen_width,
                                      game_attributes.screen_height, 0, game_attributes.panel_height)

        self.clock = self.game_attributes.clock
        self.fps = self.game_attributes.fps

        self.new_button = UITextButton('new_button', 400, 655, whirlwind_image, 40, 40, text_message='hello')
        self.new_button.button.on_click(self.new_button.handle_on_click_event)
        self.add(self.new_button)

    @staticmethod
    def display_caption():
        display.set_caption("Las Trepidantes Aventuras de Gerardo EL MAGIAS")

    def display_victory(self):
        self.display_victory_banner()

    def display_defeat(self):
        self.display_defeat_banner()

    def update(self, text_sprite):
        # Setup TickRate for the Game
        self.clock.tick(self.fps)

        # draw backgrounds
        self.set_stage_background(self.battle_master.level)
        self.display_panel_background()

        # draw panel
        self.display_gold_icon()

        # damage text
        text_sprite.update()
        text_sprite.draw(self.surface)

        # draw units
        self.battle_master.stage_unit_renderer.render_units()

        # draw effects: in front of units
        self.update_effects()

        self.update_ui_text_elements(self.battle_master)
        self.new_button.update()

        self.render_ui_elements(self.ui_elements)
        self.render_ui_elements(self.ui_text_elements)

    def render_ui_elements(self, elements):
        for ui_element in elements:
            if not ui_element.hidden:
                if isinstance(ui_element, UILayout):
                    self.render_ui_elements(ui_element.elements)
                else:
                    if isinstance(ui_element, UITextElement) or isinstance(ui_element, UIButton):
                        ui_surface_element, ui_element_position = ui_element.render()
                        self.surface.blit(ui_surface_element, ui_element_position)

                    elif isinstance(ui_element, UIRect):
                        color, x, y, width, height, border_size = ui_element.render()
                        draw.rect(self.surface, color, (x, y, width, height), border_size)
                    else:
                        self.surface.blit(ui_element.image, (ui_element.rect.x, ui_element.rect.y))
