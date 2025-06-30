import json
import os

INVENTORY_FILE = "data/inventory.json"

def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w") as f:
            json.dump({}, f)
    with open(INVENTORY_FILE, "r") as f:
        return json.load(f)

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

def get_user_inventory(user_id):
    inventory = load_inventory()
    uid = str(user_id)
    if uid not in inventory:
        inventory[uid] = {
            "ton": 0.0,
            "rfn": 0,
            "nft": [],
            "items": [],
            "books": [],
            "quests_done": [],
            "crafted": [],
            "daily_limit": {"crafts": 0},
        }
        save_inventory(inventory)
    return inventory[uid]

def update_user_inventory(user_id, data):
    inventory = load_inventory()
    inventory[str(user_id)] = data
    save_inventory(inventory)

def add_item_to_inventory(user_id, item_id):
    inventory = get_user_inventory(user_id)
    inventory['items'].append(item_id)
    update_user_inventory(user_id, inventory)

def add_nft_to_inventory(user_id, nft_id):
    inventory = get_user_inventory(user_id)
    inventory['nft'].append(nft_id)
    update_user_inventory(user_id, inventory)

def deduct_ton(user_id, amount):
    inventory = get_user_inventory(user_id)
    if inventory['ton'] >= amount:
        inventory['ton'] -= amount
        update_user_inventory(user_id, inventory)
        return True
    return False

def add_ton(user_id, amount):
    inventory = get_user_inventory(user_id)
    inventory['ton'] += amount
    update_user_inventory(user_id, inventory)

def add_rfn(user_id, amount):
    inventory = get_user_inventory(user_id)
    inventory['rfn'] += amount
    update_user_inventory(user_id, inventory)

def inventory_to_string(user_id):
    inv = get_user_inventory(user_id)
    nft_list = '\n'.join(inv['nft']) or "Brak"
    item_list = '\n'.join(inv['items']) or "Brak"
    return (
        f"💰 TON: {inv['ton']}\n"
        f"🪙 RFN: {inv['rfn']}\n"
        f"📦 Przedmioty:\n{item_list}\n"
        f"🃏 Karty NFT:\n{nft_list}"
    )
