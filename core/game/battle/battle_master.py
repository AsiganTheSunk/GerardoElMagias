#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from core.units.player.hero import HeroPlayer
from core.units.player.hero import HeroPlayer
from core.game.battle.enemy.group_generator import EnemyGroupGenerator
import constants.globals
from random import randint
from core.game.constants.game_modes import GameModes
from render.stage_unit_renderer import StageUnitRenderer
from core.game.stage.constants.stage_realms import StageRealms


class BattleMaster:
    def __init__(self, animation_master, sound_master, game_attributes):
        self.animation_master = animation_master
        self.sound_master = sound_master
        self.game_attributes = game_attributes

        self.queue = []
        self.level = 1
        self.boss_levels = [4, 7, 11, 15, 19, 20]
        self.boss_level = 0

        self.stage_unit_renderer = StageUnitRenderer(self.animation_master, self.game_attributes)

        self.friendly_fighters = [self.create_hero()]
        self.enemy_fighters = self.create_enemies()
        self.current_fighter = self.friendly_fighters[0]
        self.game_mode = GameModes.BATTLE
        self.previous_game_mode = None

    def swap_battle_mode(self, game_mode=None):
        if self.previous_game_mode is None:
            self.previous_game_mode = self.game_mode
            self.game_mode = game_mode

        if game_mode is None:
            self.game_mode = self.previous_game_mode
            self.previous_game_mode = None

    def get_hero(self):
        return self.friendly_fighters[0]

    def is_spell_book_phase(self):
        return self.game_mode is GameModes.SPELL_BOOK

    def is_victory_phase(self):
        return self.game_mode is GameModes.VICTORY

    def is_defeat_phase(self):
        return self.game_mode is GameModes.DEFEAT

    def is_level_up_phase(self):
        return self.game_mode is GameModes.LEVEL_UP

    def is_player_phase(self):
        return self.current_fighter is self.friendly_fighters[0]

    def is_battle_phase(self):
        return self.game_mode is GameModes.BATTLE or self.game_mode is GameModes.BOSS_BATTLE

    def current_stage(self):
        if self.boss_level > 3:
            return StageRealms.DUNGEON
        elif self.boss_level > 1:
            return StageRealms.CASTLE
        else:
            return StageRealms.FOREST

    def create_enemies(self):
        enemy_fighters = []
        enemy_group = EnemyGroupGenerator(self.sound_master)
        if self.is_boss_level():
            self.game_mode = GameModes.BOSS_BATTLE
            enemy_fighters = [enemy_group.scripted_enemy(self.boss_level, self.sound_master)]
            self.stage_unit_renderer.add(enemy_fighters[0], self.current_stage())
        else:
            self.game_mode = GameModes.BATTLE
            enemy_fighters = enemy_group.generate_enemy(self.level, self.boss_level)
            for unit_to_render in enemy_fighters:
                self.stage_unit_renderer.add(unit_to_render, self.current_stage())

        return enemy_fighters

    def is_boss_level(self):
        return self.level in self.boss_levels

    def create_hero(self):
        base_strength = randint(10, 15)
        base_dexterity = randint(10, 15)
        base_magic = randint(10, 15)
        base_vitality = randint(15, 20)
        base_resilience = randint(10, 15)
        base_luck = randint(1, 5)

        hero_player = HeroPlayer(1, base_strength, base_dexterity, base_magic,
                                 base_vitality, base_resilience, base_luck,
                                 self.sound_master)

        self.stage_unit_renderer.add(hero_player, self.current_stage())
        return hero_player

    def get_total_fighters(self):
        return len(self.enemy_fighters) + len(self.friendly_fighters)

    def move_to_defeat_phase(self):
        if not self.get_hero().alive:
            self.game_mode = GameModes.DEFEAT

    def move_to_victory_phase(self):
        hero_player = self.get_hero()
        if self.no_enemies_alive():
            self.game_mode = GameModes.VICTORY
            hero_player.gain_experience()

    def move_to_next_fighter(self):
        self.move_to_victory_phase()
        self.move_to_defeat_phase()

        combined_fighters = self.friendly_fighters + self.enemy_fighters
        combined_alive_fighters = list(filter(lambda fighter: fighter.alive, combined_fighters))
        current_index = combined_fighters.index(self.current_fighter)
        self.current_fighter = combined_fighters[(current_index + 1) % len(combined_fighters)]
        if self.current_fighter not in combined_alive_fighters:
            self.move_to_next_fighter()

    def next_level(self):
        self.level += 1
        if self.is_boss_level():
            self.boss_level += 1

        self.stage_unit_renderer.reset_stage_enemy_units()
        self.enemy_fighters = self.create_enemies()
        self.current_fighter = self.get_hero()

    def get_alive_enemies(self):
        return list(filter(lambda enemy: enemy.alive, self.enemy_fighters))

    def no_enemies_alive(self):
        return len(self.get_alive_enemies()) == 0

    def run_fighter_action(self, text_sprite):
        hero_player = self.get_hero()
        if self.current_fighter == hero_player:
            if hero_player.next_action:
                hero_player.run_next_action(text_sprite)
                self.move_to_next_fighter()

            if hero_player.whirlwind_status:
                hero_player.use_whirlwind(self.enemy_fighters, text_sprite)
                self.move_to_next_fighter()
                constants.globals.action_cooldown = 0
                hero_player.whirlwind_status = False

            if hero_player.ultimate_status:
                hero_player.use_ultimate(self.enemy_fighters, text_sprite)
                if hero_player.multi_attacks_left == 0:
                    hero_player.ultimate_status = False
                    constants.globals.action_cooldown = 0
                    self.move_to_next_fighter()
                    hero_player.multi_attacks_left = 7
                else:
                    self.move_to_victory_phase()
        else:
            # Enemy action
            self.current_fighter.action(hero_player, text_sprite)
            self.move_to_next_fighter()

    def handle_potion_click(self, event, button):
        hero_player = self.get_hero()
        potion = button.id
        # esto tendrá más sentido cuando las pociones sean parte de items en lugar de ser su propia movida
        if self.is_player_phase() and self.is_battle_phase():
            if potion == 'healing_potion':
                if hero_player.stash.has_healing_potion():
                    hero_player.next_action = ['use', potion]
            elif potion == 'mana_potion':
                if hero_player.stash.has_mana_potion():
                    hero_player.next_action = ['use', potion]
            # else:
            #     damage_text.warning(hero_player, 'No Healing Potions', self.game_attributes.text_sprite)
