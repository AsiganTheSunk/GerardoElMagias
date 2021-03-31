#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.items.equipement.constants.equipement_item_type import EquipmentItemType
from core.items.equipement.constants.equipment_slot_type import EquipmentSlotType
from core.items.equipement.generated_equipment import GeneratedEquipment
from core.items.affix.basic_affix import BasicAffix
from core.items.affix.constants.affix_attribute_type import AffixAttributeType
from core.items.equipement.constants.item_rarity import ItemRarity
from core.items.equipement.category.armor import Armor
from core.items.equipement.category.amulet import Amulet
from core.items.equipement.category.shield import Shield
from core.items.equipement.category.ring import Ring
from core.items.equipement.category.melee_weapon import MeleeWeapon

# Static Affix:
static_prefix = [BasicAffix('Resplandeciente', 20, AffixAttributeType.MAGIC, 7, 10,
                            [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD,
                        EquipmentItemType.RING, EquipmentItemType.AMULET])]

static_prefix1 = [BasicAffix('Reluciente', 10, AffixAttributeType.MAGIC, 4, 6,
                             [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD,
                         EquipmentItemType.RING, EquipmentItemType.AMULET])]

static_suffix = [BasicAffix('de Vida', 1, AffixAttributeType.HEALTH, 5, 15,
                       [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD,
                        EquipmentItemType.RING, EquipmentItemType.AMULET])]

# Static Items
static_amulet = GeneratedEquipment(Amulet("Amulet", 1, EquipmentSlotType.AMULET),
                                   EquipmentItemType.AMULET, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_amulet2 = GeneratedEquipment(Amulet("Amulet", 1, EquipmentSlotType.AMULET),
                                    EquipmentItemType.AMULET, ItemRarity.MAGICAL, static_prefix1, static_suffix)

static_body = GeneratedEquipment(Armor('Harapos', 1, 1, EquipmentSlotType.BODY),
                                 EquipmentItemType.ARMOR, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_dual = GeneratedEquipment(MeleeWeapon("Mandoble", "Espada", 16, 9, 13, EquipmentSlotType.DUAL_HAND),
                                 EquipmentItemType.WEAPON, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_main_weapon = GeneratedEquipment(MeleeWeapon('Puñal', 'Espada', 1, 2, 1, EquipmentSlotType.MAIN_HAND),
                                        EquipmentItemType.WEAPON, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_off_weapon = GeneratedEquipment(Shield('Rodela', 1, 20, EquipmentSlotType.OFF_HAND),
                                       EquipmentItemType.SHIELD, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_ring0 = GeneratedEquipment(Ring("Ring", 1, EquipmentSlotType.RING),
                                  EquipmentItemType.RING, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_ring1 = GeneratedEquipment(Ring("Ring", 1, EquipmentSlotType.RING),
                                  EquipmentItemType.RING, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_ring2 = GeneratedEquipment(Ring("Ring", 1, EquipmentSlotType.RING),
                                  EquipmentItemType.RING, ItemRarity.MAGICAL, static_prefix1, static_suffix)
