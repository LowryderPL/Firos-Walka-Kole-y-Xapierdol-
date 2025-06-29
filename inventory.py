import random
import json
from datetime import datetime, timedelta

class Inventory:
    def __init__(self, player_id):
        self.player_id = player_id
        self.items = []
        self.crafting_attempts = []
        self.max_crafts_per_2_days = 3

    def load_inventory(self):
        try:
            with open(f"data/inventories/{self.player_id}.json", "r") as f:
                data = json.load(f)
                self.items = data.get("items", [])
                self.crafting_attempts = [
                    datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
                    for ts in data.get("crafting_attempts", [])
                ]
        except FileNotFoundError:
            self.items = []
            self.crafting_attempts = []

    def save_inventory(self):
        with open(f"data/inventories/{self.player_id}.json", "w") as f:
            json.dump({
                "items": self.items,
                "crafting_attempts": [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in self.crafting_attempts]
            }, f, indent=4)

    def add_item(self, item):
        self.items.append(item)
        self.save_inventory()

    def get_items(self):
        return self.items

    def can_craft(self):
        now = datetime.now()
        self.crafting_attempts = [
            attempt for attempt in self.crafting_attempts if now - attempt < timedelta(days=2)
        ]
        return len(self.crafting_attempts) < self.max_crafts_per_2_days

    def perform_crafting(self, ingredients):
        if not self.can_craft():
            return {"success": False, "reason": "Limit osiągnięty. Możesz craftować 3x na 2 dni."}

        rarity = self.determine_rarity()
        result = self.craft_result(rarity)

        self.crafting_attempts.append(datetime.now())
        if result["success"]:
            self.add_item(result["item"])
        self.save_inventory()

        return result

    def determine_rarity(self):
        roll = random.randint(1, 100)
        if roll <= 40:
            return "zwykły"
        elif roll <= 65:
            return "rzadki"
        elif roll <= 80:
            return "epicki"
        elif roll <= 90:
            return "legendarny"
        elif roll <= 97:
            return "mistyczny"
        else:
            return "boski"

    def craft_result(self, rarity):
        chance = {
            "zwykły": 90,
            "rzadki": 70,
            "epicki": 50,
            "legendarny": 35,
            "mistyczny": 25,
            "boski": 15
        }[rarity]

        success_roll = random.randint(1, 100)
        if success_roll <= chance:
            item = {
                "name": f"Przedmiot {rarity.upper()}",
                "rarity": rarity,
                "nft": True if rarity in ["epicki", "legendarny", "mistyczny", "boski"] else False,
                "value_ton": self.calculate_ton_cost(rarity),
                "attributes": self.random_attributes(rarity)
            }
            return {"success": True, "item": item}
        else:
            failure_item = {
                "name": "Złamany Kryształ",
                "rarity": "złom",
                "value_ton": 0.1,
                "description": "Nieudany crafting, ale coś pozostało z magii..."
            }
            return {"success": False, "item": failure_item}

    def calculate_ton_cost(self, rarity):
        cost_map = {
            "zwykły": 0.2,
            "rzadki": 0.4,
            "epicki": 0.8,
            "legendarny": 1.0,
            "mistyczny": 2.0,
            "boski": 3.0
        }
        return cost_map[rarity]

    def random_attributes(self, rarity):
        base = {
            "zwykły": 1,
            "rzadki": 3,
            "epicki": 5,
            "legendarny": 8,
            "mistyczny": 12,
            "boski": 20
        }[rarity]

        return {
            "atak": random.randint(base, base + 3),
            "obrona": random.randint(base, base + 2),
            "szansa_krytyka": round(random.uniform(0.5, 5.0), 2)
        }
def update_item_level(user_id, item_id, increment):
    for item in USERS[user_id]['inventory']:
        if item['id'] == item_id:
            item['level'] += increment
            if item['level'] > 15:
                item['level'] = 15
            break
