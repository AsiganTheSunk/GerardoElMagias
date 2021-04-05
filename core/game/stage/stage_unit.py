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
from interface.ui_elements.ui_resource_bar import UIResourceBar


class StageUnit:
    def __init__(self, unit_identifier, unit, unit_position, animation_master, adjustment_y=0, adjustment_x=0):
        self.unit_identifier = unit_identifier
        self.unit = unit

        x, y = unit_position
        self.x = x
        self.y = y

        # Default Adjust Y of the Enemy Unit: Compensate Enemy Box
        # self.unit_position_y_correction(unit)

        self.animation_set = \
            UnitAnimationSet(animation_master.surface, x, y, unit.name,
                             animation_master.get_unit_animation_set(unit.name))
        self.animation_callbacks = animation_master.get_unit_animation_set_callbacks(unit.name)

        self.health_bar = None
        self.mana_bar = None
        self.fury_bar = None

    @property
    def get_unit_animation_set(self):
        return self.animation_set

    @property
    def get_unit_animation_callbacks(self):
        return self.animation_callbacks

    def set_health_bar(self, health_bar_position, size_x=160, size_y=15):
        health_bar_x, health_bar_y = health_bar_position
        # self.health_bar = HealthBar(health_bar_x, health_bar_y, self.unit.current_hp, self.unit.max_hp, size_x, size_y)
        self.health_bar = UIResourceBar(health_bar_x, health_bar_y, self.unit.current_hp, self.unit.max_hp, size_x, size_y)

    def set_mana_bar(self, mana_bar_position, size_x=160, size_y=15):
        mana_bar_x, mana_bar_y = mana_bar_position
        self.mana_bar = ManaBar(mana_bar_x, mana_bar_y, self.unit.current_mp, self.unit.max_mp, size_x, size_y)

    def set_fury_bar(self, fury_bar_position, size_x=160, size_y=15):
        fury_bar_x, fury_bar_y = fury_bar_position
        self.fury_bar = FuryBar(fury_bar_x, fury_bar_y, self.unit.current_fury, self.unit.max_fury, size_x, size_y)

    def render_health_bar(self, surface):
        if self.health_bar is not None:
            self.health_bar.draw(self.unit.current_hp, self.unit.max_hp, surface)

    def render_mana_bar(self, surface):
        if self.mana_bar is not None:
            self.mana_bar.draw(self.unit.current_mp, self.unit.max_mp, surface)

    def render_fury_bar(self, surface):
        if self.fury_bar is not None:
            self.fury_bar.draw(self.unit.current_fury, self.unit.max_fury, surface)

    def unit_position_y_correction(self, unit):
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
