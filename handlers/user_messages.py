import logging, os, time
from aiogram import Router, types
from persistence import bot_messages

router = Router()

@router.message()
async def answer_message(message: types.Message):
    user_message = message.text
    logging.info(F" Received message: '{user_message}', from user: {message.from_user.id}")
    bot_messages.save_last_message(user_message)

    os.system("py gpt.py")
    while not os.path.exists("answer_message.txt"):
        time.sleep(0.1)

    gpt_answer = bot_messages.read_answer_message()
    logging.info(F" Replied: '{gpt_answer}', to user: {message.from_user.id}")
    await message.reply(text=gpt_answer)