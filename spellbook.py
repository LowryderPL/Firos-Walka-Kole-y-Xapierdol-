# spellbook.py – Firos: Magic & Magic (wersja z systemem many)

from mana_system import ManaManager

class Spell:
    def __init__(self, name, cost, description, school="uniwersalna", difficulty="łatwe", effect=""):
        self.name = name
        self.cost = cost
        self.description = description
        self.school = school
        self.difficulty = difficulty
        self.effect = effect

    def cast(self, mana_manager: ManaManager):
        if mana_manager.spend_mana(self.cost):
            print(f"\n🔮 Rzucasz zaklęcie: {self.name}!")
            print(f"Opis: {self.description}")
            print(f"Szkoła: {self.school} | Poziom: {self.difficulty}")
            if self.effect:
                print(f"Efekt specjalny: {self.effect}")
        else:
            print("❌ Nie udało się rzucić zaklęcia.")

class Spellbook:
    def __init__(self, mana_manager: ManaManager):
        self.spells = []
        self.mana_manager = mana_manager
        self._add_default_spells()

    def _add_default_spells(self):
        self.spells = [
            Spell("Ognista Kula", 10, "Zadaje 30 obrażeń.", "ogień", "łatwe", "podpalenie"),
            Spell("Leczenie", 5, "Przywraca 20 HP.", "życie", "łatwe"),
            Spell("Lodowy Pocisk", 8, "Zamraża przeciwnika.", "lód", "średnie", "spowolnienie"),
            Spell("Teleportacja", 15, "Przenosi do miasta.", "przestrzeń", "trudne")
        ]

    def list_spells(self):
        print("\n📖 TWOJA KSIĘGA ZAKLĘĆ")
        if not self.spells:
            print("Brak zaklęć.")
            return
        for idx, spell in enumerate(self.spells, 1):
            print(f"{idx}. {spell.name} ({spell.school}, {spell.difficulty}) – koszt: {spell.cost} MANA")

    def cast_spell(self, index):
        try:
            spell = self.spells[index - 1]
            spell.cast(self.mana_manager)
        except IndexError:
            print("❌ Nieprawidłowy numer zaklęcia.")

    def learn_spell(self, spell):
        for s in self.spells:
            if s.name == spell.name:
                print(f"⚠️ Już znasz to zaklęcie: {spell.name}")
                return
        self.spells.append(spell)
        print(f"📘 Nauczyłeś się nowego zaklęcia: {spell.name}!")

# Test gry z many
if __name__ == "__main__":
    mana = ManaManager(max_mana=40)
    book = Spellbook(mana)

    while True:
        mana.show()
        book.list_spells()
        choice = input("Wybierz numer zaklęcia do rzucenia (lub X): ").strip().lower()
        if choice == "x":
            break
        elif choice.isdigit():
            book.cast_spell(int(choice))
        else:
            print("Nieprawidłowy wybór.")
