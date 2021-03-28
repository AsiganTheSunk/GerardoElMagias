#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ClassSound:
    def __init__(self, class_name, sounds):
        self.class_name = class_name
        self.sounds = sounds

        self.attack_sound = sounds['fx']['attacks']['hit_cut']
        self.critical_attack_sound = sounds['fx']['attacks']['critical_hit_cut']
        self.hurt_sound = None
        self.block_sound = sounds['fx']['attacks']['miss']
        self.miss_sound = sounds['fx']['attacks']['miss']
