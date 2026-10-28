import os
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    admin_id = int(os.getenv("ADMIN_ID", 0))

    if user_id == admin_id:
        await message.answer(
            "Здравствуйте! Этот бот сделан на коленке на вайбе навайбкожен и прочее <3 \n"
            "https://github.com/INTEL3GENT \n\n"
            "Для выключения вашего ПК напишите /shutdown"
        )
        return

    await message.answer(
        f"Не твой комп, гуляй)\n\n"
        f"Если вы настраиваете бота:\n"
        f"Чтобы авторизоваться, скопируйте ваш ID и добавьте его в файл .env <3\n\n"
        f"`{user_id}`\n\n"
        f"_(Нажмите на ID выше, чтобы быстро скопировать его)_",
        parse_mode="Markdown"
    )

@router.message(Command('shutdown'))
async def cmd_shutdown(message: types.Message):
    admin_id = int(os.getenv("ADMIN_ID", 0))
    
    if message.from_user.id != admin_id:
        await message.answer("Не твой компег")
        return

    await message.answer("Завершение работы Windows...")
    os.system("shutdown /s /t 0")
