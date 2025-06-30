from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler, Updater

=== GŁÓWNE MENU ===

def main_menu(update: Update, context: CallbackContext): keyboard = [ [InlineKeyboardButton("🌍 Eksploruj", callback_data='explore')], [InlineKeyboardButton("📦 Ekwipunek", callback_data='inventory')], [InlineKeyboardButton("🌪 Misje", callback_data='quests')], [InlineKeyboardButton("🏰 Miasta & Lokacje", callback_data='locations')], [InlineKeyboardButton("⚗ Alchemia", callback_data='alchemy')], [InlineKeyboardButton("✨ Tworzenie Zaklęć", callback_data='spell_crafting')], [InlineKeyboardButton("🛒 Marketplace NFT", callback_data='marketplace')], [InlineKeyboardButton("🏆 Ranking", callback_data='ranking')], [InlineKeyboardButton("@ Ustawienia", callback_data='settings')] ] reply_markup = InlineKeyboardMarkup(keyboard) update.message.reply_text("🌟 Główne Menu Firos: Magic & Magic 🌟", reply_markup=reply_markup, parse_mode='Markdown')

=== OBSŁUGA KLIKNIĘĆ ===

def handle_callback(update: Update, context: CallbackContext): query = update.callback_query query.answer()

if query.data == 'explore':
    query.edit_message_text("\ud83c\udf10 Wyruszasz na eksplorację Świata Firos!")

elif query.data == 'inventory':
    from inventory import show_inventory
    show_inventory(update, context)

elif query.data == 'quests':
    from questy import show_quests
    show_quests(update, context)

elif query.data == 'locations':
    from locations import show_locations
    show_locations(update, context)

elif query.data == 'alchemy':
    from alchemy import open_alchemy_lab
    open_alchemy_lab(update, context)

elif query.data == 'spell_crafting':
    from spell_crafting import open_spell_crafting_ui
    open_spell_crafting_ui(update, context)

elif query.data == 'marketplace':
    from marketplace_logic import open_marketplace
    open_marketplace(update, context)

elif query.data == 'ranking':
    from ranking import show_ranking
    show_ranking(update, context)

elif query.data == 'settings':
    query.edit_message_text("⚙️ Ustawienia są w trakcie rozbudowy.")

else:
    query.edit_message_text("❓ Nierozpoznana opcja.")

=== URUCHOMIENIE BOTA (do main.py) ===

def run_bot(): updater = Updater("TU_WSTAW_TOKEN", use_context=True) dp = updater.dispatcher

dp.add_handler(CommandHandler("start", main_menu))
dp.add_handler(CallbackQueryHandler(handle_callback))

updater.start_polling()
updater.idle()

To możesz wkleić do main.py:

from menu import run_bot

if name == 'main':

run_bot()

