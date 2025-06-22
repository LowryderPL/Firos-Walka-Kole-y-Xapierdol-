# inventory.py – FIROS: Magic & Magic

class Item:
    def __init__(self, name, rarity, power, slot, nft_id=None, max_uses=3, description=""):
        self.name = name
        self.rarity = rarity  # common, rare, epic, legendary, ancient
        self.power = power
        self.slot = slot  # e.g. helmet, sword, armor
        self.nft_id = nft_id
        self.max_uses = max_uses
        self.uses_left = max_uses
        self.description = description

    def use(self):
        if self.uses_left > 0:
            self.uses_left -= 1
            print(f"Użyto przedmiotu {self.name}. Pozostało użyć: {self.uses_left}")
        else:
            print(f"{self.name} nie może być już użyty – zużyty.")

    def upgrade(self):
        self.power += 1
        print(f"{self.name} ulepszony! Nowa moc: {self.power}")


class Inventory:
    def __init__(self):
        self.slots = {
            "helmet": None,
            "armor": None,
            "sword": None,
            "ring": None,
            "boots": None,
            "artifact": None
        }
        self.backpack = []

    def equip(self, item):
        if item.slot in self.slots:
            self.slots[item.slot] = item
            print(f"Wyposażono: {item.name} ({item.slot})")
        else:
            print("Nie można wyposażyć – nieznany slot.")

    def unequip(self, slot):
        if slot in self.slots and self.slots[slot]:
            print(f"Zdjęto: {self.slots[slot].name}")
            self.slots[slot] = None
        else:
            print("Nie ma nic w tym slocie.")

    def add_to_backpack(self, item):
        self.backpack.append(item)
        print(f"Dodano do plecaka: {item.name}")

    def show_inventory(self):
        print("=== Ekwipunek ===")
        for slot, item in self.slots.items():
            if item:
                print(f"{slot.capitalize()}: {item.name} [{item.rarity}] – Moc: {item.power} ({item.uses_left}/{item.max_uses})")
            else:
                print(f"{slot.capitalize()}: ---")
        print("=== Plecak ===")
        for i, item in enumerate(self.backpack):
            print(f"{i + 1}. {item.name} ({item.rarity})")
