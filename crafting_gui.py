
# crafting_gui.py
import tkinter as tk
from crafting import CraftingSystem
from inventory import Inventory

class CraftingGUI:
    def __init__(self, root, inventory):
        self.root = root
        self.system = CraftingSystem(inventory)
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Crafting System")
        self.label.pack()
        self.items_list = tk.Listbox(self.frame)
        self.items_list.pack()
        self.craft_button = tk.Button(self.frame, text="Craft", command=self.craft_selected)
        self.craft_button.pack()
        self.refresh()

    def refresh(self):
        self.items_list.delete(0, tk.END)
        for item in self.system.get_craftable_items():
            self.items_list.insert(tk.END, item)

    def craft_selected(self):
        selection = self.items_list.curselection()
        if not selection:
            return
        item_name = self.items_list.get(selection[0])
        if self.system.craft(item_name):
            self.refresh()

if __name__ == "__main__":
    root = tk.Tk()
    inv = Inventory()
    inv.add_item("Iron Ore", 3)
    inv.add_item("Wood", 1)
    gui = CraftingGUI(root, inv)
    root.mainloop()
