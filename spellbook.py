class Spell:
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost  # koszt w punktach many
        self.description = description

    def cast(self):
        print(f"\nRzucasz zaklęcie: {self.name}!")
        print(self.description)
        print(f"Koszt many: {self.cost}")

class Spellbook:
    def __init__(self):
        self.spells = [
            Spell("Ognista Kula", 10, "Zadaje 30 pkt obrażeń wszystkim wrogom."),
            Spell("Leczenie", 5, "Przywraca 20 pkt zdrowia."),
            Spell("Lodowy Pocisk", 8, "Spowalnia i rani przeciwnika."),
        ]

    def list_spells(self):
        print("\n=== TWOJA KSIĘGA ZAKLĘĆ ===")
        for idx, spell in enumerate(self.spells, start=1):
            print(f"{idx}. {spell.name} – koszt: {spell.cost} – {spell.description}")

    def cast_spell(self, index):
        try:
            spell = self.spells[index - 1]
            spell.cast()
        except IndexError:
            print("Nieprawidłowy numer zaklęcia.")

    def learn_spell(self, spell):
        self.spells.append(spell)
        print(f"Nauczyłeś się nowego zaklęcia: {spell.name}!")

# Instancja globalna
spellbook = Spellbook()

# Przykład użycia w grze
def use_spellbook():
    spellbook.list_spells()
    choice = input("Wybierz numer zaklęcia do rzucenia: ").strip()
    if choice.isdigit():
        spellbook.cast_spell(int(choice))
    else:
        print("Nieprawidłowy wybór.")
