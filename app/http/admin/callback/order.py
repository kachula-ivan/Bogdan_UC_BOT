from datetime import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery

from database.commands import db
from database.migrations.orders import Order, STATUS_COMPLETED, STATUS_DECLINED
from keyboartds.inline import decline_order_accept, new_order, empty

router = Router()


@router.callback_query(F.data.startswith('order_completed:'))
async def order_completed(call: CallbackQuery):
    try:
        order_id = call.data[len('order_completed:'):]
        order = await db.get_order(int(order_id))

        await db.update_model(Order, int(order_id), {'status': STATUS_COMPLETED, 'paid_at': datetime.now()})
        await db.add_stats('uc', order.uc)
        await db.add_stats('orders', 1)
        await db.add_stats('sum', float(order.sum))

        await call.message.edit_text(f'✅ Заказ #<code>{order_id}</code>. <code>{order.pubg_id}</code> - {order.uc} UC')

        try:
            await call.bot.send_message(order.user.telegram_id, f'✅ Заказ #<code>{order_id}</code> подтверждён')
        except:
            pass
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')


@router.callback_query(F.data.startswith('order_decline:'))
async def order_decline(call: CallbackQuery):
    try:
        order_id = call.data[len('order_decline:'):]

        await call.message.edit_text('Точно?')
        await call.message.edit_reply_markup(str(call.message.message_id), decline_order_accept(order_id))
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')


@router.callback_query(F.data.startswith('decline_order:'))
async def decline_register(call: CallbackQuery):
    try:
        order_id = call.data[len('decline_order:'):]

        order = await db.get_order(int(order_id))

        await db.update_model(Order, int(order_id), {'status': STATUS_DECLINED})

        try:
            await call.bot.send_message(int(order.user.telegram_id), f'❌ Заказ: #<code>{order_id}</code> был отменен')
        except:
            pass

        await call.message.edit_text(f'❌ Отказано. Заказ #{order_id}. <code>{order.pubg_id}</code> - {order.uc} UC')
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')


@router.callback_query(F.data.startswith('accept_order:'))
async def accept_register(call: CallbackQuery):
    try:
        order_id = call.data[len('accept_order:'):]
        order = await db.get_model(Order, int(order_id))

        await call.message.edit_text(f'🪪 Новый шанс заказа #<code>{order_id}</code>: \n'
                                     f'<code>{order.pubg_id}</code> - pubg_id\n'
                                     f'<code>{order.uc}</code> - uc'),

        await call.message.edit_reply_markup(str(call.message.message_id), new_order(order_id))
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')
