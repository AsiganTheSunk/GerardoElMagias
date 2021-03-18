from core.game.battle.scripted_enemies import scripted_enemy
from constants.game_windows import screen_height, panel_height
from core.units.classes.player import HeroPlayer
from core.units.enemy_group import EnemyGroup
import constants.globals

from core.game.game_modes import GameModes


class BattleMaster:
    def __init__(self, animation_master):
        self.queue = []
        self.level = 1
        self.boss_levels = [4, 7, 11, 15, 19, 20]
        self.boss_level = 0
        self.animation_master = animation_master
        self.friendly_fighters = [self.create_hero()]
        self.enemy_fighters = self.create_enemies()
        self.current_fighter = self.friendly_fighters[0]
        self.game_mode = GameModes.BATTLE

    def create_enemies(self):
        enemy_fighters = []
        if self.is_boss_level():
            enemy_fighters = [scripted_enemy(self.boss_level, self.animation_master)]
        else:
            enemy_group = EnemyGroup(self.animation_master)
            enemy_fighters = enemy_group.generate_enemy(self.level, self.boss_level)
        return enemy_fighters

    def is_boss_level(self):
        return self.level in self.boss_levels

    def create_hero(self):
        return HeroPlayer(150, 580, "Hero", 1, 96, 30, 12, 10, 8, 2, 1, 1, 190, screen_height - panel_height + 20,
                          190, screen_height - panel_height + 40, 190, screen_height - panel_height + 40,
                          self.animation_master)

    def get_hero(self):
        return self.friendly_fighters[0]

    def get_total_fighters(self):
        return len(self.enemy_fighters) + len(self.friendly_fighters)

    def move_to_next_fighter(self):
        if not self.get_hero().alive:
            self.game_mode = GameModes.DEFEAT
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

        self.enemy_fighters = self.create_enemies()
        self.current_fighter = self.get_hero()

    def get_alive_enemies(self):
        return list(filter(lambda enemy: enemy.alive, self.enemy_fighters))

    def are_enemies_alive(self):
        return len(self.get_alive_enemies()) == 0

    def run_fighter_action(self, damage_text_group):
        hero_player = self.get_hero()
        if self.current_fighter == hero_player:
            if hero_player.next_action:
                hero_player.run_next_action(damage_text_group)
                self.move_to_next_fighter()

            if hero_player.ultimate_status:
                hero_player.use_ultimate(self.enemy_fighters, damage_text_group)
                if hero_player.multi_attacks_left == 0:
                    hero_player.ultimate_status = False
                    constants.globals.action_cooldown = 0
                    self.move_to_next_fighter()
                    hero_player.multi_attacks_left = 7
        else:
            # Enemy action
            self.current_fighter.action(hero_player, damage_text_group)
            self.move_to_next_fighter()

