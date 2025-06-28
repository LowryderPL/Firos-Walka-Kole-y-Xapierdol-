crafting.py — System Rzemiosla FIROS: Magic & Magic

from random import randint, choice

Przykładowe składniki i receptury

MATERIALS = { "Żelazo": 10, "Mithril": 2, "Runiczny Pył": 5, "Drewno": 15, "Skóra": 8, "Zwoj Ognia": 1, "Kryształ Cienia": 1 }

RECIPES = { "Miecz Płomieni": { "Żelazo": 3, "Zwoj Ognia": 1 }, "Pancerz Cienia": { "Skóra": 4, "Kryształ Cienia": 1 }, "Runiczna Laska": { "Drewno": 3, "Runiczny Pył": 2 } }

Magia tworzenia i sukcesu

class CraftingSystem: def init(self, player_inventory): self.inventory = player_inventory

def can_craft(self, item_name):
    if item_name not in RECIPES:
        return False
    for material, amount in RECIPES[item_name].items():
        if self.inventory.get(material, 0) < amount:
            return False
    return True

def craft(self, item_name):
    if not self.can_craft(item_name):
        return f"Nie masz wymaganych materiałów do stworzenia: {item_name}"

    success_chance = 90  # procent
    if randint(1, 100) > success_chance:
        return f"Tworzenie {item_name} nie powiodło się. Materiały stracone."

    for material, amount in RECIPES[item_name].items():
        self.inventory[material] -= amount

    self.inventory[item_name] = self.inventory.get(item_name, 0) + 1
    return f"Stworzono: {item_name}!"

def list_recipes(self):
    return [f"{item}: {materials}" for item, materials in RECIPES.items()]

Przykład użycia

def test(): inventory = { "Żelazo": 5, "Zwoj Ognia": 1, "Skóra": 10, "Kryształ Cienia": 2, "Drewno": 10, "Runiczny Pył": 4 } crafter = CraftingSystem(inventory) print(crafter.list_recipes()) print(crafter.craft("Miecz Płomieni")) print(crafter.craft("Pancerz Cienia"))

if name == "main": test()

