#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.stage.stage_unit import StageUnit
from core.game.stage.constants.stage_realms import StageRealms
from core.game.stage.db.stage_unit_positions import STAGE_UNIT_REALM_POSITIONS
from core.game.stage.db.stage_unit_resource_positions import STAGE_UNIT_UI_RESOURCE_POSITIONS


class StageUnitRenderer:
    def __init__(self, animation_master, game_attributes):
        self.stage_units = []
        self.unit_counter = 0

        self.animation_master = animation_master
        self.game_attributes = game_attributes

    def increment_unit_counter(self):
        self.unit_counter += 1

    def unit_position_adjustment(self, level, boss_level):
        pass

    def add(self, unit, stage_realm, level=0, boss_level=0):
        # Init Resources and Animations
        new_stage_unit = StageUnit(self.increment_unit_counter(), unit,
                                   self.get_stage_unit_position(stage_realm, len(self.stage_units)),
                                   self.animation_master)

        self.set_stage_unit_resource_positions(len(self.stage_units), new_stage_unit)

        # Add to stage_units to be rendered
        self.stage_units.append(new_stage_unit)
        # Establish animation_set, animation_callbacks for the Unit
        unit.set_animations(new_stage_unit.animation_set, new_stage_unit.animation_callbacks)

    def render_units(self):
        for stage_unit in self.stage_units:
            stage_unit.animation_set.draw()
            stage_unit.animation_set.update()

            stage_unit.render_health_bar(self.animation_master.surface)
            stage_unit.render_mana_bar(self.animation_master.surface)
            stage_unit.render_fury_bar(self.animation_master.surface)

    def reset_stage_enemy_units(self):
        self.stage_units = [self.stage_units[0]]

    def set_stage_unit_resource_positions(self, stage_unit_index, stage_unit_data):
        if stage_unit_index == 0:
            player_unit_resource_positions = self.get_unit_resource_position(0)

            stage_unit_data.set_health_bar(player_unit_resource_positions[0])       # Set HealthBar Position
            stage_unit_data.set_mana_bar(player_unit_resource_positions[1])         # Set ManaBar Position
            stage_unit_data.set_fury_bar(player_unit_resource_positions[2])         # Set FuryBar Position
        else:
            stage_unit_data.set_health_bar(self.get_unit_resource_position(stage_unit_index)[0])

    def get_unit_resource_position(self, stage_unit_index):
        stage_unit_resource_positions = []
        # Establish Stage Unit Height Correction
        stage_unit_height_correction = self.game_attributes.screen_height - self.game_attributes.panel_height
        for stage_unit_resource_x, stage_unit_resource_y in STAGE_UNIT_UI_RESOURCE_POSITIONS[stage_unit_index]:
            stage_unit_resource_positions.append((stage_unit_resource_x,
                                                  stage_unit_resource_y(stage_unit_height_correction)))
        return stage_unit_resource_positions

    @staticmethod
    def get_stage_unit_position(stage_realm, stage_unit_index):
        if stage_realm is StageRealms.DUNGEON:
            return STAGE_UNIT_REALM_POSITIONS[StageRealms.DUNGEON][stage_unit_index]
        elif stage_realm is StageRealms.CASTLE:
            return STAGE_UNIT_REALM_POSITIONS[StageRealms.CASTLE][stage_unit_index]
        elif stage_realm is StageRealms.FOREST:
            return STAGE_UNIT_REALM_POSITIONS[StageRealms.FOREST][stage_unit_index]