from map.merklebuilder.merkel_builder import StageBuilder

from logging import INFO, DEBUG, WARNING

merkle_tree_builder = StageBuilder(DEBUG)
# merkle_tree = merkle_tree_builder.build_merkle_tree(6)
new_tree = merkle_tree_builder.build_tree(2)
# new_tree.show_merkle_tree()


new_tree.show_stage_tree()
