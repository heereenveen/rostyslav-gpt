from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def starting(message: types.Message):
    await message.answer(text="Вас вітає Rostyslav-GPT! 🖖")