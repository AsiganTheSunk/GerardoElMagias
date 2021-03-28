#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.text.combat_text_resolver import CombatTextResolver
from core.game.text.damage_text import DamageText
from constants.basic_images import lightning_image, firestorm_image, background_shop_image, heal_image, earth_image, water_nova_image, exitbook_button_image
from constants.sound import lightning_spell_sound, firestorm_spell_sound, heal_spell_sound, earth_spell_sound

from interface.basic_elements.button import Button

from interface.basic_elements.image import Image
from interface.elements.ui_layout import UILayout

combat_text_resolver = CombatTextResolver()
damage_text = DamageText()


class SpellBook(UILayout):
    def __init__(self, battle_master, text_sprite, add_effect):
        super().__init__()
        self.battle_master = battle_master
        self.text_sprite = text_sprite
        background_panel = Image(background_shop_image, 260, 60)

        lightning_spell_button = Button('lightning_spell', 330, 100, lightning_image, 120, 120)
        firestorm_spell_button = Button('fire_storm_spell', 345, 250, firestorm_image, 90, 90)
        earth_spell_button = Button('earth_shock_spell', 330, 360, earth_image, 130, 130)
        heal_spell_button = Button('heal_spell', 690, 100, heal_image, 100, 100)
        magic_nova_spell_button = Button('magic_nova_spell', 420, 25, water_nova_image, 250, 250)

        lightning_spell_button.on_click(self.handle_spell_click)
        firestorm_spell_button.on_click(self.handle_spell_click)
        earth_spell_button.on_click(self.handle_spell_click)
        heal_spell_button.on_click(self.handle_spell_click)
        magic_nova_spell_button.on_click(self.handle_spell_click)

        self.elements = [
            background_panel,
            lightning_spell_button, firestorm_spell_button,
            earth_spell_button, heal_spell_button,
            magic_nova_spell_button
        ]
        self.add_effect = add_effect

    def handle_spell_click(self, event, button):
        if self.cast_spell(button.id, self.battle_master.get_hero(), self.battle_master.enemy_fighters, self.text_sprite):
            self.battle_master.swap_battle_mode()
            self.hidden = True
            self.battle_master.move_to_next_fighter()

    def cast_spell(self, name, caster, target, text_sprite):
        if name == 'lightning_spell' and caster.use_lightning_spell(target, text_sprite):
            lightning_spell_sound.play()
            return True
        elif name == 'fire_storm_spell' and caster.use_firestorm_spell(target, text_sprite):
            self.add_effect(target, 'fire_storm')
            firestorm_spell_sound.play()
            return True
        elif name == 'heal_spell' and caster.use_heal_spell(text_sprite):
            heal_spell_sound.play()
            return True
        elif name == 'earth_shock_spell' and caster.use_earth_spell(target, text_sprite):
            self.add_effect(target, 'earth_shock')
            earth_spell_sound.play()
            return True
        elif name == 'magic_nova_spell' and caster.use_magicnova_spell(target, text_sprite):
            self.add_effect(target, 'water_nova')
            earth_spell_sound.play()
            return True
        return False


