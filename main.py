from dotenv import load_dotenv
import os
from aiogram import Dispatcher, Bot
from aiogram.types import message
import asyncio
from handler import router


load_dotenv()
API_TOKEN = os.environ.get("API_TOKEN")

dp = Dispatcher()


async def main():
    bot = Bot(token=API_TOKEN)
    print("Bot started")
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        print("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())