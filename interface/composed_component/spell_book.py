#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText
from constants.basic_images import lightning_image, firestorm_image, background_shop_image, skill_heal_image, exitbook_button_image
from interface.basic_components import button
from constants.sound import lightning_spell_1_sound, firestorm_spell_1_sound, heal_spell_1_sound

from core.game.game_modes import GameModes

combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


def open_spell_book(caster, target, screen, text_sprite, battle_master):
    screen.blit(background_shop_image, (320, 80))
    exitbook_button = button.Button(screen, 920, 90, exitbook_button_image, 100, 50)
    lightning_spell_button = button.Button(screen, 350, 120, lightning_image, 150, 150)
    firestorm_spell_button = button.Button(screen, 365, 310, firestorm_image, 110, 110)
    heal_spell_button = button.Button(screen, 700, 120, skill_heal_image, 130, 130)

    if exitbook_button.draw():
        battle_master.game_mode = GameModes.BATTLE

    if lightning_spell_button.draw():
        if caster.use_lightning(target, text_sprite):
            lightning_spell_1_sound.play()
            battle_master.game_mode = GameModes.BATTLE
            battle_master.move_to_next_fighter()

    if firestorm_spell_button.draw():
        if caster.use_firestorm(target, text_sprite):
            firestorm_spell_1_sound.play()
            battle_master.game_mode = GameModes.BATTLE
            battle_master.move_to_next_fighter()

    if heal_spell_button.draw():
        if caster.use_heal(text_sprite):
            heal_spell_1_sound.play()
            battle_master.game_mode = GameModes.BATTLE
            battle_master.move_to_next_fighter()
