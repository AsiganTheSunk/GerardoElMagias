from random import randint

level = randint(1, 30)
base_mf = 0


class Shield:
    def __init__(self, name, item_lvl, block_chance):
        self.name = name
        self.item_lvl = item_lvl
        self.block_chance = block_chance


class Weapon:
    def __init__(self, name, weapon_subclass, minimum_damage, maximum_damage, item_lvl):
        self.name = name
        self.weapon_subclass = weapon_subclass
        self.item_lvl = item_lvl
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage


class Armor:
    def __init__(self, name, item_lvl, armor):
        self.name = name
        self.item_lvl = item_lvl
        self.armor = armor


class Amulet:
    def __init__(self, name, item_lvl):
        self.name = name
        self.item_lvl = item_lvl

items_pool = {
    # Name, block chance, itemlvl
    'Shield': [Shield('Rodela', 20, 2), Shield('Defensor', 25, 7), Shield('Aegis', 30, 13), Shield('Guardian', 35, 17),
               Shield("Escudo forjado en el infierno", 45, 25)],

    #Name, defense, itemlvl
    'Armor': [Armor('Harapos', 1, 1), Armor('Armadura de cuero', 5, 4), Armor('Coraza', 10, 8), Armor('Cota de malla', 15, 12),
              Armor('Piel de balrog', 20, 16), Armor('Armadura forjada en el infierno', 30, 25)],

    #Name, weaponclass, minimum damage, maximum damage, itemlvl
    "Weapon": [Weapon("Puñal", "Espada", 1, 2, 1), Weapon("Daga", "Espada", 1, 4, 1),
               Weapon("Espada corta", "Espada", 2, 5, 3), Weapon("Lanza", "Lanza", 1, 6, 3), Weapon("Espada larga", "Espada", 3, 6, 5),
               Weapon("Pica", "Lanza", 2, 7, 5), Weapon("Hacha", "Hacha", 3, 8, 8), Weapon("Espada bastarda", "Espada", 6, 9, 10),
               Weapon("Hacha doble", "Hacha", 3, 10, 10), Weapon("Látigo", "Látigo", 1, 15, 12), Weapon("Alabarda", "Lanza", 5, 11, 12),
               Weapon("Gladius", "Espada", 8, 12, 14), Weapon("Partisana", "Lanza", 5, 14, 14), Weapon("Mandoble", "Espada", 9, 13, 16),
               Weapon("Decapitador", "Hacha", 6, 15, 16), Weapon("Espada forjada en el infierno", "Espada", 12, 18, 25)],
    "Amulet": [Amulet("Amulet", 1)]
}

base_item_pool = {

    # Name, block chance, itemlvl
    'Shield': [('Rodela', 20, 2), ('Defensor', 25, 7), ('Aegis', 30, 13), ('Guardian', 35, 17),
               ("Escudo forjado en el infierno", 45, 25)],

    # Name, defense, itemlvl
    'Armor': [('Harapos', 1, 1), ('Armadura de cuero', 5, 4), ('Coraza', 10, 8), ('Cota de malla', 15, 12),
              ('Piel de balrog', 20, 16), ('Armadura forjada en el infierno', 30, 25)],

    # Name, weaponclass, itemlevel, maximum damage, minimum damage
    "Weapon": [("Puñal", "Espada", 1, 2, 1), ("Daga", "Espada", 1, 4, 1),
               ("Espada corta", "Espada", 3, 5, 2), ("Lanza", "Lanza", 3, 6, 1), ("Espada larga", "Espada", 5, 6, 3),
               ("Pica", "Lanza", 5, 7, 2), ("Hacha", "Hacha", 8, 8, 3), ("Espada bastarda", "Espada", 10, 9, 6),
               ("Hacha doble", "Hacha", 10, 10, 3), ("Látigo", "Látigo", 12, 15, 1), ("Alabarda", "Lanza", 12, 11, 5),
               ("Gladius", "Espada", 14, 12, 8), ("Partisana", "Lanza", 14, 14, 5), ("Mandoble", "Espada", 16, 13, 9),
               ("Decapitador", "Hacha", 16, 15, 6), ("Espada forjada en el infierno", "Espada", 25, 18, 12)],

    "Amulet": [("Amulet", 1, 1)],
}


