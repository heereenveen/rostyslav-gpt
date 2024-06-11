from aiogram import Router, types
from aiogram.filters import CommandStart
from middlewares.middleware import ThrottlingMiddleware

router = Router()

router.message.middleware(ThrottlingMiddleware())

@router.message(CommandStart())
async def starting(message: types.Message):
    await message.answer(text="Вас вітає Rostyslav-GPT! 🖖")