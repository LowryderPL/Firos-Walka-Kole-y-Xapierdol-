class Item:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def display_info(self):
        print(f"▶ {self.name} ({self.rarity})\n  {self.description}")

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"[+1] Zdobyto: {item.name} ({item.rarity})")

    def show_inventory(self):
        if not self.items:
            print("⚠ Twój ekwipunek jest pusty.")
        else:
            print("📦 Twój ekwipunek:")
            for item in self.items:
                item.display_info()
