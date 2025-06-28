# inventory.py — Rozbudowany system ekwipunku w Firos: Magic & Magic

class Item:
    def __init__(self, name, item_type, power=0, weight=1, value=0, rarity="zwykły", description="", level=1, usable=False):
        self.name = name
        self.type = item_type  # np. "zbroja", "mikstura", "artefakt", "runiczny"
        self.power = power
        self.weight = weight
        self.value = value
        self.rarity = rarity
        self.description = description
        self.level = level
        self.usable = usable

    def __str__(self):
        return (f"{self.name} ({self.type}, {self.rarity}) - Moc: {self.power}, Lvl: {self.level}, "
                f"Waga: {self.weight}, Wartość: {self.value}\nOpis: {self.description}")


class EquipmentSlot:
    def __init__(self, name):
        self.name = name
        self.item = None

    def equip(self, item):
        self.item = item
        print(f"🛡️ Wyposażono: {item.name} w slocie {self.name}")

    def unequip(self):
        if self.item:
            print(f"❌ Zdjęto: {self.item.name} ze slotu {self.name}")
            item = self.item
            self.item = None
            return item
        else:
            print(f"⚠️ Slot {self.name} jest już pusty.")
            return None

    def __str__(self):
        return f"{self.name}: {self.item.name if self.item else 'pusty'}"


class Inventory:
    def __init__(self, capacity=40):
        self.slots = {
            "głowa": EquipmentSlot("głowa"),
            "tors": EquipmentSlot("tors"),
            "nogi": EquipmentSlot("nogi"),
            "buty": EquipmentSlot("buty"),
            "broń": EquipmentSlot("broń"),
            "tarcza": EquipmentSlot("tarcza"),
            "amulet": EquipmentSlot("amulet"),
            "pierścień1": EquipmentSlot("pierścień1"),
            "pierścień2": EquipmentSlot("pierścień2")
        }
        self.items = []
        self.capacity = capacity

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"➕ Dodano do plecaka: {item.name}")
        else:
            print("❌ Plecak jest pełny!")

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                del self.items[i]
                print(f"❌ Usunięto: {item_name} z plecaka")
                return
        print(f"⚠️ Nie znaleziono przedmiotu: {item_name}")

    def equip_item(self, slot_name, item_name):
        item = next((i for i in self.items if i.name == item_name), None)
        if item and slot_name in self.slots:
            self.slots[slot_name].equip(item)
            self.items.remove(item)
        else:
            print(f"❌ Nie można wyposażyć: {item_name} w slot {slot_name}")

    def unequip_item(self, slot_name):
        if slot_name in self.slots:
            item = self.slots[slot_name].unequip()
            if item:
                self.add_item(item)

    def use_item(self, item_name):
        item = next((i for i in self.items if i.name == item_name), None)
        if item:
            if item.usable:
                print(f"🧪 Użyto: {item.name} (+{item.power} HP/MANA)")
                self.items.remove(item)
            else:
                print(f"⚠️ {item.name} nie może być użyty!")
        else:
            print(f"❌ Przedmiot {item_name} nie został znaleziony.")

    def show_inventory(self):
        print("🎒 Twój ekwipunek:")
        if not self.items:
            print("  - pusty -")
        for item in self.items:
            print("-", item)

    def show_equipment(self):
        print("🧙 Wyposażenie postaci:")
        for slot in self.slots.values():
            print("-", slot)

    def filter_items(self, item_type):
        filtered = [item for item in self.items if item.type == item_type]
        print(f"🔍 Przedmioty typu {item_type}:")
        for item in filtered:
            print("-", item)

    def upgrade_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                if item.level < 15:
                    item.level += 1
                    item.power += 2
                    print(f"🔧 Ulepszono: {item.name} do poziomu {item.level}")
                else:
                    print(f"⚠️ {item.name} osiągnął maksymalny poziom.")
                return
        print(f"❌ Nie znaleziono przedmiotu: {item_name}")

# Test (można zakomentować)
if __name__ == "__main__":
    inv = Inventory()
    inv.add_item(Item("Hełm Cienia", "zbroja", power=5, description="Hełm z mrocznej stali", rarity="rzadki"))
    inv.add_item(Item("Mikstura Mocy", "mikstura", power=15, usable=True, description="Zwiększa siłę"))
    inv.add_item(Item("Runa Ognia", "runiczny", power=8, rarity="epicki", description="Runa zwiększająca obrażenia od ognia"))
    inv.show_inventory()
    inv.equip_item("głowa", "Hełm Cienia")
    inv.show_equipment()
    inv.use_item("Mikstura Mocy")
    inv.upgrade_item("Runa Ognia")
