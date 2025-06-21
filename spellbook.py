class Spell:
    def __init__(self, name, mana_cost, effect):
        self.name = name
        self.mana_cost = mana_cost
        self.effect = effect

    def cast(self):
        return f"Zaklęcie: {self.name} | Koszt many: {self.mana_cost} | Efekt: {self.effect}"


class Spellbook:
    def __init__(self):
        self.spells = [
            Spell("Kula Ognia", 5, "Zadaje 10 obrażeń obszarowych"),
            Spell("Lodowy Pocisk", 4, "Spowalnia wroga na 2 tury"),
            Spell("Tarczownik", 3, "Zwiększa pancerz o 5"),
            Spell("Dotyk Cienia", 6, "Kradnie życie wrogowi"),
            Spell("Święty Blask", 7, "Leczy 15 punktów życia"),
        ]
        self.mana = 20

    def show_spells(self):
        print("\n📖 TWOJA KSIĘGA ZAKLĘĆ:")
        for idx, spell in enumerate(self.spells, start=1):
            print(f"{idx}. {spell.cast()}")
        print(f"\n✨ Dostępna mana: {self.mana}")

    def cast_spell(self, idx):
        try:
            spell = self.spells[idx - 1]
            if self.mana >= spell.mana_cost:
                self.mana -= spell.mana_cost
                print(f"✅ Rzucono zaklęcie: {spell.name} ({spell.effect})")
                print(f"🔋 Pozostała mana: {self.mana}")
            else:
                print("❌ Za mało many.")
        except IndexError:
            print("❌ Nieprawidłowy numer zaklęcia.")


# Globalna instancja do użycia w grze
spellbook = Spellbook()


def show_spellbook():
    spellbook.show_spells()


def use_spell():
    spellbook.show_spells()
    try:
        choice = int(input("Wybierz zaklęcie do rzucenia (numer): "))
        spellbook.cast_spell(choice)
    except ValueError:
        print("❌ Błąd wyboru.")
