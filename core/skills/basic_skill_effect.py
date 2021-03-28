#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicSkillEffect:
    def __init__(self, target, caster=None):
        if caster is not None:
            # Caster Center Coordinates x,y
            self.caster_center = caster.animation_set.rect.center
        else:
            self.caster_center = caster

        # Target Center Coordinates x,y
        self.target_center = target.animation_set.rect.center
