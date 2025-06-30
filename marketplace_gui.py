from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from marketplace_logic import (
    list_market_items,
    purchase_item,
    add_item_to_market,
    get_user_inventory
)

def register_marketplace_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["marketplace"])
    async def open_market(msg: types.Message):
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("🛒 Przeglądaj rynek", callback_data="market_browse"))
        keyboard.add(InlineKeyboardButton("➕ Wystaw przedmiot", callback_data="market_sell"))
        keyboard.add(InlineKeyboardButton("❌ Zamknij", callback_data="market_close"))
        await msg.answer("🏪 *Marketplace NFT i Ekwipunku*", parse_mode="Markdown", reply_markup=keyboard)

    @dp.callback_query_handler(lambda c: c.data == "market_browse")
    async def browse_market(call: types.CallbackQuery):
        items = list_market_items()
        if not items:
            await call.message.edit_text("🪙 Rynek jest pusty.")
        else:
            formatted = "\n".join(items)
            await call.message.edit_text(f"🛒 **Dostępne przedmioty:**\n\n{formatted}", parse_mode="Markdown")

    @dp.callback_query_handler(lambda c: c.data == "market_sell")
    async def sell_item(call: types.CallbackQuery):
        user_id = str(call.from_user.id)
        inventory = get_user_inventory(user_id)["items"]
        if not inventory:
            await call.message.edit_text("📦 Nie masz nic do sprzedaży.")
            return

        # Dla uproszczenia – wystaw pierwszy przedmiot
        item = inventory[0]
        price = 1.0  # domyślna cena
        add_item_to_market(user_id, item, price)
        await call.message.edit_text(f"✅ Wystawiono {item} za {price} TON.")

    @dp.callback_query_handler(lambda c: c.data == "market_close")
    async def close_market(call: types.CallbackQuery):
        await call.message.edit_text("❌ Zamknięto rynek.")
