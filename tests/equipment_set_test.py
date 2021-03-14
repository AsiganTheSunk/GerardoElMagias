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

    assert equipment_set.un_equip(backpack, 13) is False
    assert len(backpack.backpack_list) == 0


def test_equip_while_not_empty():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    backpack.add_item(static_amulet)
    backpack.add_item(static_amulet2)

    # Starting Backpack len is 2
    assert len(backpack.backpack_list) == 2

    # Starting Backpack len is 1
    assert equipment_set.equip(static_amulet, backpack) is True
    assert len(backpack.backpack_list) == 1
    # Starting Backpack len is 1 since the item is replaced
    assert equipment_set.equip(static_amulet2, backpack) is True
    assert len(backpack.backpack_list) == 1

    # Non Equipped Item is static Amulet
    assert backpack.backpack_list[0] is static_amulet
    # Equipped Item is static Amulet 2
    assert equipment_set.get_item_from_slot(equipment_set.get_index_from_type(static_amulet2)) is static_amulet2


def test_unequip_while_item_is_equiped():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    backpack.add_item(static_amulet)
    assert len(backpack.backpack_list) == 1
    equipment_set.equip(static_amulet, backpack)
    assert len(backpack.backpack_list) == 0
    assert equipment_set.un_equip(backpack, 13) is True
    assert len(backpack.backpack_list) == 1
    assert equipment_set.get_item_from_slot(equipment_set.get_index_from_type(static_amulet)) is None


def test_equip_ring0_ring1_ring2():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    backpack.add_item(static_ring0)
    backpack.add_item(static_ring1)
    backpack.add_item(static_ring2)

    assert len(backpack.backpack_list) == 3
    assert equipment_set.equip(static_ring0, backpack) is True
    assert equipment_set.get_item_from_slot(11) is static_ring0
    assert equipment_set.equip(static_ring1, backpack) is True
    assert equipment_set.get_item_from_slot(12) is static_ring1
    assert len(backpack.backpack_list) == 1
    assert equipment_set.equip(static_ring2, backpack) is True

    assert equipment_set.get_item_from_slot(11) is static_ring2
    assert len(backpack.backpack_list) == 1
    assert backpack.backpack_list[0] is static_ring0

    assert equipment_set.equip(static_ring0, backpack, 11)
    assert equipment_set.get_item_from_slot(11) is static_ring0
    assert backpack.backpack_list[0] is static_ring2
    assert len(backpack.backpack_list) == 1

    assert equipment_set.un_equip(backpack, 11) is True
    assert len(backpack.backpack_list) == 2
    assert backpack.backpack_list[1] is static_ring0

    assert equipment_set.un_equip(backpack, 12) is True
    assert len(backpack.backpack_list) == 3
    assert backpack.backpack_list[2] is static_ring1


def test_equip_dual_while_main_or_off():
    backpack = BackPack()
    equipment_set = EquipmentSet()

    backpack.add_item(static_off_weapon)
    backpack.add_item(static_main_weapon)
    backpack.add_item(static_dual)

    assert len(backpack.backpack_list) == 3
    assert equipment_set.equip(static_main_weapon, backpack) is True
    assert equipment_set.get_item_from_slot(9) is static_main_weapon
    assert equipment_set.equip(static_off_weapon, backpack) is True
    assert equipment_set.get_item_from_slot(10) is static_off_weapon
    assert len(backpack.backpack_list) == 1

    assert equipment_set.equip(static_dual, backpack) is True
    assert equipment_set.get_item_from_slot(14) is static_dual
    assert len(backpack.backpack_list) == 2

    assert equipment_set.equip(static_main_weapon, backpack) is True
    assert equipment_set.get_item_from_slot(9) is static_main_weapon
    assert equipment_set.equip(static_off_weapon, backpack) is True
    assert equipment_set.get_item_from_slot(10) is static_off_weapon
    assert len(backpack.backpack_list) == 1

    assert backpack.backpack_list[0] is static_dual
    assert equipment_set.equip(static_dual, backpack) is True
    assert equipment_set.get_item_from_slot(14) is static_dual
    assert len(backpack.backpack_list) == 2

    assert backpack.backpack_list[0] is static_main_weapon
    assert backpack.backpack_list[1] is static_off_weapon
