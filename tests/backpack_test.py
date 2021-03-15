from core.units.resources.backpack import BackPack
from tests.static_resources import *


def test_backpack():
    backpack = BackPack()
    backpack.add_item(static_body)
    backpack.add_item(static_amulet)
    backpack.add_item(static_ring0)
    backpack.add_item(static_ring1)
    backpack.add_item(static_ring2)
    backpack.add_item(static_main_weapon)
    backpack.add_item(static_off_weapon)
    backpack.add_item(static_dual)

    assert len(backpack.backpack_list) == 8

    backpack.remove_item(static_body)
    backpack.remove_item(static_amulet)
    backpack.remove_item(static_ring0)
    backpack.remove_item(static_ring1)
    backpack.remove_item(static_ring2)
    backpack.remove_item(static_main_weapon)
    backpack.remove_item(static_off_weapon)
    backpack.remove_item(static_dual)

    assert len(backpack.backpack_list) == 0
