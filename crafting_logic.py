import random
from inventory import get_user_inventory, update_user_inventory, add_item_to_inventory, deduct_ton

RARITIES = ["common", "uncommon", "rare", "epic", "legendary", "mythical"]
CRAFT_COST_TON = {
    "standard": 0.9,
    "premium": 3.0
}
MAX_ATTEMPTS = 3

def can_craft(user_id):
    inv = get_user_inventory(user_id)
    limit = inv.get("daily_limit", {}).get("crafts", 0)
    return limit < MAX_ATTEMPTS

def reset_daily_limit(user_id):
    inv = get_user_inventory(user_id)
    inv["daily_limit"]["crafts"] = 0
    update_user_inventory(user_id, inv)

def increase_craft_count(user_id):
    inv = get_user_inventory(user_id)
    inv["daily_limit"]["crafts"] += 1
    update_user_inventory(user_id, inv)

def attempt_craft(user_id, mode="standard"):
    if not can_craft(user_id):
        return "❌ Osiągnąłeś dzienny limit craftingu (3/2 dni)."

    cost = CRAFT_COST_TON["premium" if mode == "premium" else "standard"]
    if not deduct_ton(user_id, cost):
        return f"❌ Brak wystarczającej ilości TON (koszt: {cost} TON)."

    increase_craft_count(user_id)

    success = random.random() < (0.6 if mode == "standard" else 0.5)
    if success:
        rarity = random.choices(
            RARITIES,
            weights=[50, 25, 15, 7, 2, 1] if mode == "standard" else [0, 0, 20, 40, 30, 10]
        )[0]
        item = f"{rarity.capitalize()} Crafted Item"
        add_item_to_inventory(user_id, item)
        return f"✅ Udało się! Otrzymano: **{item}**"
    else:
        fallback = f"🔁 Niepowodzenie craftingu – otrzymano losowy przedmiot!"
        random_drop = random.choice(["Kawałek zbroi", "Złamany zwój", "Pył magiczny"])
        add_item_to_inventory(user_id, random_drop)
        return f"❌ Crafting nieudany. {fallback} ➕ {random_drop}"
