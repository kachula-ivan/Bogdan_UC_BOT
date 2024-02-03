from aiogram import Router, F
from aiogram.types import Message

router = Router()
flags = {"throttling_key": "default"}


@router.message(F.text.startswith('📝📋 Регистрация 🖋️🔒'), flags=flags)
async def register(message: Message):
    await message.answer('Админ для регистрации: @BogdanPubg')
