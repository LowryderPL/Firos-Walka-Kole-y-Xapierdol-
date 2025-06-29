import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# === IMPORTY SYSTEMOWE ===
from marketplace_logic import handle_marketplace
from inventory import show_inventory
from questy import handle_quest_menu
from bosses import handle_boss_battle
from nft_cards import handle_nft_display
from spell_crafting import handle_spell_crafting

# === KONFIGURACJA ===
API_TOKEN = 'TWOJ_TOKEN_TUTAJ'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# === MENU GŁÓWNE ===
def get_main_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🗺 Mapa", callback_data="map"),
        InlineKeyboardButton("🎒 Ekwipunek", callback_data="inventory"),
        InlineKeyboardButton("🧪 Crafting Zaklęć", callback_data="crafting"),
        InlineKeyboardButton("📜 Questy", callback_data="quests"),
        InlineKeyboardButton("👹 Bossowie", callback_data="bosses"),
        InlineKeyboardButton("🃏 Karty NFT", callback_data="nft"),
        InlineKeyboardButton("🛒 Marketplace", callback_data="market")
    )
    return keyboard

# === START KOMENDY ===
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("🌟 Witaj w świecie Firos!", reply_markup=get_main_menu())

# === CALLBACKS ===
@dp.callback_query_handler(lambda c: True)
async def handle_callbacks(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == "inventory":
        await show_inventory(callback_query)
    elif data == "market":
        await handle_marketplace(callback_query)
    elif data == "quests":
        await handle_quest_menu(callback_query)
    elif data == "bosses":
        await handle_boss_battle(callback_query)
    elif data == "nft":
        await handle_nft_display(callback_query)
    elif data == "crafting":
        await handle_spell_crafting(callback_query)
    elif data == "map":
        await callback_query.message.edit_text("🗺 Tu będzie mapa świata Firos (w przygotowaniu)...")
    else:
        await callback_query.message.edit_text("Nieznana opcja.")

# === URUCHOMIENIE BOTA ===
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
