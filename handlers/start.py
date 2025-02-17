from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
async def start_command(message: types.Message):
    user = message.from_user
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Наш адрес", callback_data="adress")],
        [types.InlineKeyboardButton(text="Режим работы", callback_data="hours")],
        [types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
        [types.InlineKeyboardButton(text="Инстаграм", url="https://geeks.kg")]]
    )

    await message.answer(f"Hello , {user.first_name}", reply_markup=kb)
async def about_us_handler(callback: CallbackQuery):
    await callback.answer("наш адрес", show_alert=True)
def register_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")