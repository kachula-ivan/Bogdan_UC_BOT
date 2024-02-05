from aiogram import F, Router
from aiogram.types import CallbackQuery

from database.commands import db
from database.migrations.price import Price
from keyboartds.inline import price_list_destroy as kb_destroy, price_list_delete as kb_delete

router = Router()


@router.callback_query(F.data.startswith('price_delete:'))
async def price_list_delete(call: CallbackQuery):
    price_id = call.data[len('price_delete:'):]
    price = await db.get_model(Price, int(price_id))

    await call.message.edit_text(f'Удалить прайс? {price.uc} UC - {price.sum} $')
    await call.message.edit_reply_markup(call.inline_message_id, reply_markup=kb_destroy(price))


@router.callback_query(F.data.startswith('price_destroy:'))
async def price_list_destroy(call: CallbackQuery):
    price_id = call.data[len('price_destroy:'):]
    price = await db.get_model(Price, int(price_id))
    await price.delete()

    await price_destroy_cancel(call)


@router.callback_query(F.data.startswith('price_destroy_cancel'))
async def price_destroy_cancel(call: CallbackQuery):
    await call.message.edit_text('❌ Выбери пак чтобы удалить:')
    await call.message.edit_reply_markup(call.inline_message_id, reply_markup=kb_delete(await db.get_prices()))
