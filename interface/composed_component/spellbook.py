from pygame import display
import constants.globals
from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText
from constants.basic_images import *
from interface.basic_components import button
from constants.sound import *
from core.game.game_modes import GameModes

combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


def open_spellbook(caster, target, screen, damage_text_group, battle_master):
    screen.blit(shop_image, (120, 190))
    next_button = button.Button(screen, 800, 10, next_img, 80, 80)
    lightning_spell_button = button.Button(screen, 150, 220, lightning_img, 150, 150)
    firestorm_spell_button = button.Button(screen, 165, 410, firestorm_img, 110, 110)
    heal_spell_button = button.Button(screen, 500, 220, heal_img, 130, 130)

    if next_button.draw():
        battle_master.game_mode = GameModes.BATTLE
    if lightning_spell_button.draw():
        if caster.use_lightning(target, damage_text_group):
            lightning_spell_1_sound.play()
            battle_master.game_mode = GameModes.BATTLE
            battle_master.move_to_next_fighter()

    if firestorm_spell_button.draw():
        if caster.use_firestorm(target, damage_text_group):
            firestorm_spell_1_sound.play()
            battle_master.game_mode = GameModes.BATTLE
            battle_master.move_to_next_fighter()

    if heal_spell_button.draw():
        if caster.use_heal(damage_text_group):
            heal_spell_1_sound.play()
            battle_master.game_mode = GameModes.BATTLE
            battle_master.move_to_next_fighter()

        display.update()
