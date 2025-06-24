# alchemy.py – Firos: Magic & Magic (pełna wersja z plecakiem i zwojami)

from scrolls import Scroll
from spellbook import Spell
from backpack import Backpack

class Recipe:
    def __init__(self, name, ingredients, result, description, category="mikstura"):
        self.name = name
        self.ingredients = ingredients
        self.result = result
        self.description = description
        self.category = category  # "mikstura", "zwój", "mutacja", itd.

class Alchemy:
    def __init__(self):
        self.recipes = []
        self.backpack = Backpack()

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def list_recipes(self):
        print("\n=== 📘 RECEPTURY ALCHEMICZNE ===")
        for idx, r in enumerate(self.recipes, start=1):
            print(f"{idx}. [{r.category.upper()}] {r.name} → {r.result}")
            print(f"   Składniki: {', '.join(r.ingredients)}")
            print(f"   Opis: {r.description}")

    def craft(self, ingredients):
        for recipe in self.recipes:
            if sorted(recipe.ingredients) == sorted(ingredients):
                print(f"\n🧪 Stworzyłeś: {recipe.result}!")
                print(f"Opis: {recipe.description}")

                # === Dodaj wynik do plecaka ===
                if recipe.category == "zwój":
                    spell_map = {
                        "scroll_fireball": Spell("Ognista Kula", 10, "Zadaje 30 obrażeń wszystkim wrogom.",
                                                 school="ogień", difficulty="łatwe", effect="podpalenie"),
                        "scroll_frostblast": Spell("Lodowy Wybuch", 8, "Zamraża przeciwnika.",
                                                   school="lód", difficulty="średnie", effect="spowolnienie"),
                        "scroll_teleport": Spell("Teleportacja", 15, "Przenosi gracza do miasta.",
                                                 school="przestrzeń", difficulty="trudne", effect="natychmiastowy ruch")
                    }
                    spell = spell_map.get(recipe.result)
                    if spell:
                        new_scroll = Scroll(recipe.name, spell, recipe.description)
                        self.backpack.add_scroll(new_scroll)
                elif recipe.category == "mikstura" or recipe.category == "mutacja":
                    self.backpack.add_ingredient(recipe.result)
                return recipe.result

        print("❌ Nie udało się stworzyć mikstury. Sprawdź składniki.")
        return None

# === INSTANCJA ===
alchemy = Alchemy()

# === RECEPTURY ===
alchemy.add_recipe(Recipe(
    name="Mikstura Leczenia",
    ingredients=["ziele", "grzyb", "woda"],
    result="mikstura_leczenia",
    description="Przywraca 50 punktów życia.",
    category="mikstura"
))

alchemy.add_recipe(Recipe(
    name="Mikstura Mutacji",
    ingredients=["krew", "cień", "ziele"],
    result="mikstura_mutacji",
    description="Zwiększa siłę, zmniejsza obronę.",
    category="mutacja"
))

alchemy.add_recipe(Recipe(
    name="Zwój Ognistej Kuli",
    ingredients=["proch", "krew", "pergamin"],
    result="scroll_fireball",
    description="Uczy zaklęcia Ognista Kula.",
    category="zwój"
))

alchemy.add_recipe(Recipe(
    name="Zwój Lodowego Wybuchu",
    ingredients=["lód", "popiół", "pergamin"],
    result="scroll_frostblast",
    description="Uczy zaklęcia Lodowy Wybuch.",
    category="zwój"
))

alchemy.add_recipe(Recipe(
    name="Zwój Teleportacji",
    ingredients=["popiół", "runiczny_papier", "woda"],
    result="scroll_teleport",
    description="Teleportuje gracza do ostatniego miasta.",
    category="zwój"
))

# === INTERFEJS ===
def alchemy_interface():
    print("\n🧪 STÓŁ ALCHEMICZNY")
    alchemy.list_recipes()
    chosen = input("Podaj składniki oddzielone przecinkiem: ").strip()
    ingredients = [i.strip().lower() for i in chosen.split(",")]
    alchemy.craft(ingredients)
    alchemy.backpack.show()

# Test lokalny
if __name__ == "__main__":
    alchemy_interface()
