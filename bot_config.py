from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage



token = dotenv_values('.env')['token']
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)