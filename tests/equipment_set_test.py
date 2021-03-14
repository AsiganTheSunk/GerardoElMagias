from core.items.equipement_items.item_types import *
from core.items.equipement_items.item_categories import *
from core.items.generated_item import GeneratedItem
from core.items.affix_system.affix_type import *
from core.items.affix_system.affix_category import *
from core.units.resources.equipment import EquipmentSet
from tests.static_resources import *


def test_equip_while_empty():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    assert equipment_set.unequip(static_amulet, backpack) is False
    assert len(backpack.backpack_list) == 0


def test_equip_while_not_empty():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    backpack.add_item(static_amulet)
    backpack.add_item(static_amulet)

    assert len(backpack.backpack_list) == 2
    assert equipment_set.equip(static_amulet, backpack) is True
    assert len(backpack.backpack_list) == 1
    assert equipment_set.equip(static_amulet, backpack) is True
    assert len(backpack.backpack_list) == 1


def test_unequip_while_item_not_equip():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    assert equipment_set.unequip(static_amulet, backpack) is False
    assert len(backpack.backpack_list) == 0


def test_unequip_while_item_is_equiped():
    backpack = BackPack()
    equipment_set = EquipmentSet()
    backpack.add_item(static_amulet)
    equipment_set.equip(static_amulet, backpack)

    assert equipment_set.unequip(static_amulet, backpack) is True
    assert len(backpack.backpack_list) == 1


def test_equip_ring0_ring1_ring2():
    backpack = BackPack()
    equipment_set = EquipmentSet()
    pass


def test_equip_dual_while_main_or_off():
    backpack = BackPack()
    equipment_set = EquipmentSet()
    pass


def test_equip_off_or_main_while_dual():
    backpack = BackPack()
    equipment_set = EquipmentSet()
    pass

    # except AssertionError as expected_error:
    #     assert AssertionError is expected_error

    # backpack.remove_item(static_body)
    # backpack.remove_item(static_amulet)
    # backpack.remove_item(static_ring0)
    # backpack.remove_item(static_ring1)
    # backpack.remove_item(static_ring2)
    # backpack.remove_item(static_main_weapon)
    # backpack.remove_item(static_off_weapon)
    # backpack.remove_item(static_dual)

# # backpack.list_items()
#
# equipment_set = EquipmentSet()
# # equipment_set.list_equipment()
# print('---------------' * 10)
# equipment_set.equip(static_amulet, backpack)
# equipment_set.list_equipment()
# print('---------------' * 10)
# # backpack.list_items()
# equipment_set.unequip(static_amulet, backpack)
# equipment_set.list_equipment()
# backpack.list_items()
#
# print('---------------' * 10)
# print('RING TEST')
# print('---------------' * 10)
# equipment_set.equip(static_ring0, backpack)
# equipment_set.equip(static_ring1, backpack)
# equipment_set.list_equipment()
#
# print('---------------' * 10)
# equipment_set.equip(static_ring2, backpack)
# equipment_set.list_equipment()
# equipment_set.equip(static_ring0, backpack, 12)
# equipment_set.list_equipment()
# backpack.list_items()
#
#
# print('---------------' * 10)
# print('MAIN OFF and DUAL TEST')
# print('---------------' * 10)
# equipment_set.equip(static_body, backpack)
# equipment_set.equip(static_dual, backpack)
# equipment_set.equip(static_main_weapon, backpack)
# equipment_set.equip(static_off_weapon, backpack)
# equipment_set.list_equipment()
# backpack.list_items()
# print('---------------' * 10)
# equipment_set.equip(static_dual, backpack)
# equipment_set.list_equipment()
# backpack.list_items()

