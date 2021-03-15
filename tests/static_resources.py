from core.units.resources.backpack import BackPack
from core.items.equipement_items.item_types import *
from core.items.equipement_items.item_categories import *
from core.items.generated_item import GeneratedItem
from core.items.affix_system.affix_type import *
from core.items.affix_system.affix_category import *
from core.units.resources.equipment import EquipmentSet


# Static Affix:
static_prefix = [Affix('Resplandeciente', 20, AttributeType.MAGIC_POWER, 7, 10,
                       [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD,
                        EquipmentItemType.RING, EquipmentItemType.AMULET])]

static_prefix1 = [Affix('Reluciente', 10, AttributeType.MAGIC_POWER, 4, 6,
                        [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD,
                         EquipmentItemType.RING, EquipmentItemType.AMULET])]

static_suffix = [Affix('de Vida', 1, AttributeType.HEALTH, 5, 15,
                       [EquipmentItemType.WEAPON, EquipmentItemType.ARMOR, EquipmentItemType.SHIELD,
                        EquipmentItemType.RING, EquipmentItemType.AMULET])]

# Static Items
static_amulet = GeneratedItem(Amulet("Amulet", 1, EquipmentSlotType.AMULET),
                              EquipmentItemType.AMULET, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_amulet2 = GeneratedItem(Amulet("Amulet", 1, EquipmentSlotType.AMULET),
                              EquipmentItemType.AMULET, ItemRarity.MAGICAL, static_prefix1, static_suffix)

static_body = GeneratedItem(Armor('Harapos', 1, 1, EquipmentSlotType.BODY),
                            EquipmentItemType.ARMOR, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_dual = GeneratedItem(MeleeWeapon("Mandoble", "Espada", 16, 9, 13, EquipmentSlotType.DUAL_HAND),
                            EquipmentItemType.WEAPON, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_main_weapon = GeneratedItem(MeleeWeapon('Puñal', 'Espada', 1, 2, 1, EquipmentSlotType.MAIN_HAND),
                                   EquipmentItemType.WEAPON, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_off_weapon = GeneratedItem(Shield('Rodela', 1, 20, EquipmentSlotType.OFF_HAND),
                                  EquipmentItemType.SHIELD, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_ring0 = GeneratedItem(Ring("Ring", 1, EquipmentSlotType.RING),
                             EquipmentItemType.RING, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_ring1 = GeneratedItem(Ring("Ring", 1, EquipmentSlotType.RING),
                             EquipmentItemType.RING, ItemRarity.MAGICAL, static_prefix, static_suffix)

static_ring2 = GeneratedItem(Ring("Ring", 1, EquipmentSlotType.RING),
                             EquipmentItemType.RING, ItemRarity.MAGICAL, static_prefix1, static_suffix)
