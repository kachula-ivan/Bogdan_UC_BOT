import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import config
from app.filters.isActive import IsActive
from app.http.client.states.states import Order as OrderStates
from database.commands import db
from database.migrations.orders import Order, STATUS_CREATE
from database.migrations.price import Price
from keyboartds.default import main, one_time_default_kb
from aiogram.types import ReplyKeyboardRemove

from app.http.client.commands.start import bot
from keyboartds.inline import new_order

router = Router()
router.message.filter(IsActive())


@router.callback_query(F.data.startswith('price:'))
async def pack(call: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.pubg_id)

    telegram_id = call.from_user.id
    user = await db.get_user(int(telegram_id))

    price_id = call.data[len('price:'):]
    await state.update_data(PRICE_ID=price_id)

    await call.message.delete()

    if not (user.pubg_id is None) and int(user.pubg_id) >= 9999:
        await call.message.answer('Введите PUBG ID, или выбери из сохраненных:', reply_markup=one_time_default_kb(user.pubg_id))
    else:
        await call.message.answer('Введите PUBG ID:', reply_markup=ReplyKeyboardRemove())


@router.message(OrderStates.pubg_id)
async def type_pubg_id(message: Message, state: FSMContext):
    pubg_id = message.text

    if pubg_id.isdigit() and int(pubg_id) >= 9999:
        data = await state.get_data()
        telegram_id = message.from_user.id

        user = await db.get_user(int(telegram_id))
        price = await db.get_model(Price, int(data['PRICE_ID']))

        if user.pubg_id is None:
            await db.update_user(int(telegram_id), {'pubg_id': int(pubg_id)})

        order = await db.add_model(Order, {
            'status': STATUS_CREATE,
            'uc': price.uc,
            'sum': int(price.sum),
            'pubg_id': int(pubg_id),
            'created_at': datetime.datetime.now(),
            'user_id': user.id,
        })

        await bot.send_message(config.CHAT_TELEGRAM_ID, (f'🪪 Заказ #<code>{order.id}</code>: \n'
                                                         f'<code>{order.pubg_id}</code> - pubg_id\n'
                                                         f'<code>{order.uc}</code> - uc'),
                               reply_markup=new_order(order.id))

        await message.answer('✅ Заказ успешно оформлен!', reply_markup=main())
    else:
        await message.answer('❌ Не корректные данные!', reply_markup=main())

    await state.clear()
