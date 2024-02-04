from aiogram import Router, F
from aiogram.types import Message

from app.filters.isActive import IsActive
from database.commands import db
from keyboartds.inline import profile

router = Router()
router.message.filter(IsActive())

flags = {"throttling_key": "default"}


@router.message(F.text.startswith('👤 Аккаунт'), flags=flags)
async def register(message: Message):
    user = await db.get_user(message.from_user.id)

    await message.answer(f'📱 Мой кабинет\n\n'
                         f'🔑 Мой ID: {user.id}\n'
                         f'🔑 PUBG ID: {user.pubg_id}\n\n'
                         f'👤 Первый вход: {str(user.created_at)[:16]}\n',
                         reply_markup=profile())
