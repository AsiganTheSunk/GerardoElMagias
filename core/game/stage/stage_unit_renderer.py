#!/usr/bin/env python
# -*- coding: utf-8 -*-


from core.units.enemy.dragon.small_dragon import SmallDragon
from core.units.enemy.dragon.dragon import Dragon
from core.units.enemy.bone.bone_wizard import BoneWizard
from core.units.enemy.bandit.bandit_chief import BanditChief
from core.units.enemy.bandit.bandit import Bandit
from core.units.enemy.djinn.djinn import Djinn
from core.units.enemy.demon.demon import Demon
from core.units.enemy.lizard.lizard import Lizard
from core.units.resources.fury_bar import FuryBar
from core.units.resources.mana_bar import ManaBar
from core.units.resources.health_bar import HealthBar

from core.game.animations.sets.unit_animation_set import UnitAnimationSet


class StageUnit:
    def __init__(self, unit_identifier, unit, x, y, animation_master, adjustment_y=0, adjustment_x=0):
        self.unit_identifier = unit_identifier
        self.unit = unit
        self.x = x
        self.y = y

        # Default Adjust Y of the Enemy Unit: Compensate Enemy Box
        self.position_y_adjustment(unit)

        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y, unit.name,
                             animation_master.get_unit_animation_set(unit.name))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks(unit.name)

        self.health_bar = None
        self.mana_bar = None
        self.fury_bar = None

    def get_unit_animation_set(self):
        return self.animation_set

    def get_unit_animation_callbacks(self):
        return self.animation_callbacks

    def set_health_bar(self, health_bar_x, health_bar_y):
        self.health_bar = HealthBar(health_bar_x, health_bar_y, self.unit.current_hp, self.unit.max_hp)

    def set_mana_bar(self, mana_bar_x, mana_bar_y):
        self.mana_bar = ManaBar(mana_bar_x, mana_bar_y, self.unit.current_mp, self.unit.max_mp)

    def set_fury_bar(self, fury_bar_x, fury_bar_y):
        self.fury_bar = FuryBar(fury_bar_x, fury_bar_y, self.unit.current_fury, self.unit.max_fury)

    def position_y_adjustment(self, unit):
        if type(unit) is Bandit:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is BoneWizard:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is Lizard:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is BanditChief:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is SmallDragon:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is Djinn:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is Dragon:
            position_y_adjustment = 1
            self.y += position_y_adjustment

        elif type(unit) is Demon:
            position_y_adjustment = 1
            self.y += position_y_adjustment


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

    def add(self, unit, stage, level=0, boss_level=0):
        # Init Resources and Animations
        stage_unit_pos_x, stage_unit_pos_y = self.get_stage_unit_position(stage, len(self.stage_units))
        new_stage_unit = StageUnit(self.increment_unit_counter(), unit, stage_unit_pos_x, stage_unit_pos_y, self.animation_master)
        self.set_stage_unit_resource(len(self.stage_units), new_stage_unit)

        # Add to stage_units to be rendered
        self.stage_units.append(new_stage_unit)
        # Establish animation_set, animation_callbacks
        unit.set_animations(new_stage_unit.animation_set, new_stage_unit.animation_callbacks)

    def render_units(self):
        for stage_unit in self.stage_units:
            stage_unit.animation_set.draw()
            stage_unit.animation_set.update()
            if stage_unit.health_bar is not None:
                stage_unit.health_bar.draw(stage_unit.unit.current_hp, stage_unit.unit.max_hp,
                                           self.animation_master.surface)
            if stage_unit.mana_bar is not None:
                stage_unit.mana_bar.draw(stage_unit.unit.current_mp, stage_unit.unit.max_mp,
                                         self.animation_master.surface)
            if stage_unit.fury_bar is not None:
                stage_unit.fury_bar.draw(stage_unit.unit.current_fury, stage_unit.unit.max_fury,
                                         self.animation_master.surface)

    def reset_stage_enemy_units(self):
        self.stage_units = [self.stage_units[0]]

    def set_stage_unit_resource(self, stage_unit_index, stage_unit_data):
        if stage_unit_index == 0:
            player_resource_position = self.get_resource_unit_position(0)

            health_bar_x, health_bar_y = player_resource_position[0]
            mana_bar_x, mana_bar_y = player_resource_position[1]
            fury_bar_x, fury_bar_y = player_resource_position[2]

            stage_unit_data.set_health_bar(health_bar_x, health_bar_y)
            stage_unit_data.set_mana_bar(mana_bar_x, mana_bar_y)
            stage_unit_data.set_fury_bar(fury_bar_x, fury_bar_y)

        else:
            stage_unit_pos_x, stage_unit_pos_y = self.get_resource_unit_position(stage_unit_index)[0]
            stage_unit_data.set_health_bar(stage_unit_pos_x, stage_unit_pos_y)
            # stage_unit_data.set_mana_bar()
            # stage_unit_data.set_fury_bar()

    def get_resource_unit_position(self, stage_unit_index):
        stage_unit_position_resource_list = [
            [
                (270, self.game_attributes.screen_height - self.game_attributes.panel_height + 20),
                (270, self.game_attributes.screen_height - self.game_attributes.panel_height + 40),
                (270, self.game_attributes.screen_height - self.game_attributes.panel_height + 40)
            ],
            [
                (680, self.game_attributes.screen_height - self.game_attributes.panel_height + 40)
            ],
            [
                (680, self.game_attributes.screen_height - self.game_attributes.panel_height + 100)
            ],
            [
                (900, self.game_attributes.screen_height - self.game_attributes.panel_height + 40)
            ],
            [
                (900, self.game_attributes.screen_height - self.game_attributes.panel_height + 100)
            ]
        ]
        return stage_unit_position_resource_list[stage_unit_index]

    def get_stage_unit_position(self, stage, stage_unit_index):
        if stage == 'dungeon':
            stage_dungeon_positions = [
                (300, 480),
                (700, 370), (825, 450),
                (950, 370), (1075, 450)
            ]
            return stage_dungeon_positions[stage_unit_index]
        elif stage == 'castle':
            stage_castle_positions = [
                (300, 480),
                (700, 420), (825, 480),
                (950, 420), (1075, 480)
            ]
            return stage_castle_positions[stage_unit_index]
        elif stage == 'forest':
            stage_forest_positions = [
                (300, 480),
                (650, 475), (775, 500),
                (900, 475), (1025, 500)
            ]
            return stage_forest_positions[stage_unit_index]