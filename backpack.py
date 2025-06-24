# backpack.py – System przechowywania zwojów, składników i artefaktów

from scrolls import get_scrolls
from inventory import Item

class Backpack:
    def __init__(self):
        self.scrolls = []      # lista zwojów
        self.ingredients = []  # lista składników
        self.artifacts = []    # lista przedmiotów (Item)

    def add_scroll(self, scroll):
        self.scrolls.append(scroll)
        print(f"📜 Dodano zwój: {scroll.name}")

    def add_ingredient(self, name):
        self.ingredients.append(name)
        print(f"🌿 Dodano składnik: {name}")

    def add_artifact(self, item: Item):
        self.artifacts.append(item)
        print(f"🗡️ Dodano artefakt: {item.name} ({item.rarity})")

    def show(self):
        print("\n🎒 ZAWARTOŚĆ PLECAKA")

        print("\n📜 Zwoje:")
        if self.scrolls:
            for i, s in enumerate(self.scrolls, 1):
                status = "✅" if s.used else "❌"
                print(f"{i}. {status} {s.name} – {s.description}")
        else:
            print("Brak zwojów.")

        print("\n🌿 Składniki:")
        if self.ingredients:
            for i, ing in enumerate(self.ingredients, 1):
                print(f"{i}. {ing}")
        else:
            print("Brak składników.")

        print("\n🗡️ Artefakty:")
        if self.artifacts:
            for i, art in enumerate(self.artifacts, 1):
                print(f"{i}. {art.name} ({art.rarity}) – Moc: {art.power}")
        else:
            print("Brak artefaktów.")

# Przykład testowy
if __name__ == "__main__":
    from scrolls import Scroll
    from spellbook import Spell

    backpack = Backpack()

    # Dodaj przykładowe zwój
    example_scroll = Scroll("Zwój Ognistej Kuli", Spell("Ognista Kula", 10, "Zadaje 30 dmg"), "Pergamin z płomiennym symbolem.")
    backpack.add_scroll(example_scroll)

    # Dodaj składniki
    backpack.add_ingredient("ziele")
    backpack.add_ingredient("popiół")

    # Dodaj artefakt
    item = Item(name="Amulet Ognia", rarity="epic", power=7, slot="artifact")
    backpack.add_artifact(item)

    # Pokaż całość
    backpack.show()
