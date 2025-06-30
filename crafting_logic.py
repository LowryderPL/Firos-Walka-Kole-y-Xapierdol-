# crafting_logic.py

import random
from database import get_player_inventory, update_inventory_item, get_player_ton_balance, update_player_ton_balance
from utils import generate_loot_item

RARITY_TIERS = {
    "pospolity": 60,
    "rzadki": 25,
    "epicki": 10,
    "legendarny": 4,
    "boski": 1
}

TON_COST = {
    "standard": 0.9,
    "premium": 3.0
}

CRAFT_LIMIT = 3  # co 48h

def can_craft(player_id):
    # funkcja do limitu craftów
    return True  # do rozszerzenia na system timestampów

def attempt_craft(player_id, tier="standard"):
    if not can_craft(player_id):
        return "🛑 Wyczerpałeś limit craftingu. Spróbuj ponownie za 48h."

    cost = TON_COST[tier]
    balance = get_player_ton_balance(player_id)

    if balance < cost:
        return f"❌ Masz za mało TON. Wymagane: {cost} TON."

    update_player_ton_balance(player_id, -cost)
    
    chance = 60 if tier == "standard" else 50
    roll = random.randint(1, 100)

    if roll <= chance:
        new_item = generate_loot_item()
        update_inventory_item(player_id, new_item)
        return f"✅ Udało się! Stworzyłeś: {new_item['name']} ({new_item['rarity']})"
    else:
        # szansa na losowy item w ramach niepowodzenia
        if random.random() < 0.5:
            consolation = generate_loot_item(min_rarity="pospolity", max_rarity="rzadki")
            update_inventory_item(player_id, consolation)
            return f"❌ Crafting nieudany, ale znalazłeś: {consolation['name']} ({consolation['rarity']})"
        return "❌ Crafting nieudany. Przedmioty przepadły."
