from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
import base64

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
@router.message(F.text.lower() == "encode base64")
async def encode_base64(message: Message):
    text = message.text
    encode_text = base64.b64encode(text.encode("utf-8")).decode('utf-8')
    await message.answer(encode_text)

@router.message(F.text.lower() == "decode base64")
async def decode_base64(message: Message):
    text = message.text
    decode_text = base64.b64decode(text).decode('utf-8',  errors='ignore')
    await message.answer(decode_text)