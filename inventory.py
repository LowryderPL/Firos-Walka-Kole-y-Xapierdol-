class Inventory:
    def __init__(self):
        # Przykładowe przedmioty NFT w ekwipunku
        self.items = [
            {
                "id": 1,
                "name": "Miecz Cienia",
                "type": "broń",
                "rarity": "epicki",
                "power": 120,
                "defense": 20,
                "magic": 0,
                "description": "Przeklęty miecz wykuty z czarnego kamienia."
            },
            {
                "id": 2,
                "name": "Zbroja Wędrowca",
                "type": "zbroja",
                "rarity": "rzadka",
                "power": 0,
                "defense": 80,
                "magic": 10,
                "description": "Zbroja należąca do starego maga-wojownika."
            },
            {
                "id": 3,
                "name": "Karta Bohatera: Eldrin",
                "type": "karta klasowa",
                "rarity": "unikatowa",
                "power": 50,
                "defense": 40,
                "magic": 150,
                "description": "Potężny elficki mag, obrońca Lasy Firowe."
            }
        ]

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item_by_id(self, item_id):
        self.items = [item for item in self.items if item["id"] != item_id]

    def find_item_by_id(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                return item
        return None

    def list_inventory(self):
        for item in self.items:
            print(f"{item['name']} | Typ: {item['type']} | Moc: {item['power']} | Obrona: {item['defense']} | Magia: {item['magic']}")
