#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mixer

# SOUND FX
# SPELL SOUNDS
lightning_spell_1_sound = mixer.Sound("resources/sound/spells/lightning_spell_1.wav")
lightning_spell_1_sound.set_volume(0.1)

lightning_spell_2_sound = mixer.Sound("resources/sound/spells/lightning_spell_2.wav")
lightning_spell_2_sound.set_volume(0.1)

firestorm_spell_1_sound = mixer.Sound("resources/sound/spells/firestorm_spell_1.wav")
firestorm_spell_1_sound.set_volume(0.1)

firestorm_spell_2_sound = mixer.Sound("resources/sound/spells/firestorm_spell_2.wav")
firestorm_spell_2_sound.set_volume(0.1)

heal_spell_1_sound = mixer.Sound("resources/sound/spells/heal_spell_1.wav")
heal_spell_1_sound.set_volume(0.1)


# ATTACK RELATED SOUNDS
hit_cut_sound = mixer.Sound("resources/sound/attacks/hit_cut.wav")
hit_cut_sound.set_volume(0.1)

hit_cut_boss_sound = mixer.Sound("resources/sound/attacks/hit_cut_boss.wav")
hit_cut_boss_sound.set_volume(0.1)

block_sound = mixer.Sound("resources/sound/attacks/block.wav")
block_sound.set_volume(0.1)

miss_sound = mixer.Sound("resources/sound/attacks/miss.wav")
miss_sound.set_volume(0.1)

critical_hit_sound = mixer.Sound("resources/sound/attacks/critical_hit.wav")
critical_hit_sound.set_volume(0.07)

ultimate_sound = mixer.Sound("resources/sound/attacks/ultimate.wav")
ultimate_sound.set_volume(0.10)

ulti_up_sound = mixer.Sound("resources/sound/fx/attacks/ulti_up.wav")
ulti_up_sound.set_volume(0.10)



# ITEM SOUNDS
health_potion_sound = mixer.Sound("resources/sound/items/health_potion.wav")
health_potion_sound.set_volume(0.15)

gold_sound = mixer.Sound("resources/sound/items/gold.wav")
gold_sound.set_volume(0.15)

eat_sound = mixer.Sound("resources/sound/items/eat.wav")
eat_sound.set_volume(0.15)

drink_sound = mixer.Sound("resources/sound/items/drink.wav")
drink_sound.set_volume(0.15)

empty_sound = mixer.Sound("resources/sound/items/empty.wav")
empty_sound.set_volume(0.15)

error_sound = mixer.Sound("resources/sound/items/error.wav")
error_sound.set_volume(0.12)

drum_roll_sound = mixer.Sound("resources/sound/items/drum_roll.wav")
drum_roll_sound.set_volume(0.10)
