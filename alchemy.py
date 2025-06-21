class Ingredient:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def describe(self):
        return f"{self.name} – {self.effect}"


class Potion:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def brew(self):
        effects = ", ".join([ing.effect for
