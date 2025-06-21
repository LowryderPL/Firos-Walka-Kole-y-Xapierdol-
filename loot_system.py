import random
from inventory import inventory

class LootSystem:
    def __init__(self):
        self.loot_table = {
            "Wilczy Cień": ["Wilcza skóra", "Złamany kieł", "Mikstura many"],
            "Wędrowny Ghul": ["Zepsuty naszyjnik", "Kość z runą", "Trujący pył"],
            "Słony Demon": ["Sól piekielna", "Kamień runiczny", "Zwoje przeklętego ognia"],
            "Ognisty Widmowąż": ["Łuska ognia", "Esencja płomienia", "Zwoje ognistego oddechu"],
            "Król Zguby": ["Korona cienia", "Księga zapomnianych zaklęć", "Pierścień zagłady"]
        }

    def drop_loot(self, beast_name):
        loot = self.loot_table.get(beast_name, [])
        if not loot:
            print("🪙 Brak nagród dla tego potwora.")
            return
        dropped = random.choice(loot)
        inventory.add_item(dropped)

loot_system = LootSystem()
