import tkinter as tk
from tkinter import messagebox, Toplevel

class InventoryGUI:
    def __init__(self, master, inventory, character_class):
        self.master = master
        self.master.title("Inventory")
        self.inventory = inventory
        self.character_class = character_class
        self.weight_limit = 100
        self.player_xp = 0
        self.player_level = 1
        self.theme = "day"

        self.equipped_slots = {
            "Head": None,
            "Torso": None,
            "Arms": None,
            "Legs": None,
            "Main Weapon": None,
            "Off-Hand": None,
            "Backpack": None,
            "Belt": None,
            "Amulet": None,
            "Ring Left": None,
            "Ring Right": None,
            "Rune": None
        }

        self.create_widgets()
        self.update_inventory_display()

    def create_widgets(self):
        tk.Label(self.master, text="Inventory Items:").grid(row=0, column=0)
        self.inventory_listbox = tk.Listbox(self.master, width=40)
        self.inventory_listbox.grid(row=1, column=0, rowspan=10)
        self.inventory_listbox.bind('<Double-1>', self.equip_item)
        self.inventory_listbox.bind("<Enter>", self.show_tooltip)
        self.inventory_listbox.bind("<Leave>", self.hide_tooltip)

        tk.Label(self.master, text="Equipped Items:").grid(row=0, column=1)
        self.equipped_labels = {}
        for idx, slot in enumerate(self.equipped_slots.keys()):
            tk.Label(self.master, text=f"{slot}:").grid(row=idx+1, column=1, sticky='e')
            label = tk.Label(self.master, text="None", width=30)
            label.grid(row=idx+1, column=2, sticky='w')
            self.equipped_labels[slot] = label

        self.weight_label = tk.Label(self.master, text="Total Weight: 0 / 100")
        self.weight_label.grid(row=13, column=0, sticky='w')

        self.xp_label = tk.Label(self.master, text="XP: 0 | Level: 1")
        self.xp_label.grid(row=13, column=2, sticky='e')

        self.burn_button = tk.Button(self.master, text="Burn Item for XP", command=self.burn_item)
        self.burn_button.grid(row=14, column=0, pady=5)

        self.craft_button = tk.Button(self.master, text="Open Crafting", command=self.open_crafting)
        self.craft_button.grid(row=14, column=1)

        self.alchemy_button = tk.Button(self.master, text="Open Alchemy", command=self.open_alchemy)
        self.alchemy_button.grid(row=14, column=2)

        self.theme_button = tk.Button(self.master, text="Toggle Theme", command=self.toggle_theme)
        self.theme_button.grid(row=15, column=1)

    def update_inventory_display(self):
        self.inventory_listbox.delete(0, tk.END)
        for item in self.inventory:
            color = "black"
            rarity = item.get("rarity", "common")
            if rarity == "rare": color = "blue"
            elif rarity == "epic": color = "purple"
            elif rarity == "legendary": color = "orange"
            self.inventory_listbox.insert(tk.END, f"{item['name']} [{item['type']}]")

        total_weight = sum(item['weight'] for item in self.inventory)
        self.weight_label.config(text=f"Total Weight: {total_weight} / {self.weight_limit}")
        self.xp_label.config(text=f"XP: {self.player_xp} | Level: {self.player_level}")

    def equip_item(self, event):
        selection = self.inventory_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        item = self.inventory[index]

        if self.character_class not in item.get("allowed_classes", ["All"]):
            messagebox.showwarning("Class Restriction", "Your class cannot equip this item.")
            return

        slot = item["slot"]
        self.equipped_slots[slot] = item
        self.equipped_labels[slot].config(text=item["name"])
        del self.inventory[index]
        self.update_inventory_display()

    def burn_item(self):
        selection = self.inventory_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Select an item to burn.")
            return
        index = selection[0]
        item = self.inventory.pop(index)
        xp_gain = item['value'] // 2
        self.player_xp += xp_gain
        if self.player_xp >= self.player_level * 100:
            self.player_level += 1
            self.player_xp = 0
            messagebox.showinfo("Level Up!", f"You reached Level {self.player_level}!")
        else:
            messagebox.showinfo("Item Burned", f"You gained {xp_gain} XP from burning {item['name']}.")
        self.update_inventory_display()

    def open_crafting(self):
        top = Toplevel(self.master)
        top.title("Crafting System")
        tk.Label(top, text="Crafting will be implemented here.").pack(pady=10)

    def open_alchemy(self):
        top = Toplevel(self.master)
        top.title("Alchemy System")
        tk.Label(top, text="Alchemy will be implemented here.").pack(pady=10)

    def toggle_theme(self):
        if self.theme == "day":
            self.master.configure(bg="black")
            self.theme = "night"
        else:
            self.master.configure(bg="white")
            self.theme = "day"

    def show_tooltip(self, event):
        pass  # Możesz dodać własne tooltipy np. Toplevel z opisem

    def hide_tooltip(self, event):
        pass

# Example usage
if __name__ == "__main__":
    inventory = [
        {"name": "Iron Helmet", "type": "Armor", "slot": "Head", "weight": 5, "value": 50, "allowed_classes": ["Warrior"], "rarity": "common"},
        {"name": "Steel Sword", "type": "Weapon", "slot": "Main Weapon", "weight": 10, "value": 100, "allowed_classes": ["Warrior", "Rogue"], "rarity": "epic"},
        {"name": "Magic Rune", "type": "Rune", "slot": "Rune", "weight": 2, "value": 75, "allowed_classes": ["Mage"], "rarity": "rare"},
    ]
    character_class = "Warrior"

    root = tk.Tk()
    app = InventoryGUI(root, inventory, character_class)
    root.mainloop()
