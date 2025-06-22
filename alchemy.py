class Ingredient:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

class Potion:
    def __init__(self, name, ingredients, effect, description):
        self.name = name
        self.ingredients = ingredients
        self.effect = effect
        self.description = description

    def show_info(self):
        print(f"\n🧪 {self.name}")
        print(f"Efekt: {self.effect}")
        print(f"Składniki: {', '.join(self.ingredients)}")
        print(f"Opis: {self.description}")

def get_potions():
    return [
        Potion("Eliksir Życia", ["Zioło Miłości", "Krew Trolla"], "+50 HP", "Przywraca zdrowie na polu bitwy."),
        Potion("Mikstura Cienia", ["Czarna Orchidea", "Proch Nocy"], "+25 do skradania", "Umożliwia niezauważone przejścia."),
        Potion("Napój Furii", ["Serce Smoka", "Ząb Wilkołaka"], "+40 DMG na 3 tury", "Rytualny napój barbarzyńców."),
        Potion("Mikstura Mrozu", ["Lód Wieczności", "Oko Bazyliszka"], "Zamraża przeciwnika na 1 turę", "Magiczny eliksir używany w starożytnych bitwach."),
    ]

def brew_potion(selected_ingredients):
    potions = get_potions()
    for p in potions:
        if set(p.ingredients) == set(selected_ingredients):
            return p
    return None

def show_alchemy_lab():
    print("\n🔬 Witamy w Laboratorium Alchemii")
    potions = get_potions()
    for i, p in enumerate(potions, 1):
        print(f"{i}. {p.name} - {p.effect}")
    choice = input("Wybierz miksturę, by zobaczyć szczegóły: ")
    try:
        potions[int(choice)-1].show_info()
    except:
        print("Niepoprawny wybór.")