class ItemGenerator:
    def get_item_type(self):
        item_type = ['Shield', 'Armor', 'Weapon', "Amulet"]
        weapon_index = randint(0, len(item_type) - 1)
        return item_type[weapon_index]

    def get_base_item2(self, level, item_type, base_item_pool):
        drop_item_pool = []
        for index, base_item in enumerate(base_item_pool[item_type]):
            if base_item.item_lvl < level:
                drop_item_pool.append(base_item)

        print(drop_item_pool)
        if len(drop_item_pool) >= 1:
            randomize = randint(0, len(drop_item_pool) - 1)
        else:
            randomize = 0

        selected_base_item = drop_item_pool[randomize]
        return selected_base_item

    def get_base_item(self, level, item_type):
        drop_item_pool = []
        for index, base_item in enumerate(base_item_pool[item_type]):
            if base_item[2] < level:
                drop_item_pool.append(base_item)

        print(drop_item_pool)
        if len(drop_item_pool) >= 1:
            randomize = randint(0, len(drop_item_pool) - 1)
        else:
            randomize = 0

        selected_base_item = drop_item_pool[randomize]
        return selected_base_item

    def roll_rarity(self, base_mf, item_type):
        converted_mf = 1 + (base_mf / 100)

        rand = randint(1, 100)
        if rand < 3 * converted_mf:
            item_rarity = ("Unique")
            return item_rarity

        rand = randint(1, 100)
        if rand < 8 * converted_mf:
            item_rarity = ("Rare")
            return item_rarity

        rand = randint(1, 100)
        if rand < 20 * converted_mf:
            item_rarity = ("Magical")
            return item_rarity

        else:
            item_rarity = ("Normal")
            return item_rarity

#
#item_type = item_generator.get_item_type()
#item_rarity = item_generator.roll_rarity(base_mf, item_type)
#base_item = item_generator.get_base_item(level, item_type)

item_generator = ItemGenerator()
item_type = item_generator.get_item_type()
item_rarity = item_generator.roll_rarity(base_mf, item_type)
base_item = item_generator.get_base_item2(level, item_type, items_pool)

print(item_type, item_rarity, base_item.item_lvl, base_item.name)

print(f'Monster level: {level}')
print(f"MF: {base_mf}")
print("============================================")
print(item_type)
print(base_item[0])
if item_type == "Shield":
    print(f"Bloqueo: {base_item[1]}")
if item_type == "Armor":
    print(f"Defensa: {base_item[1]}")
if item_type == "Weapon":
    print(f"Daño: de {base_item[4]} a {base_item[3]}")

print(f"Calidad: {item_rarity}")
print("============================================")


affix_pool = {
    'strength_type': {
        'Cruel': {'stat': randint(1, 3), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 1},
        'Bestial': {'stat': randint(4, 6), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 10},
        'Mortal': {'stat': randint(7, 10), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 20},
    },
    'magic_type': {
        'Brillante': {'stat': randint(1, 3), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 1},
        'Reluciente': {'stat': randint(4, 6), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 10},
        'Resplandeciente': {'stat': randint(7, 10), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 20},
    }
}

suffix_pool = {
    'dexterity_type': {
        'del Macaco': {'stat': randint(1, 3), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 1},
        'del Mono': {'stat': randint(4, 6), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 10},
        'del Huron': {'stat': randint(7, 10), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 20},
    },
    'health_type': {
        'de Vida': {'stat': randint(5, 15), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 1},
        'de Vitalidad': {'stat': randint(16, 30), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 10},
        'de Matusalén': {'stat': randint(31, 50), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 20},
    },
    'mana_type': {
        'de Mago': {'stat': randint(5, 10), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 1},
        'de Brujo': {'stat': randint(11, 25), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 10},
        'de Merlín': {'stat': randint(26, 40), 'allowed_types': ['Shield', 'Armor', 'Weapon'], 'minimum_ilvl': 20},
    }
}


