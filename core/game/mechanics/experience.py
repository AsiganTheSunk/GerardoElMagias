#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.game.text.damage_text import DamageText
from core.game.battle.combat.combat_utils import get_alive_targets_status

damage_text = DamageText()


class ExperienceMaster:
    @staticmethod
    def evaluate_kill(caster, target, text_sprite):
        if not target.alive:
            caster.experience_to_gain += target.level
            damage_text.cast(caster, "+EXP!", text_sprite)

    @staticmethod
    def evaluate_group_kill(caster, target_list, pre_target_list, post_target_list, text_sprite):
        for index, target_unit in enumerate(post_target_list):
            if pre_target_list[index] is True and post_target_list[index] is False:
                caster.experience_to_gain += target_list[index].level
                damage_text.cast(caster, "+EXP!", text_sprite)

    def aoe_experience_helper(self, caster, target_list, aoe_spell, text_sprite):
        # Pre Save State for Enemy List: target_list
        pre_target_list = get_alive_targets_status(target_list)

        # Cast Spell
        aoe_spell(caster, target_list, text_sprite)

        # Post Save State for Enemy List: target_list
        pos_target_list = get_alive_targets_status(target_list)

        # Evaluate Kills
        self.evaluate_group_kill(caster, target_list, pre_target_list, pos_target_list, text_sprite)