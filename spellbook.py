class Spell:
    def __init__(self, name, effect, cost):
        self.name = name
        self.effect = effect
        self.cost = cost

    def cast(self):
        print(f"\n>> Rzucasz zaklęcie: {self.name}")
        print(f"Efekt: {self.effect}")
        print(f"Koszt many: {self.cost} 🪄")

def get_spellbook():
    return [
        Spell("Płomień Igni", "Zadaje 30 obrażeń ognistych.", 5),
        Spell("Tarcza Quen", "Pochłania następny atak.", 4),
        Spell("Zamrożenie Aard", "Zatrzymuje wroga na 1 turę.", 6),
        Spell("Zdrada Axii", "Kontrolujesz umysł przeciwnika przez 1 turę.", 8),
        Spell("Oczyszczenie Yrden", "Zmniejsza odporność wroga na magię.", 7),
        Spell("Uzdrowienie Natury", "Przywraca 40 punktów życia.", 6),
        Spell("Więzy Krwi", "Poświęć 20 HP, by zadać 40 obrażeń.", 0),
    ]

def use_spell():
    spellbook = get_spellbook()
    print("\n=== TWOJA KSIĘGA ZAKLĘĆ ===")
    for idx, spell in enumerate(spellbook, start=1):
        print(f"{idx}. {spell.name} (Koszt: {spell.cost}) – {spell.effect}")
    
    choice = input("\nWybierz numer zaklęcia do rzucenia: ").strip()
    try:
        selected = spellbook[int(choice)-1]
        selected.cast()
    except (IndexError, ValueError):
        print("Nieprawidłowy wybór zaklęcia.")
