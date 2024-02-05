from re import search

from aiogram import Router, F
from aiogram.types import Message

from app.filters.isActive import IsActive
from database.commands import db
from keyboartds.default import main
from keyboartds.inline import price_list

router = Router()
flags = {"throttling_key": "default"}


@router.message(F.text.startswith('📝📋 Регистрация 🖋️🔒'), flags=flags)
async def register(message: Message):
    await message.answer('Админ для регистрации: @BogdanPubg')


@router.message(IsActive(), F.text.startswith('💰 Прайс лист 📜'), flags=flags)
async def register(message: Message):
    await message.answer('Выбери пак:', reply_markup=price_list(await db.get_prices()))


@router.message(IsActive(), F.text.startswith('📊 Статистика'), flags=flags)
async def stats(message: Message):
    user = await db.get_user(message.from_user.id)
    orders = await db.get_orders(user.id)

    await message.answer(f'📊 Статистика\n\nСделано: <code>{len(orders)}</code> заказов\nКуплено: <code>'
                         f'{sum(int(search(r'\d+', order.uc).group()) for order in orders)}</code> UC\n',
                         reply_markup=main())
