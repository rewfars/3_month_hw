from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from bot_config import bot


async def adress_callback(callback: CallbackQuery):

    await bot.send_message(callback.from_user.id, 'наш адрес Ибраимова 103')
    await callback.answer()

def register_handler(dp: Dispatcher):
    dp.register_callback_query_handler(adress_callback, lambda call: call.data == "adress")