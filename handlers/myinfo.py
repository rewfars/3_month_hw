from aiogram import types, Dispatcher
async def myinfo_command(message: types.Message):
    user_info = (
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш username: @{message.from_user.username if message.from_user.username else 'не указан'}"
    )
    await message.reply(user_info)

def register_handler(dp: Dispatcher):
    dp.register_message_handler(myinfo_command, commands="myinfo")