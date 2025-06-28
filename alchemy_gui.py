import tkinter as tk
from tkinter import messagebox
from alchemy import AlchemySystem

class AlchemyGUI:
    def __init__(self, root, inventory, player_stats):
        self.root = root
        self.alchemy = AlchemySystem(inventory, player_stats)
        self.root.title("🧪 Alchemia - Firos")
        self.root.geometry("520x420")
        self.root.configure(bg="#111")

        self.selected_recipe = tk.StringVar()
        self.message = tk.StringVar()

        self._build_interface()

    def _build_interface(self):
        tk.Label(self.root, text="Wybierz eliksir do uwarzenia:", fg="white", bg="#111", font=("Helvetica", 12)).pack(pady=10)

        recipes = list(self.alchemy.recipes.keys())
        if recipes:
            self.selected_recipe.set(recipes[0])
        self.dropdown = tk.OptionMenu(self.root, self.selected_recipe, *recipes)
        self.dropdown.config(bg="#333", fg="white", font=("Helvetica", 10))
        self.dropdown["menu"].config(bg="#222", fg="white")
        self.dropdown.pack(pady=5)

        self.info_label = tk.Label(self.root, text="", fg="#ccc", bg="#111", font=("Helvetica", 10))
        self.info_label.pack(pady=5)

        tk.Button(self.root, text="Uwarz eliksir", command=self.brew_potion, bg="#6a3", fg="white", font=("Helvetica", 11, "bold")).pack(pady=10)
        tk.Label(self.root, textvariable=self.message, fg="#4caf50", bg="#111", wraplength=460, font=("Helvetica", 10)).pack(pady=10)

        tk.Button(self.root, text="Zamknij", command=self.root.quit, bg="#a22", fg="white").pack(pady=5)

        self.selected_recipe.trace("w", self.update_info)
        self.update_info()

    def update_info(self, *args):
        name = self.selected_recipe.get()
        if name:
            recipe = self.alchemy.recipes[name]
            ingredients = ", ".join(f"{item} x{qty}" for item, qty in recipe["ingredients"].items())
            effect = recipe["effect"]
            self.info_label.config(text=f"Składniki: {ingredients}\nEfekt: {effect}")

    def brew_potion(self):
        name = self.selected_recipe.get()
        result = self.alchemy.brew(name)
        self.message.set(result)
        self.update_info()

# Test lokalny (odkomentuj, jeśli chcesz uruchomić)
# if __name__ == "__main__":
#     inventory = {
#         "Zioła": 5,
#         "Krew Trolla": 2,
#         "Esencja Ognia": 1
#     }
#     stats = {"alchemy_lvl": 3}
#     root = tk.Tk()
#     app = AlchemyGUI(root, inventory, stats)
#     root.mainloop()
