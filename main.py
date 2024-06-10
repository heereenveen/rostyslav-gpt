import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import json
import time

with open('config.json') as config_file:
    config = json.load(config_file)

API_TOKEN = config['BOT_API_TOKEN']

dp = Dispatcher()

def save_last_message(message):
    with open("last_message.txt", "w") as file:
        file.write(message)

def read_answer_message():
    with open("answer_message.txt", "r") as file:
        return file.read().strip()

@dp.message(CommandStart())
async def starting(message: types.Message):
    await message.answer(text="Вас вітає Rostyslav-GPT! 🖖")

@dp.message()
async def answer_message(message: types.Message):
    user_message = message.text
    logging.info(F" Received message: '{user_message}', from user: {message.from_user.id}")
    save_last_message(user_message)

    os.system("py gpt.py")
    while not os.path.exists("answer_message.txt"):
        time.sleep(0.1)

    gpt_answer = read_answer_message()
    logging.info(F" Replied: '{gpt_answer}', to user: {message.from_user.id}")
    await message.reply(text=gpt_answer)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())