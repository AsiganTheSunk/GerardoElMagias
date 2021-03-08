
def setup_battle(target_list, hero_player):
    clock.tick(fps)

    # draw backgrounds
    draw_bg_forest()

    # draw panel
    draw_stage()
    draw_panel()

    # damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # draw fighters
    hero_player.unit_animation.update()
    hero_player.draw(screen)
    hero_player.health_bar.draw(hero_player.current_hp, hero_player.max_hp, screen)
    hero_player.mana_bar.draw(hero_player.current_mp, hero_player.max_mp, screen)
    hero_player.fury_bar.draw(hero_player.current_fury, hero_player.max_fury, screen)

    for target_unit in target_list:
        target_unit.update()
        target_unit.draw(screen)
        target_unit.health_bar.draw(target_unit.current_hp, target_unit.max_hp, screen)

