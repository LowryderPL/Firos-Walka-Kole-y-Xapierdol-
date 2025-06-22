class Item:
    def __init__(self, name, type_, rarity, effect, equipped=False):
        self.name = name
        self.type = type_  # np. 'broń', 'zbroja', 'artefakt', 'mikstura'
        self.rarity = rarity
        self.effect = effect
        self.equipped = equipped

    def __str__(self):
        status = " (Wyposażony)" if self.equipped else ""
        return f"{self.name} [{self.type} | {self.rarity}] - {self.effect}{status}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"\n✅ Dodano: {item.name}")

    def remove_item(self, item_name):
        self.items = [i for i in self.items if i.name != item_name]
        print(f"\n❌ Usunięto: {item_name}")

    def equip_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.equipped = True
                print(f"\n🛡️ Wyposażono: {item.name}")
                return
        print("🔍 Przedmiot nie znaleziony.")

    def list_items(self):
        print("\n🎒 Ekwipunek:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")

# Przykład użycia:
if __name__ == "__main__":
    inv = Inventory()
    inv.add_item(Item("Miecz Świtu", "broń", "epicki", "+30 DMG"))
    inv.add_item(Item("Zbroja Cienia", "zbroja", "rzadka", "+20 DEF"))
    inv.list_items()
    inv.equip_item("Miecz Świtu")
    inv.list_items()
