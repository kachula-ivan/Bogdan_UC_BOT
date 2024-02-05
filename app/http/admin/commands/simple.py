from aiogram import Router, F
from aiogram.types import Message

from app.filters.isAdmin import IsAdmin
from database.commands import db
from keyboartds.default import main_admin
from keyboartds.inline import price_list_delete

router = Router()
flags = {"throttling_key": "default"}


@router.message(IsAdmin(), F.text.startswith('📜 Прайс лист'), flags=flags)
async def price_list(message: Message):
    await message.answer('❌ Выбери пак чтобы удалить:', reply_markup=price_list_delete(await db.get_prices()))


@router.message(IsAdmin(), F.text.startswith('Статистика бота 📊'), flags=flags)
async def price_list(message: Message):
    stats = await db.get_stats()
    await message.answer(f'📊 Статистика бота\n\nПользователей: <code>{stats.users}</code>\n'
                         f'Всех заказов: <code>{stats.orders}</code>\n'
                         f'Продано UC: <code>{stats.uc}</code>\n'
                         f'Заработано: <code>{stats.sum}</code> $', reply_markup=main_admin())
