from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Lista przedmiotów dostępnych w marketplace
market_items = [
    {"id": "nft_001", "name": "⚔️ Miecz Cienia", "price_rfn": 30, "price_ton": 0.2},
    {"id": "nft_002", "name": "🛡️ Zbroja Duszy", "price_rfn": 50, "price_ton": 0.35},
    {"id": "nft_003", "name": "🔥 Runa Płomienia", "price_rfn": 20, "price_ton": 0.1},
]

# Funkcja otwierająca marketplace
def handle_marketplace_action(bot, user_id):
    markup = InlineKeyboardMarkup()
    for item in market_items:
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton(f"{item['name']} – {item['price_rfn']} RFN", callback_data=f"buy_rfn_{item['id']}"),
            InlineKeyboardButton(f"{item['price_ton']} TON", callback_data=f"buy_ton_{item['id']}")
        )
    bot.send_message(user_id, "🏪 *Marketplace NFT – wybierz przedmiot do zakupu:*", reply_markup=markup, parse_mode="Markdown")

# Funkcja obsługująca kliknięcia w marketplace
def handle_marketplace_callback(bot, callback_query, user_states):
    user_id = callback_query.from_user.id
    data = callback_query.data

    if user_id not in user_states:
        user_states[user_id] = {
            "inventory": [],
            "rfm": 100,
            "ton": 0.5,
            "nft": [],
            "active_menu": "main"
        }

    user = user_states[user_id]

    for item in market_items:
        if data == f"buy_rfn_{item['id']}":
            if user["rfm"] >= item["price_rfn"]:
                user["rfm"] -= item["price_rfn"]
                user["inventory"].append(item["name"])
                bot.answer_callback_query(callback_query.id, text=f"✅ Kupiono {item['name']} za RFN!")
                bot.edit_message_text(f"🛒 Zakupiono {item['name']} za {item['price_rfn']} RFN.",
                                      chat_id=callback_query.message.chat.id,
                                      message_id=callback_query.message.message_id)
            else:
                bot.answer_callback_query(callback_query.id, text="❌ Za mało RFN!")
            return

        elif data == f"buy_ton_{item['id']}":
            if user["ton"] >= item["price_ton"]:
                user["ton"] -= item["price_ton"]
                user["inventory"].append(item["name"])
                bot.answer_callback_query(callback_query.id, text=f"✅ Kupiono {item['name']} za TON!")
                bot.edit_message_text(f"🛒 Zakupiono {item['name']} za {item['price_ton']} TON.",
                                      chat_id=callback_query.message.chat.id,
                                      message_id=callback_query.message.message_id)
            else:
                bot.answer_callback_query(callback_query.id, text="❌ Za mało TON!")
            return

    bot.answer_callback_query(callback_query.id, text="❓ Nieznana opcja.")
