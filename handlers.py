from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("начнем"))
async def cmd_start(message: Message):
    await message.answer("Привет! Это бот для предзаказа шаурмы 🍔.")
