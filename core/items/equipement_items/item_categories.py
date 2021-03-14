from enum import Enum


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