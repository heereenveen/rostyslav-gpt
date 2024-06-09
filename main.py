import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


import json

with open('config.json') as config_file:
    config = json.load(config_file)

API_TOKEN = config['BOT_API_TOKEN']


dp = Dispatcher()

@dp.message(CommandStart())
async def starting(message: types.Message):
    await message.answer(text="Вас вітає Rostyslav-GPT! 🖖")

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())