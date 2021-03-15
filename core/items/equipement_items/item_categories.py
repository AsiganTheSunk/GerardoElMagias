from enum import Enum


# class EquipmentSlotType(Enum):
#     HEAD = 0
#     SHOULDERS = 1
#     CAPE = 2
#     GLOVES = 3
#     BRACERS = 4
#     BODY = 5
#     PANTS = 6
#     FEET = 7
#     BELT = 8
#     MAIN_HAND = 9
#     OFF_HAND = 10
#     RING_0 = 11
#     RING_1 = 12
#     AMULET = 13
#     DUAL_HAND = 14


class EquipmentSlotType(Enum):
    BODY = 'Pechera'
    PANTS = 'Pantalones'
    GLOVES = 'Guantes'
    CAPE = 'Capa'
    SHOULDERS = 'Hombreras'
    HEAD = 'Cabeza'
    BELT = 'Cinturon'
    BRACERS = 'Brazales'
    MAIN_HAND = 'Mano Principal'
    OFF_HAND = 'Mano Secundaria'
    AMULET = 'Amuleto'
    RING = 'Anillo'
    FEET = 'Pies'
    DUAL_HAND = 'Ambas Manos'


class ItemRaritySubType(Enum):
    NORMAL = ''
    ETHEREAL = 'Etéreo'


class ItemRarity(Enum):
    COMMON = 'Común'
    MAGICAL = 'Mágico'
    RARE = 'Raro'
    UNIQUE = 'Único'


class EquipmentItemType(Enum):
    RING = 'Anillo'
    WEAPON = 'Arma'
    AMULET = 'Amuleto'
    ARMOR = 'Armadura'
    SHIELD = 'Escudo'


class MeleeWeaponSubType(Enum):
    KNIFE = 'Puñal'
    PIKE = 'Pica'
    DAGGER = 'Daga'
    WHIP = 'Látigo'
    FIST = 'Puño'
    DUAL_HAND = 'Mandoble'


class MeleeWeaponType(Enum):
    SWORD = 'Espada'
    AXE = 'Hacha'
    LANCE = 'Lanza'
    WHIP = 'Látigo'


class ShieldType(Enum):
    HEATER = 'Heater'
    ROUND = 'Rodela'
    WANKEL = 'Wankel'
    WAR_DOOR = 'War Door'
    OVAL = 'Oval'
    KITE = 'Kite'
    SCUTUM = 'Scutum'
    AFRICAN = 'African'
    CELTIC = 'Celtic'
    COFFIN = 'Coffin'
    BUCKLER = 'Buckler'


class ShieldSubType(Enum):
    LIGHT = 'Ligero'
    HEAVY = 'Pesado'


class ArmorType(Enum):
    CLOTH = 'Tela'
    LEATHER = 'Cuero'
    CHAIN_MAIL = 'Cota de Malla'
    PLATE = 'Placas'
    BARLOG_SKIN = 'Piel de Barlog'
    INFERNAL_FORGED = 'Coraza forjada en el infierno'


class ArmorSubType(Enum):
    LIGHT = 'Ligera'
    HEAVY = 'Pesada'