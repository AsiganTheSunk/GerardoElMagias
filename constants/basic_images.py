#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image
from pygame import transform

# Background Images:
background_forest = image.load("resources/background/forest.png")
background_forest = transform.scale(background_forest, (1024, 576))
background_castle = image.load("resources/background/castle.gif")
background_castle = transform.scale(background_castle, (1024, 576))
background_dungeon = image.load("resources/background/dungeon.jpg")
background_dungeon = transform.scale(background_dungeon, (1024, 576))

# Panel Images:
panel_image = image.load("resources/icons/panel.jpg")

# Button Images:
spellbook_image = image.load("resources/icons/spellbook.png")
health_potion_image = image.load("resources/icons/health_potion.png")
mana_potion_image = image.load("resources/icons/mana_potion.png")
lightning_image = image.load("resources/icons/lightning.png")
firestorm_image = image.load("resources/icons/firestorm.png")
earth_image = image.load("resources/icons/earth.png")
heal_image = image.load("resources/icons/heal.png")
magicnova_image = image.load("resources/icons/magic_nova.png")


next_button_image = image.load("resources/icons/next.png")
exitbook_button_image = image.load("resources/icons/exitbook.png")
ultimate_image = image.load("resources/icons/ultimate.png")

gold_image = image.load("resources/icons/oro.png")

# Victory & Defeat Images:
victory_banner_image = image.load("resources/icons/victory.png")
defeat_banner_image = image.load("resources/icons/defeat.png")

# Sword Image:
sword_image = image.load("resources/icons/sword.png")

# Restart Image:
restart_image = image.load("resources/icons/restart.png")

# Loot Image:
loot_image = image.load("resources/icons/loot.png")

# Shop Image:
background_shop_image = image.load("resources/icons/shop.png")


# Weapon Images
# Sword Images
# Basic Swords
daga_image = image.load("resources/weapons/swords/base/daga.png")
espada_bastarda_image = image.load("resources/weapons/swords/base/espada_bastarda.png")
espada_corta_image = image.load("resources/weapons/swords/base/espada_corta.png")
espada_forjada_en_el_infierno_image = image.load("resources/weapons/swords/base/espada_forjada_en_el_infierno.png")
espada_larga_image = image.load("resources/weapons/swords/base/espada_larga.png")
gladius_image = image.load("resources/weapons/swords/base/gladius.png")
mandoble_image = image.load("resources/weapons/swords/base/mandoble.png")
punhal_image = image.load("resources/weapons/swords/base/puñal.png")
#Unique Swords
fragmento_de_infierno_image = image.load("resources/weapons/swords/unique/fragmento_de_infierno.png")


# Axe Images
# Basic Axes
decapitador_image = image.load("resources/weapons/axes/base/decapitador.png")
hacha_imgage = image.load("resources/weapons/axes/base/hacha.png")
hacha_doble_image = image.load("resources/weapons/axes/base/hacha_doble.png")

# Polearm images
alabarda_image = image.load("resources/weapons/polearms/base/alabarda.png")
lanza_image = image.load("resources/weapons/polearms/base/lanza.png")
partisana_image = image.load("resources/weapons/polearms/base/partisana.jpeg")
pica_image = image.load("resources/weapons/polearms/base/pica.png")

# Armor images
# Base Armors
armadura_de_cuero_image = image.load("resources/items/armors/base/armadura_de_cuero.png")
chaleco_de_cuero_image = image.load("resources/items/armors/base/chaleco_de_cuero.png")
coraza_image = image.load("resources/items/armors/base/coraza.png")
coraza_forjada_en_el_infierno_image = image.load("resources/items/armors/base/coraza_forjada_en_el_infierno.png")
cota_de_malla_image = image.load("resources/items/armors/base/cota_de_malla.png")
piel_de_balrog_image = image.load("resources/items/armors/base/coraza.png")
# Elite Armors



# Shield Images
# Base Shields
aegis_image = image.load("resources/items/shields/base/aegis.png")
defensor_image = image.load("resources/items/shields/base/defensor.png")
escudo_forjado_en_el_infierno_image = image.load("resources/items/shields/base/escudo_forjado_en_el_infierno.png")
guardian_image = image.load("resources/items/shields/base/guardian.png")
rodela_image = image.load("resources/items/shields/base/rodela.png")
# Unique Shields
furia_de_leon_image = image.load("resources/items/shields/unique/furia_de_leon.png")
guardia_del_monarca_image = image.load("resources/items/shields/unique/guardia_del_monarca.png")

# Skull Image:
skull_image = image.load("resources/icons/skull.png")
