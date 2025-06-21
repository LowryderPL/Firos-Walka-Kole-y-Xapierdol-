class Ingredient:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

class Potion:
    def __init__(self, name, ingredients, effect):
        self.name = name
        self.ingredients = ingredients
        self.effect = effect

    def brew(self):
        print(f"\nZwarzyłeś miksturę: {self.name}")
        print(f"Składniki: {', '.join(ing.name for ing in self.ingredients)}")
        print(f"Efekt: {self.effect}")

def get_ingredients():
    return [
        Ingredient("Ziele Ghula", "Rzadki"),
        Ingredient("Korzeń Mandragory", "Pospolity"),
        Ingredient("Krew Wilkołaka", "Epicki"),
        Ingredient("Oko Harpii", "Rzadki"),
        Ingredient("Pazur Bazyliszka", "Legendarny"),
    ]

def get_potions():
    ing = get_ingredients()
    return [
        Potion("Eliksir Szału", [ing[0], ing[1]], "Zwiększa atak o 20% na 3 tury."),
        Potion("Mikstura Cienia", [ing[3], ing[1]], "Zwiększa szansę na unik o 30%."),
        Potion("Krew Nocy", [ing[2], ing[4]], "Natychmiast zadaje 50 obrażeń."),
    ]

def brew_potion():
    potions = get_potions()
    print("\n=== Kocioł Alchemiczny ===")
    for idx, potion in enumerate(potions, 1):
        print(f"{idx}. {potion.name} – {potion.effect}")
    choice = input("\nWybierz numer mikstury do stworzenia: ").strip()
    try:
        selected = potions[int(choice)-1]
        selected.brew()
    except:
        print("Nieprawidłowy wybór.")
