
import tkinter as tk
from tkinter import messagebox, ttk

class MarketplaceGUI(tk.Tk):
    def __init__(self, user_inventory, listings):
        super().__init__()
        self.title("Marketplace - Firos Magic & Magic")
        self.geometry("800x600")
        self.configure(bg="#1e1e1e")
        self.user_inventory = user_inventory
        self.listings = listings
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="🛒 Marketplace", font=("Georgia", 24), bg="#1e1e1e", fg="white")
        title.pack(pady=10)

        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")

        self.create_market_tab()
        self.create_sell_tab()

    def create_market_tab(self):
        market_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(market_tab, text='Browse Items')

        columns = ('ID', 'Item', 'Type', 'Price', 'Currency', 'Seller')
        self.market_tree = ttk.Treeview(market_tab, columns=columns, show='headings')
        for col in columns:
            self.market_tree.heading(col, text=col)
            self.market_tree.column(col, width=100)
        self.market_tree.pack(expand=True, fill='both', padx=10, pady=10)

        for item in self.listings:
            self.market_tree.insert('', tk.END, values=item)

        buy_button = tk.Button(market_tab, text="Buy Selected", command=self.buy_item, bg="#3e3e3e", fg="white")
        buy_button.pack(pady=5)

    def create_sell_tab(self):
        sell_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(sell_tab, text='Sell Item')

        self.inventory_list = tk.Listbox(sell_tab)
        for item in self.user_inventory:
            self.inventory_list.insert(tk.END, item)
        self.inventory_list.pack(pady=10)

        self.price_entry = tk.Entry(sell_tab)
        self.price_entry.insert(0, "Enter Price")
        self.price_entry.pack(pady=5)

        self.currency_var = tk.StringVar()
        self.currency_var.set("RFN")
        currency_menu = tk.OptionMenu(sell_tab, self.currency_var, "RFN", "TON")
        currency_menu.pack(pady=5)

        sell_button = tk.Button(sell_tab, text="List for Sale", command=self.list_item, bg="#3e3e3e", fg="white")
        sell_button.pack(pady=5)

    def buy_item(self):
        selected = self.market_tree.selection()
        if selected:
            item = self.market_tree.item(selected[0], 'values')
            messagebox.showinfo("Purchase", f"You bought: {item[1]} for {item[3]} {item[4]}")
        else:
            messagebox.showwarning("Warning", "No item selected.")

    def list_item(self):
        selected_index = self.inventory_list.curselection()
        if selected_index:
            item = self.inventory_list.get(selected_index)
            price = self.price_entry.get()
            currency = self.currency_var.get()
            messagebox.showinfo("Listed", f"Listed {item} for {price} {currency}.")
        else:
            messagebox.showwarning("Warning", "Select an item to sell.")

# Example usage
if __name__ == "__main__":
    user_inventory = ["Sword of Fire", "Elven Bow", "Shadow Cloak"]
    listings = [
        (1, "Arcane Staff", "Weapon", 300, "RFN", "Player123"),
        (2, "Dragon Armor", "Armor", 450, "TON", "DarkLord"),
    ]
    app = MarketplaceGUI(user_inventory, listings)
    app.mainloop()
