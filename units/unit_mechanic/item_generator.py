from random import randint

level = randint(1, 30)
base_mf = 0

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
    def __init__(self):
        self.rarity_probabilities = [60, 75, 80, 95]

    def get_item_type(self):
        item_type = ['Shield', 'Armor', 'Weapon', "Amulet"]
        weapon_index = randint(0, len(item_type) - 1)
        return item_type[weapon_index]

    def get_base_item(self, level, item_type):
        drop_item_pool = []
        for index, base_item in enumerate(base_item_pool[item_type]):
            if base_item[2] < level:
                drop_item_pool.append(base_item)

        randomize = randint(0, len(drop_item_pool) - 1)
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


item_generator = ItemGenerator()
item_type = item_generator.get_item_type()
item_rarity = item_generator.roll_rarity(base_mf, item_type)
base_item = item_generator.get_base_item(level, item_type)

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
