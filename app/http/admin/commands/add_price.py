from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from app.filters.isAdmin import IsAdmin
from app.http.admin.states.states import AddPrice
from database.commands import db
from database.migrations.price import Price
from keyboartds.default import main_admin

router = Router()
router.message.filter(IsAdmin())

flags = {"throttling_key": "default"}


@router.message(F.text.startswith('💰 Добавить прайс'), flags=flags)
async def uc(message: Message, state: FSMContext):
    await state.set_state(AddPrice.uc)
    await message.answer("Количество UC:", reply_markup=ReplyKeyboardRemove())


@router.message(AddPrice.uc, flags=flags)
async def sum_type(message: Message, state: FSMContext):
    await state.update_data(UC=message.text)
    await state.set_state(AddPrice.sum)
    await message.answer("Цена (Пример: <code>1.7</code>):", reply_markup=ReplyKeyboardRemove())


@router.message(AddPrice.sum, flags=flags)
async def check(message: Message, state: FSMContext):
    try:
        data = await state.get_data()

        price = await db.add_model(Price, {
            'uc': data['UC'],
            'sum': float(message.text),
            'currency': '$',
        })

        await message.answer(f'Теперь этот пак в продаже.\nuc: {price.uc}\nsum: {price.sum}', reply_markup=main_admin())
    except:
        await message.answer(f'❌ Цена должна быть числом! Число через точку', reply_markup=main_admin())
    await state.clear()

