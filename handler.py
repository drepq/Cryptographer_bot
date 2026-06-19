from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types

router = Router()


kb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="encode Base64"),
      types.KeyboardButton(text="decode Base64")]
      ], resize_keyboard=True)


@router.message(Command("start"))
async def first_message(message: Message):
    await message.answer("""\n
Привет! Я бот-инструмент для быстрого кодирования/декодирования текста
Надеюсь что я буду помогать
""", reply_markup=kb)