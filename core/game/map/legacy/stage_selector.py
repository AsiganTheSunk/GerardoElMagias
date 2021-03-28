#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StageSelector:
    def __init__(self, world_map):
        self.world_map = world_map
        self.current_realm_index = 0
        self.current_realm = self.world_map[self.current_realm_index]
        self.current_stage = self.world_map[self.current_realm_index][0]

    def get_current_stage(self):
        return self.current_stage

    # Todo: Review how to properly implement this step, via index would be a better option
    def set_current_stage(self, stage_node):
        if stage_node.previous.properties.complete_status:
            return stage_node

    # Todo: Talk with stage initializer to run the stage
    def run_stage_node(self):
        pass

    def has_been_completed(self):
        return self.current_stage.properties.complete_status

    def move_to_next_node(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.next_node

    def move_to_previous_node(self):
        if self.current_stage.previous_node is not None:
            self.current_stage = self.current_stage.previous_node

    def move_to_right_alternative_node(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.right_child

    def move_to_left_alternative_node(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.left_child

    def move_to_dungeon(self):
        if self.has_been_completed():
            self.current_stage = self.current_stage.dungeon_node

    def is_main_line_completed(self):
        self.is_completed_realm(self.current_realm[0])

    def is_completed_realm(self, stage_node=None):
        if stage_node is not None:
            if stage_node.propierties.complete_status:
                self.is_completed_realm(stage_node.next_node)
            return False
        return True

    def move_to_next_realm(self):
        if self.is_completed_realm() and self.current_realm_index < len(self.world_map):
            self.current_realm_index += 1
            self.current_realm = self.world_map[self.current_realm_index]

    def move_to_previous_realm(self):
        if self.current_realm_index > 0:
            self.current_realm_index -= 1
            self.current_realm = self.world_map[self.current_realm_index]
