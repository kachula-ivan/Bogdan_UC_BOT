from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

from app.filters.isAdmin import IsAdmin
from keyboartds.default import main_admin

router = Router()
flags = {"throttling_key": "default"}


@router.message(IsAdmin(), Command("admin"), flags=flags)
async def admin(message: Message):
    await message.answer("Админ панель", reply_markup=main_admin())

