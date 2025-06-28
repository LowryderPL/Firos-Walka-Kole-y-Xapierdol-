# inventory_gui.py – GUI ekwipunku postaci

class InventoryGUI:
    def __init__(self, inventory):
        self.inventory = inventory

    def display(self):
        print("\n📦 Ekwipunek postaci:")
        for i, item in enumerate(self.inventory.items, start=1):
            print(f"{i}. {item.name} (typ: {item.type}, moc: {item.power})")

        print("\n🎽 Wyposażenie:")
        for slot, equipment in self.inventory.slots.items():
            print(f"{slot}: {equipment.item.name if equipment.item else '-'}")

        print(f"\nWaga: {self.inventory.get_total_weight()} / {self.inventory.weight_limit} kg")

    def show_item_details(self, item_name):
        item = next((i for i in self.inventory.items if i.name == item_name), None)
        if item:
            print(f"🔍 Szczegóły: {item.name}")
            print(f"Typ: {item.type}")
            print(f"Moc: {item.power}")
            print(f"Waga: {item.weight}")
        else:
            print(f"❌ Nie znaleziono przedmiotu o nazwie: {item_name}")