import asyncio
import logging
import json
from aiogram import Bot, Dispatcher, Router
from handlers import command_messages, user_messages
from middlewares.middleware import ThrottlingMiddleware

with open('config.json') as config_file:
    config = json.load(config_file)

API_TOKEN = config['BOT_API_TOKEN']
dp = Dispatcher()
router = Router()

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN)
    dp.include_routers(
        command_messages.router,
        user_messages.router
    )
    dp.message.middleware(ThrottlingMiddleware())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())