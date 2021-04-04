#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import display
from interface.composed_ui_elements.player.player_interface_panel import PlayerInterfacePanel
from interface.composed_ui_elements.player_interface_text import PlayerUITextStageInformation
from core.game.stage.selector.stage_background_selector import StageBackgroundSelector
from core.game.stage.render.stage_unit_effects_renderer import StageUnitEffectsRenderer
from interface.composed_ui_elements.player.player_bottom_panel_buttons import PlayerBottomPanelButtons
from interface.player_interface_renderer import PlayerInterfaceRenderer


class StageRenderer(PlayerUITextStageInformation,
                    StageBackgroundSelector, StageUnitEffectsRenderer, PlayerInterfaceRenderer):
    def __init__(self, battle_master, game_attributes, animation_master, sound_master):
        self.battle_master = battle_master
        self.game_attributes = game_attributes
        self.animation_master = animation_master
        self.sound_master = sound_master

        PlayerInterfaceRenderer.__init__(self, game_attributes.surface)
        StageBackgroundSelector.__init__(self, game_attributes.surface)
        StageUnitEffectsRenderer.__init__(self, animation_master)
        PlayerUITextStageInformation.__init__(self, game_attributes)

        self.player_interface_panel = PlayerInterfacePanel(game_attributes)
        self.player_bottom_panel_buttons = \
            PlayerBottomPanelButtons(self.sound_master, self.battle_master, self.game_attributes, self.add_effect)

        for ui_elements in self.player_interface_panel.elements:
            self.add(ui_elements)

        for ui_elements in self.player_bottom_panel_buttons.elements:
            self.add(ui_elements)

        self.clock = self.game_attributes.clock
        self.fps = self.game_attributes.fps

    @staticmethod
    def display_caption():
        display.set_caption("Las Trepidantes Aventuras de Gerardo EL MAGIAS")

    def display_victory(self):
        self.player_interface_panel.display_victory_banner()

    def display_defeat(self):
        self.player_interface_panel.display_defeat_banner()

    def update(self, text_sprite):
        # Setup TickRate for the Game
        self.clock.tick(self.fps)

        # draw backgrounds
        self.set_stage_background(self.battle_master.level)

        self.update_layout(self.battle_master)
        self.player_bottom_panel_buttons.update_button_elements()
        self.render_ui_elements(self.ui_elements)

        # draw units
        self.battle_master.stage_unit_renderer.render_units()

        # draw effects: in front of units
        self.update_effects()

        # damage text
        text_sprite.update()
        text_sprite.draw(self.surface)
        self.render_ui_elements(self.ui_text_elements)
