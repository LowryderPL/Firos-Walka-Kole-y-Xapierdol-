class Creature:
    def __init__(self, name, level, health, attack, rarity, loot):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.rarity = rarity  # 'powszechny', 'rzadki', 'epicki', 'legendarny'
        self.loot = loot      # np. {"Ząb Wilka": 1, "Złoto": 50}

    def __str__(self):
        return f"{self.name} (Lvl {self.level}) – HP: {self.health}, ATK: {self.attack}, Rzadkość: {self.rarity}"

class Bestiary:
    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        self.creatures.append(creature)
        print(f"📚 Dodano do bestiariusza: {creature.name}")

    def list_creatures(self):
        print("\n=== Bestiariusz ===")
        if not self.creatures:
            print("Brak wpisów.")
            return
        for i, c in enumerate(self.creatures, 1):
            print(f"{i}. {c}")

    def find_by_level(self, min_lvl, max_lvl):
        return [c for c in self.creatures if min_lvl <= c.level <= max_lvl]

# Przykład testowy:
if __name__ == "__main__":
    bestiary = Bestiary()
    bestiary.add_creature(Creature("Wilk", 2, 30, 5, "powszechny", {"Skóra Wilka": 1, "Złoto": 10}))
    bestiary.add_creature(Creature("Upiór Cienia", 7, 120, 18, "epicki", {"Ektoplazma": 1, "Mroczny Kamień": 1}))
    bestiary.list_creatures()
