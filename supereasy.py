if time.get_ticks() - self.update_time > action_cooldown:
    self.update_time = time.get_ticks()
    hero_player.attack(enemy_list[0], damage_text_group)