class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Dodano do ekwipunku: {item}")

    def show_inventory(self):
        print("=== TWÓJ EKWIPUNEK ===")
        if not self.items:
            print("Ekwipunek jest pusty.")
        else:
            for item in self.items:
                print(f"- {item}")
