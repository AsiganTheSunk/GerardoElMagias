# from core.units.animations.animation_resolver import AnimationSet

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
        self.fury_status = False
        self.experience_status = False
        self.ultimate_status = False

        self.next_action = None

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

    def has_experience(self):
        return self.experience_status

    def has_full_fury(self):
        return self.current_fury == self.max_fury

    def has_fury(self):
        return self.fury_status

    def reset_fury(self):
        self.current_fury = 0

    def gain_health(self, input_health):
        if self.current_hp + input_health >= self.max_hp:
            gained_health = self.max_hp - self.current_hp
            self.current_hp = self.max_hp
            return gained_health

        self.current_hp += input_health
        return input_health

    def gain_mana(self, input_mana):
        if self.current_mp + input_mana >= self.max_mp:
            gained_mana = self.max_mp - self.current_mp
            self.current_mp = self.max_mp
            return gained_mana

        self.current_mp += input_mana
        return input_mana

    def gain_fury(self, input_damage):
        fury_amount = round(input_damage * 1.4)
        if self.current_fury + fury_amount >= self.max_fury:
            self.current_fury = self.max_fury
            gained_fury = self.max_fury - self.current_fury
            return gained_fury
        else:
            self.current_fury += fury_amount
            return fury_amount

    def is_dead(self):
        return self.current_hp < 1

    def death(self):
        self.current_hp = 0
        self.alive = False

    def run_next_action(self, damage_text_group):
        if self.next_action and self.next_action[0] == 'attack':
            target = self.next_action[1]
            self.attack(target, damage_text_group)
        if self.next_action and self.next_action[0] == 'use' and self.next_action[
            1] == 'healing_potion':
            self.use_healing_potion(damage_text_group)
        if self.next_action and self.next_action[0] == 'use' and self.next_action[
            1] == 'mana_potion':
            self.use_mana_potion(damage_text_group)
    # def melee_attack(self):
    #     self.unit_animation.melee_attack_animation()
    #
    # def block(self):
    #     self.unit_animation.block_animation()
    #
    # def hurt(self):
    #     self.unit_animation.hurt_animation()
    #
    # def miss(self):
    #     self.unit_animation.miss_animation()
    #
    # def idle(self):
    #     self.unit_animation.idle_animation()
    #
    # def update(self):
    #     self.unit_animation.update()
    #
    # def draw(self, screen):
    #     self.unit_animation.draw(screen)
