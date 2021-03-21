#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


class Affix:
    def __init__(self, name, item_level, attribute_type, minimum_attribute, maximum_attribute, allowed_item_type):
        self.name = name
        self.item_level = item_level

        self.attribute_type = attribute_type
        self.attribute_value = randint(minimum_attribute, maximum_attribute)
        self.allowed_item_type = allowed_item_type
