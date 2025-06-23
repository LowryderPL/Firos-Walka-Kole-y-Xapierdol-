# alchemy.py – Firos: Magic & Magic

class Recipe:
    def __init__(self, name, ingredients, result, description, category="mikstura"):
        self.name = name
        self.ingredients = ingredients
        self.result = result
        self.description = description
        self.category = category  # np. "mikstura", "zwój", "mutacja"

class Alchemy:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def list_recipes(self):
        print("\n=== RECEPTURY ALCHEMICZNE ===")
        for idx, r in enumerate(self.recipes, start=1):
            print(f"{idx}. [{r.category.upper()}] {r.name} → {r.result}")
            print(f"   Składniki: {', '.join(r.ingredients)}")
            print(f"   Opis: {r.description}")

    def craft(self, ingredients):
        for recipe in self.recipes:
            if sorted(recipe.ingredients) == sorted(ingredients):
                print(f"\n🧪 Udało się stworzyć: {recipe.result}!")
                print(f"Opis: {recipe.description}")
                return recipe.result
        print("❌ Nie udało się stworzyć mikstury. Sprawdź składniki.")
        return None

# Globalna instancja
alchemy = Alchemy()

# === 🔮 LISTA PRZYKŁADOWYCH RECEPTUR ===

alchemy.add_recipe(Recipe(
    name="Mikstura Leczenia",
    ingredients=["ziele", "grzyb", "woda"],
    result="mikstura_leczenia",
    description="Przywraca 50 punktów życia.",
    category="mikstura"
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
    description="Uczy zaklęcia Lodowy Wybuch (spowalnia i rani).",
    category="zwój"
))

alchemy.add_recipe(Recipe(
    name="Mikstura Mutacji",
    ingredients=["krew", "cień", "ziele"],
    result="mikstura_mutacji",
    description="Tymczasowo zwiększa siłę, ale obniża obronę.",
    category="mutacja"
))

alchemy.add_recipe(Recipe(
    name="Zwój Teleportacji",
    ingredients=["popiół", "runiczny_papier", "woda"],
    result="scroll_teleport",
    description="Teleportuje gracza do ostatniego miasta.",
    category="zwój"
))

# === Interfejs użytkownika ===
def alchemy_interface():
    print("\n🔬 Masz dostęp do stołu alchemicznego.")
    alchemy.list_recipes()
    chosen = input("Podaj składniki oddzielone przecinkiem (np. ziele,woda,grzyb): ").strip()
    ingredients = [i.strip().lower() for i in chosen.split(",")]
    alchemy.craft(ingredients)

# Testowy interfejs (do uruchomienia oddzielnie)
if __name__ == "__main__":
    alchemy_interface()
