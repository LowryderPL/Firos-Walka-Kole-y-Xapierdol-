class Recipe:
    def __init__(self, name, ingredients, result, description):
        self.name = name
        self.ingredients = ingredients
        self.result = result
        self.description = description

class Alchemy:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def list_recipes(self):
        print("\n=== RECEPTURY ALCHEMICZNE ===")
        for idx, r in enumerate(self.recipes, start=1):
            print(f"{idx}. {r.name} → {r.result}")
            print(f"   Składniki: {', '.join(r.ingredients)}")
            print(f"   Opis: {r.description}")

    def craft(self, ingredients):
        for recipe in self.recipes:
            if sorted(recipe.ingredients) == sorted(ingredients):
                print(f"\nUdało się stworzyć: {recipe.result}!")
                print(f"Opis: {recipe.description}")
                return recipe.result
        print("Nie udało się stworzyć mikstury. Sprawdź składniki.")
        return None

# Globalna instancja
alchemy = Alchemy()

# Dodajemy przykładowe receptury
alchemy.add_recipe(Recipe(
    name="Mikstura Leczenia",
    ingredients=["ziele", "grzyb", "woda"],
    result="mikstura_leczenia",
    description="Przywraca 50 punktów życia."
))

alchemy.add_recipe(Recipe(
    name="Zwój Ognistej Kuli",
    ingredients=["proch", "krew", "pergamin"],
    result="scroll_fireball",
    description="Uczy zaklęcia Ognista Kula (Fireball)."
))

# Przykład użycia
def alchemy_interface():
    print("Masz dostęp do stołu alchemicznego.")
    alchemy.list_recipes()
    chosen = input("Podaj składniki oddzielone przecinkiem: ").strip()
    ingredients = [i.strip().lower() for i in chosen.split(",")]
    alchemy.craft(ingredients)
