
# Finalna wersja inventory.py łącząca pełną funkcjonalność i rozszerzenia

class Item:
    def __init__(self, name, type, power=0, weight=0, value=0, description=""):
        self.name = name
        self.type = type  # np. "broń", "zbroja", "mikstura"
        self.power = power
        self.weight = weight
        self.value = value
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.type}) - Moc: {self.power}, Waga: {self.weight}, Wartość: {self.value}"

class Inventory:
    def __init__(self, max_weight=150):
        self.slots = {
            "głowa": None,
            "tors": None,
            "nogi": None,
            "buty": None,
            "broń": None,
            "tarcza": None,
            "pierścień1": None,
            "pierścień2": None,
            "plecak": None,
            "pas": None,
            "zwój": None,
            "artefakt": None,
            "zwierzę": None,
            "skrzydła": None,
            "runiczny_slot": None,
            "crafting_slot": None
        }
        self.items = []
        self.max_weight = max_weight

    def current_weight(self):
        return sum(item.weight for item in self.items)

    def add_item(self, item):
        if self.current_weight() + item.weight <= self.max_weight:
            self.items.append(item)
            print(f"Dodano przedmiot: {item}")
        else:
            print("Nie możesz dodać tego przedmiotu. Zbyt duża waga!")

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def equip_item(self, item):
        if item.type in self.slots:
            if self.slots[item.type] is None:
                self.slots[item.type] = item
                print(f"Wyposażono: {item.name} w slot {item.type}")
            else:
                print(f"Slot {item.type} jest już zajęty przez {self.slots[item.type].name}")
        else:
            print(f"Nieznany typ przedmiotu: {item.type}")

    def unequip_item(self, slot_name):
        if slot_name in self.slots and self.slots[slot_name] is not None:
            item = self.slots[slot_name]
            self.slots[slot_name] = None
            self.add_item(item)
            print(f"Zdjęto przedmiot: {item.name} ze slotu {slot_name}")
        else:
            print("Slot pusty lub nie istnieje.")

    def show_equipment(self):
        print("Wyposażenie:")
        for slot, item in self.slots.items():
            print(f"{slot.title()}: {item.name if item else 'pusty'}")

    def show_inventory(self):
        print("Ekwipunek:")
        for item in self.items:
            print(item)

    def filter_items(self, type_filter=None):
        if type_filter:
            return [item for item in self.items if item.type == type_filter]
        return self.items
