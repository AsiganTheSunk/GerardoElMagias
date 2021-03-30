#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image
from pygame import transform

# ==============================================================
# Background Images:
# ==============================================================
background_forest_image = image.load("resources/image/background/forest.png")
background_forest_image = transform.scale(background_forest_image, (1024, 576))
background_castle_image = image.load("resources/image/background/castle.gif")
background_castle_image = transform.scale(background_castle_image, (1024, 576))
background_dungeon_image = image.load("resources/image/background/dungeon.jpg")
background_dungeon_image = transform.scale(background_dungeon_image, (1024, 576))
background_spell_book_image = image.load("resources/image/background/spell_book.png")


# ==============================================================
# Button Images:
# ==============================================================
spell_book_button_image = image.load("resources/image/button/spell_book.png")
exit_book_button_image = image.load("resources/image/button/exit_book.png")
restart_button_image = image.load("resources/image/button/restart.png")
skull_button_image = image.load("resources/image/button/skull.png")
kill_button_image = image.load("resources/image/button/kill.png")

# ==============================================================
# Consumable Images:
# ==============================================================
health_potion_image = image.load("resources/image/consumable/health_potion.png")
mana_potion_image = image.load("resources/image/consumable/mana_potion.png")


# ==============================================================
# Button Skill Images:
# ==============================================================
lightning_image = image.load("resources/image/button/lightning.png")
firestorm_image = image.load("resources/image/button/firestorm.png")
earth_image = image.load("resources/image/button/earth_shock.png")
heal_image = image.load("resources/image/button/heal.png")
water_nova_image = image.load("resources/image/button/water_nova.png")
next_button_image = image.load("resources/image/button/next.png")
ultimate_image = image.load("resources/image/button/ultimate.png")
whirlwind_image = image.load("resources/image/button/whirlwind.png")


# ==============================================================
# Icon Images:
# ==============================================================
gold_image = image.load("resources/image/icon/oro.png")


# ==============================================================
# Banner Images:
# ==============================================================
victory_banner_image = image.load("resources/image/banner/victory.png")
defeat_banner_image = image.load("resources/image/banner/defeat.png")


# ==============================================================
# Mouse Images:
# ==============================================================
sword_image = image.load("resources/image/mouse/sword.png")
loot_image = image.load("resources/image/mouse/loot.png")


# ==============================================================
# Equipment Images:
# ==============================================================

# Basic Swords Images:
# ==============================================================
daga_image = image.load("resources/image/equipment/weapons/swords/base/daga.png")
espada_bastarda_image = image.load("resources/image/equipment/weapons/swords/base/espada_bastarda.png")
espada_corta_image = image.load("resources/image/equipment/weapons/swords/base/espada_corta.png")
espada_forjada_en_el_infierno_image = image.load("resources/image/equipment/weapons/swords/base/espada_forjada_en_el_infierno.png")
espada_larga_image = image.load("resources/image/equipment/weapons/swords/base/espada_larga.png")
gladius_image = image.load("resources/image/equipment/weapons/swords/base/gladius.png")
mandoble_image = image.load("resources/image/equipment/weapons/swords/base/mandoble.png")
punhal_image = image.load("resources/image/equipment/weapons/swords/base/puñal.png")

# Unique Swords
# ==============================================================
fragmento_de_infierno_image = image.load("resources/image/equipment/weapons/swords/unique/fragmento_de_infierno.png")


# Basic Axes Images:
# ==============================================================
decapitador_image = image.load("resources/image/equipment/weapons/axes/base/decapitador.png")
hacha_imgage = image.load("resources/image/equipment/weapons/axes/base/hacha.png")
hacha_doble_image = image.load("resources/image/equipment/weapons/axes/base/hacha_doble.png")

# Basic Polearm Images:
# ==============================================================
alabarda_image = image.load("resources/image/equipment/weapons/polearms/base/alabarda.png")
lanza_image = image.load("resources/image/equipment/weapons/polearms/base/lanza.png")
partisana_image = image.load("resources/image/equipment/weapons/polearms/base/partisana.jpeg")
pica_image = image.load("resources/image/equipment/weapons/polearms/base/pica.png")


# Basic Armor Images:
# ==============================================================
armadura_de_cuero_image = image.load("resources/image/equipment/armors/base/armadura_de_cuero.png")
chaleco_de_cuero_image = image.load("resources/image/equipment/armors/base/chaleco_de_cuero.png")
coraza_image = image.load("resources/image/equipment/armors/base/coraza.png")
coraza_forjada_en_el_infierno_image = \
    image.load("resources/image/equipment/armors/base/coraza_forjada_en_el_infierno.png")
cota_de_malla_image = image.load("resources/image/equipment/armors/base/cota_de_malla.png")
piel_de_balrog_image = image.load("resources/image/equipment/armors/base/coraza.png")


# Elite Armors
# ==============================================================

# Basic Shield Images
# ==============================================================
aegis_image = image.load("resources/image/equipment/shields/base/aegis.png")
defensor_image = image.load("resources/image/equipment/shields/base/defensor.png")
escudo_forjado_en_el_infierno_image = \
    image.load("resources/image/equipment/shields/base/escudo_forjado_en_el_infierno.png")
guardian_image = image.load("resources/image/equipment/shields/base/guardian.png")
rodela_image = image.load("resources/image/equipment/shields/base/rodela.png")
# Unique Shields
furia_de_leon_image = image.load("resources/image/equipment/shields/unique/furia_de_leon.png")
guardia_del_monarca_image = image.load("resources/image/equipment/shields/unique/guardia_del_monarca.png")
