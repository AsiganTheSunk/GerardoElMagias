#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import display, mouse
from interface.composed_ui_elements.player.player_interface_panel import PlayerInterfacePanel
from interface.composed_ui_elements.player_interface_text import PlayerUITextStageInformation
from core.game.stage.selector.stage_background_selector import StageBackgroundSelector
from core.game.stage.render.stage_unit_effects_renderer import StageUnitEffectsRenderer
from interface.composed_ui_elements.player.player_bottom_panel_buttons import PlayerBottomPanelButtons
from interface.player_interface_renderer import PlayerInterfaceRenderer
import constants.globals
from core.game.text.damage_text import DamageText

# Init DamageText
damage_text = DamageText()


class StageRenderer(PlayerUITextStageInformation,
                    StageBackgroundSelector, StageUnitEffectsRenderer, PlayerInterfaceRenderer):
    def __init__(self, battle_master, game_attributes, animation_master, sound_master):
        self.battle_master = battle_master
        self.game_attributes = game_attributes
        self.animation_master = animation_master
        self.sound_master = sound_master
        self.player = battle_master.get_hero()

        PlayerInterfaceRenderer.__init__(self, game_attributes.surface)
        StageBackgroundSelector.__init__(self, game_attributes.surface)
        StageUnitEffectsRenderer.__init__(self, animation_master)
        PlayerUITextStageInformation.__init__(self, game_attributes)

        # Todo: This should not be done this way.
        self.player_interface_panel = PlayerInterfacePanel(game_attributes)
        self.player_bottom_panel_buttons = \
            PlayerBottomPanelButtons(self.sound_master, self.battle_master, self.game_attributes, self.add_effect)

        # Todo: This should not be done here.
        self.add_render(self.player_interface_panel)
        self.add_render(self.player_bottom_panel_buttons)

        self.clock = self.game_attributes.clock
        self.fps = self.game_attributes.fps

    @staticmethod
    def display_caption():
        display.set_caption("Las Trepidantes Aventuras de Gerardo EL MAGIAS")

    def display_victory(self):
        self.player_interface_panel.display_victory_banner()

    def display_defeat(self):
        self.player_interface_panel.display_defeat_banner()

    def add_render(self, ui_layout):
        for ui_element in ui_layout.elements:
            self.add(ui_element)

    def update(self):
        self.update_ui_text_stage_layout(self.battle_master)
        self.player_bottom_panel_buttons.update_button_elements()
        self.update_effects()
        self.update_victory()
        self.update_defeat()
        self.update_ultimate_buttons()
        self.update_mouse()

    def render(self):
        # Todo: Known Issues, the Victory Badge Displays Above the SpellBook. This issue comes from been unable to
        #  render layers at the moment. Since there it's just the order in which the elements where added in the list,
        #  and not a level associated to it. The current render order must be done manually.
        #  (Also the use of the Sprite class, since we are using Primitives it's not an options unless we
        #  establish the mouse_over effects as images in the future, then we can think of layering properly.)

        # Render Background
        self.set_stage_background(self.battle_master.level)

        # Render Units
        self.battle_master.stage_unit_renderer.render_units()

        # Render Interface
        self.render_interface()

        # Render Resource on Interface
        self.battle_master.stage_unit_renderer.render_unit_resources()

        # Render Text on Resource and Interface
        self.render_ui_elements(self.ui_text_elements)

        # Render Combat Text: So it shows above the current Stage Menus
        self.game_attributes.text_sprite.update()
        self.game_attributes.text_sprite.draw(self.surface)

    def resolve_render(self):
        # Setup TickRate for the Game
        self.clock.tick(self.fps)

        # Render Stage
        self.render()

        # Update Stage Render
        self.update()

    def update_ultimate_buttons(self):
        if self.player.has_enough_fury():
            self.player_bottom_panel_buttons.ultimate_button.activate()
        else:
            self.player_bottom_panel_buttons.ultimate_button.deactivate()

        if self.player.has_enough_fury(50):
            self.player_bottom_panel_buttons.whirlwind_button.activate()
        else:
            self.player_bottom_panel_buttons.whirlwind_button.deactivate()

    def update_mouse(self):
        if self.battle_master.is_victory_phase():
            for enemy_unit in self.battle_master.stage_unit_renderer.stage_units[1:]:
                if enemy_unit.animation_set.mouse_collision():
                    self.player_interface_panel.display_bag_mouse()
                    if constants.globals.clicked:
                        self.player.get_loot(enemy_unit.unit, self.game_attributes.text_sprite)
                        constants.globals.clicked = False
                    # Return to avoid normal mouse showing up
                    return

        if self.battle_master.is_battle_phase():
            for enemy_unit in self.battle_master.stage_unit_renderer.stage_units[1:]:
                if enemy_unit.unit.animation_set.mouse_collision():
                    self.player_interface_panel.display_sword_mouse()
                    if constants.globals.clicked and enemy_unit.unit.alive:
                        self.player.next_action = ('attack', enemy_unit.unit)
                    # Return to avoid normal mouse showing up
                    return
        # Enable default mouse
        mouse.set_visible(True)

    def update_victory(self):
        if self.battle_master.is_victory_phase():
            self.player_bottom_panel_buttons.next_button.hidden = False
            self.display_victory()

    def update_defeat(self):
        if self.battle_master.is_defeat_phase():
            self.display_defeat()
