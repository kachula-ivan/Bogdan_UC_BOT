from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.http.client.states.states import SetPubgId
from database.commands import db
from keyboartds.default import main
from aiogram.types import ReplyKeyboardRemove

router = Router()


@router.callback_query(F.data.startswith('set_pubg_id'))
async def enter_pubg_id(call: CallbackQuery, state: FSMContext):
    await state.set_state(SetPubgId.validate)
    await call.message.delete()
    await call.message.answer('Введите PUBG ID', reply_markup=ReplyKeyboardRemove())


@router.message(SetPubgId.validate)
async def password(message: Message, state: FSMContext):
    telegram_id = message.from_user.id

    if message.text.isdigit() and int(message.text) >= 9999:
        await db.update_user(int(telegram_id), {'pubg_id': int(message.text)})

        await message.answer('✅ PUBG ID успешно установлен!', reply_markup=main())
    else:
        await message.answer('❌ Не корректные данные!', reply_markup=main())
    await state.clear()

