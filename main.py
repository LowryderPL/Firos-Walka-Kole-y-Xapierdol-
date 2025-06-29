import telebot
from menu import show_main_menu
from inventory import get_user_inventory
from spell_crafting import handle_spell_crafting
from marketplace_logic import handle_marketplace_action
from questy import handle_quest_action
from bosses import handle_boss_action
from nft_cards import load_nft_data
from npc_dialogue import start_dialog, handle_dialog_callback

from telegram.ext import CallbackQueryHandler
import random

# === KONFIGURACJA BOTA ===
BOT_TOKEN = "TU_WSTAW_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

# === DANE GRACZY I NFT ===
user_states = {}
nft_data = load_nft_data()

# === START GRY ===
@bot.message_handler(commands=['start'])
def start_game(message):
    user_id = message.from_user.id
    user_states[user_id] = {
        'inventory': get_user_inventory(user_id),
        'nft': [],
        'rfm': 100,
        'ton': 0.5,
        'active_menu': 'main'
    }
    bot.send_message(user_id, "🌟 Witaj w Świecie Firos! 🌌", reply_markup=show_main_menu())

# === CALLBACK HANDLER ===
@bot.callback_query_handler(func=lambda c: True)
def handle_callbacks(callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data

    if data == "inventory":
        inv = get_user_inventory(user_id)
        bot.answer_callback_query(callback_query.id)
        bot.send_message(user_id, f"🎒 Ekwipunek:\n{inv}")
    
    elif data == "marketplace":
        handle_marketplace_action(bot, user_id)

    elif data == "quest":
        handle_quest_action(bot, user_id)

    elif data == "boss":
        handle_boss_action(bot, user_id)

    elif data == "crafting":
        handle_spell_crafting(bot, user_id)

    elif data == "dialog":
        start_dialog(bot, user_id)

    elif data.startswith("dialog_"):
        handle_dialog_callback(bot, callback_query)

    else:
        bot.send_message(user_id, "⚠️ Nieznana opcja.")

# === URUCHOMIENIE BOTA ===
if __name__ == '__main__':
    print("Bot wystartował... 🔥")
    bot.infinity_polling()
