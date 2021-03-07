class Stash:
    def __init__(self, healing_potions=2, mana_potions=2, gold=0):
        self.healing_potions = healing_potions
        self.mana_potions = mana_potions
        self.gold = gold

        self.items = []

    def has_healing_potion(self):
        if self.healing_potions >= 1:
            return True
        return False

    def has_mana_potion(self):
        if self.mana_potions >= 1:
            return True
        return False

    def has_enough_gold(self, gold_value):
        if self.gold >= gold_value:
            return True
        return False

    def add_gold(self, item_number):
        self.gold += item_number

    def add_lightning(self, item_number):
        self.mana_potions += item_number

    def add_healing_potion(self, item_number):
        self.healing_potions += item_number

    def add_mana_potion(self, item_number):
        self.mana_potions += item_number

    def consume_healing_potion(self):
        self.healing_potions -= 1

    def consume_mana_potion(self):
        self.mana_potions -= 1

    def consume_gold(self, item_number):
        self.gold -= item_number


