from aiogram import types, Dispatcher
from random import choice
async def random_command(message: types.Message):
    names= ('kairat' 'vlad' 'kiril')
    random_name = choice(names)
    await message.reply(f"Случайное имя: {random_name}")
def register_handler(dp: Dispatcher):
    dp.register_message_handler(random_command, commands="myinfo")