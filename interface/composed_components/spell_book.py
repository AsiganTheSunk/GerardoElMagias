#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.text.combat_text_resolver import CombatTextResolver
from core.text.damage_text import DamageText
from constants.basic_images import lightning_image, firestorm_image, background_shop_image, skill_heal_image, exitbook_button_image
from interface.basic_components import button
from constants.sound import lightning_spell_1_sound, firestorm_spell_1_sound, heal_spell_1_sound

from core.game.game_modes import GameModes
from interface.basic_components.button import Button, UIElement
from pygame import Rect

from interface.basic_components.image import Image
from interface.basic_components.ui_layout import UILayout

combat_text_resolver = CombatTextResolver()
damage_text = DamageText()

class Spellbook(UILayout):
    def __init__(self, battle_master, text_sprite):
        super().__init__()
        self.battle_master = battle_master
        self.text_sprite = text_sprite
        background_panel = Image(background_shop_image, 320, 80)
        lightning_spell_button = Button('lightning', 350, 120, lightning_image, 150, 150)
        firestorm_spell_button = Button('firestorm', 365, 310, firestorm_image, 110, 110)
        heal_spell_button = Button('heal_spell', 700, 120, skill_heal_image, 130, 130)
        lightning_spell_button.on_click(self.handle_spell_click)
        firestorm_spell_button.on_click(self.handle_spell_click)
        heal_spell_button.on_click(self.handle_spell_click)
        self.elements = [background_panel, lightning_spell_button, firestorm_spell_button, heal_spell_button]

    def handle_spell_click(self, event, button):
        if self.cast_spell(button.id, self.battle_master.get_hero(), self.battle_master.enemy_fighters, self.text_sprite):
            self.battle_master.swap_battle_mode()
            self.hidden = True
            self.battle_master.move_to_next_fighter()

    def cast_spell(self, name, caster, target, text_sprite):
        if name == 'lightning' and caster.use_lightning(target, text_sprite):
            lightning_spell_1_sound.play()
            return True
        elif name == 'firestorm' and caster.use_firestorm(target, text_sprite):
            firestorm_spell_1_sound.play()
            return True
        elif name == 'healspell' and caster.use_heal(text_sprite):
            heal_spell_1_sound.play()
            return True
        return False
