from aiogram import Router, F
from aiogram.types import Message

from app.filters.isActive import IsActive
from app.filters.isAdmin import IsAdmin
from database.commands import db
from keyboartds.inline import price_list

router = Router()
flags = {"throttling_key": "default"}


@router.message(F.text.startswith('📝📋 Регистрация 🖋️🔒'), flags=flags)
async def register(message: Message):
    await message.answer('Админ для регистрации: @BogdanPubg')


@router.message(IsActive(), F.text.startswith('💰 Прайс лист 📜'), flags=flags)
@router.message(IsAdmin(), F.text.startswith('📜 Прайс лист'), flags=flags)
async def register(message: Message):
    await message.answer('Выбери пак:', reply_markup=price_list(await db.get_prices()))
