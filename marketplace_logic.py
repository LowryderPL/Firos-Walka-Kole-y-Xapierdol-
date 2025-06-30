# marketplace_logic.py

from database import (
    get_market_items,
    add_market_item,
    remove_market_item,
    get_player_inventory,
    update_inventory_item,
    get_player_ton_balance,
    update_player_ton_balance
)

TON_FEE_PERCENT = 12
RFN_FEE_PERCENT = 5
RARE_ONLY_TON = ["legendarny", "boski"]

def list_item_for_sale(player_id, item_id, price, currency="TON"):
    inventory = get_player_inventory(player_id)
    item = next((i for i in inventory if i['id'] == item_id), None)
    
    if not item:
        return "❌ Nie masz takiego przedmiotu."
    
    if item["rarity"] in RARE_ONLY_TON and currency != "TON":
        return "❌ Ten przedmiot można sprzedać tylko za TON."

    item_to_sell = {
        "id": item_id,
        "player_id": player_id,
        "item": item,
        "price": price,
        "currency": currency
    }

    add_market_item(item_to_sell)
    return f"✅ Wystawiono {item['name']} za {price} {currency}."

def buy_market_item(buyer_id, item_id):
    item = get_market_items().get(item_id)
    if not item:
        return "❌ Przedmiot nie istnieje lub został już kupiony."

    price = item["price"]
    currency = item["currency"]
    fee = price * (TON_FEE_PERCENT if currency == "TON" else RFN_FEE_PERCENT) / 100

    if currency == "TON":
        balance = get_player_ton_balance(buyer_id)
        if balance < price:
            return "❌ Nie masz wystarczająco TON."
        update_player_ton_balance(buyer_id, -price)
        update_player_ton_balance("OWNER", fee)
    else:
        return "❌ RFN jeszcze nieobsługiwane w tej wersji."

    update_inventory_item(buyer_id, item["item"])
    remove_market_item(item_id)
    return f"✅ Kupiłeś {item['item']['name']} za {price} {currency}."
