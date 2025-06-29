import telebot
from menu import show_main_menu
from inventory import get_user_inventory
from crafting_logic import handle_crafting_action
from marketplace_logic import handle_marketplace_action
from questy import handle_quest_action
from bosses import handle_boss_action
from nft_loader import load_nft_data
import random

BOT_TOKEN = "TU_WSTAW_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

user_states = {}
nft_data = load_nft_data()

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

    quote = random.choice([
        "„Stary świat płonie, nowy się rodzi w cieniu miecza.”",
        "„Tylko głupcy nie boją się potworów.”",
        "„Firos nie przebacza – nagradza lub zabiera.”"
    ])
    bot.send_message(message.chat.id, f"🔥 Witaj w świecie Firos 🔥\n\n{quote}")
    show_main_menu(bot, message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def handle_menu(call):
    user_id = call.from_user.id
    state = user_states.get(user_id)

    if not state:
        bot.send_message(call.message.chat.id, "Użyj /start, by rozpocząć grę.")
        return

    data = call.data

    if data == "inventory":
        items = get_user_inventory(user_id)
        inv_text = "\n".join(f"- {item}" for item in items)
        bot.send_message(call.message.chat.id, f"🎒 Twoje przedmioty:\n{inv_text}")
    elif data == "crafting":
        handle_crafting_action(bot, call.message.chat.id, state)
    elif data == "marketplace":
        handle_marketplace_action(bot, call.message.chat.id, state)
    elif data == "questy":
        handle_quest_action(bot, call.message.chat.id, state)
    elif data == "boss":
        handle_boss_action(bot, call.message.chat.id, state)
    elif data == "menu":
        show_main_menu(bot, call.message.chat.id)
    else:
        bot.send_message(call.message.chat.id, "Nieznana akcja.")

# Losowe zdarzenia co 5 interakcji
def random_event():
    return random.choice([
        "🔮 Tajemniczy kupiec oferuje wymianę NFT.",
        "💥 Znalazłeś fragment zaklęcia – sprawdź crafting.",
        "🧪 Trafiasz na alchemika, który może coś stworzyć."
    ])

# Dodaj losowe zdarzenie co jakiś czas
@bot.message_handler(func=lambda m: True)
def idle_chat(m):
    if random.randint(1, 5) == 3:
        bot.send_message(m.chat.id, random_event())

bot.polling(none_stop=True)
