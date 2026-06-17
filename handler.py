from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

@router.message(Command("start"))
async def first_message(message: Message):
    await message.answer("""\n
Привет! Я бот-инструмент для быстрого кодирования/декодирования текста
Надеюсь что я буду помогать
""")