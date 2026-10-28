import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.commands import router as commands_router

load_dotenv()

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))

    dp.include_router(commands_router)

    print("Запущен (надеюсь работает) Ctrl + C для остановки")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
