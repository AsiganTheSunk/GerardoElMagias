#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.map.stage_tree.stage_tree_builder import StageTreeBuilder

from logging import DEBUG

merkle_tree_builder = StageTreeBuilder()
# merkle_tree = merkle_tree_builder.build_merkle_tree(6)
new_tree = merkle_tree_builder.build_tree(2)
# new_tree.show_merkle_tree()
new_tree.show_stage_tree()
