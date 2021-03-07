from units.unit_animation import UnitAnimation


class BasicUnit:
    def __init__(self, x, y, name, level, max_hp, max_mp, strength, dexterity, magic):

        # Basic Unit Coordinates x,y
        self.x = x
        self.y = y

        # Basic Unit Name
        self.name = name

        # Basic Unit Stats
        self.level = level

        # Basic Resource Stats: Fury, Mana, Health
        self.max_fury = 100
        self.current_fury = 0
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mp = max_mp
        self.current_mp = self.max_mp

        # Basic Attribute Stats: Strength, Dexterity, Magic, Intellect
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.intellect = 1

        # Basic Unit Status
        self.alive = True

        # Basic Unit Animation Resource
        self.unit_animation = UnitAnimation(self.x, self.y, self.name)

    def reduce_health(self, input_health):
        if self.current_hp - input_health < 0:
            self.current_hp = 0
        else:
            self.current_hp -= input_health

    def reduce_mana(self, input_mana):
        if self.current_mp >= input_mana:
            # Consume Mana: Spell Casting
            self.current_mp -= input_mana
            return True
        return False

    def reset_fury(self):
        self.current_fury = 0

    def gain_health(self, input_health):
        if self.current_hp + input_health >= self.max_hp:
            self.current_hp = self.max_hp
            return self.max_hp - self.current_mp

        self.current_hp += input_health
        return input_health

    def gain_mana(self, input_mana):
        if self.current_mp + input_mana >= self.max_mp:
            self.current_mp = self.max_mp
            return self.max_mp - self.current_mp

        self.current_mp += input_mana
        return input_mana

    def gain_fury(self, input_damage):
        fury_amount = round(input_damage * 1.5)
        if self.current_fury + fury_amount >= 100:
            self.current_fury = 100
        else:
            self.current_fury += fury_amount

    def is_dead(self):
        if self.current_hp < 1:
            return True
        return False

    def death(self):
        self.current_hp = 0
        self.alive = False
        self.unit_animation.death_animation()

    def melee_attack(self):
        self.unit_animation.melee_attack_animation()

    def block(self):
        self.unit_animation.block_animation()

    def hurt(self):
        self.unit_animation.hurt_animation()

    def dodge(self):
        self.unit_animation.dodge_animation()

    def idle(self):
        self.unit_animation.idle_animation()

    def update(self):
        self.unit_animation.update()

    def draw(self, screen):
        self.unit_animation.draw(screen)
