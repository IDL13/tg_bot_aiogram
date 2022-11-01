import os
import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor
from aiogram.types import BotCommand, BotCommandScopeDefault

load_dotenv()
API_KEY = os.getenv('API_KEY')
loop = asyncio.new_event_loop()
bot = Bot(API_KEY, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
	from handler import dp
	executor.start_polling(dp, loop=loop)