from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from inventory import get_user_inventory, update_user_inventory
from nft_cards import get_card_by_id

# Konfiguracja prowizji i cen
MARKET_TAX_PERCENT = 12
TON_EXCHANGE_RATE = 1.0  # 1 TON = 1 TON (na potrzeby demonstracyjne)

market_items = [
    {"id": "card001", "name": "Miecz Cienia", "price_ton": 0.8, "rarity": "rare"},
    {"id": "card002", "name": "Zbroja Firosu", "price_ton": 1.2, "rarity": "epic"},
    {"id": "card003", "name": "Smoczy Kryształ", "price_ton": 2.5, "rarity": "legendary"},
]

def handle_marketplace_action(bot, user_id):
    markup = InlineKeyboardMarkup()
    for item in market_items:
        button = InlineKeyboardButton(
            text=f"{item['name']} - {item['price_ton']} TON",
            callback_data=f"buy_{item['id']}"
        )
        markup.add(button)
    bot.send_message(user_id, "🛒 *Marketplace NFT – Firos*\nWybierz kartę do zakupu:", reply_markup=markup, parse_mode="Markdown")

def handle_marketplace_callback(bot, call):
    user_id = call.from_user.id
    data = call.data

    if data.startswith("buy_"):
        card_id = data.split("_")[1]
        item = next((i for i in market_items if i['id'] == card_id), None)
        if item:
            user_inventory = get_user_inventory(user_id)
            if user_inventory['ton'] >= item['price_ton']:
                user_inventory['ton'] -= item['price_ton']
                user_inventory['nft'].append(item['id'])
                update_user_inventory(user_id, user_inventory)
                bot.answer_callback_query(call.id)
                bot.send_message(user_id, f"✅ Zakupiono: {item['name']} za {item['price_ton']} TON!")
            else:
                bot.answer_callback_query(call.id, "❌ Masz za mało TON.")
        else:
            bot.answer_callback_query(call.id, "⚠️ Nie znaleziono przedmiotu.")
