from core.game.battle.scripted_enemies import scripted_enemy
from constants.game_windows import screen_height, bottom_panel
from core.units.classes.player import HeroPlayer
from core.units.enemy_group import EnemyGroup

class BattleMaster:
	def __init__(self):
		self.queue = []
		self.level = 1
		self.friendly_fighters = [self.create_hero()]
		self.enemy_fighters = self.create_enemies()
		self.current_fighter = self.friendly_fighters[0]

	def create_enemies(self):
		enemy_fighters = []
		boss_level = 1
		if self.is_boss_level(self.level):
			enemy_fighters = [scripted_enemy(boss_level)]
		else:
			enemy_group = EnemyGroup()
			enemy_fighters = enemy_group.generate_enemy(self.level, boss_level)
		return enemy_fighters
			
	def is_boss_level(self, level):
		boss_levels = [4, 7, 11, 15, 19, 20]
		return level in boss_levels

	def create_hero(self):
		return HeroPlayer(150, 580, "Hero", 1, 90, 30, 12, 9, 8, 2, 1, 1, 115, screen_height - bottom_panel + 50, 290, screen_height - bottom_panel + 50, 90, 510)
	
	def get_hero(self):
		return self.friendly_fighters[0]
		
	def get_total_fighters(self):
		return len(self.enemy_fighters) + len(self.friendly_fighters)
		
	def move_to_next_fighter(self):
		combined_fighters = self.friendly_fighters + self.enemy_fighters
		current_index = combined_fighters.index(self.current_fighter)
		self.current_fighter = combined_fighters[(current_index + 1) % len(combined_fighters)]

	def next_level(self):
		self.level += 1
		self.enemy_fighters = self.create_enemies()
	