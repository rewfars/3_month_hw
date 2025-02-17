from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from bot_config import bot

async def hours_callback(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Время раюоты с 10 до 10')
    await callback.answer()

def register_handler(dp: Dispatcher):
    dp.register_callback_query_handler(hours_callback, lambda call: call.data == "hours")