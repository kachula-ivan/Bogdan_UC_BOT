from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from app.filters.isAdmin import IsAdmin
from app.http.admin.states.states import Mailing
from database.commands import db
from keyboartds.default import main_admin
from keyboartds.inline import mailing_send, empty

router = Router()
router.message.filter(IsAdmin())

flags = {"throttling_key": "default"}


@router.message(F.text.startswith('📬 Рассылка'), flags=flags)
async def type_message(message: Message, state: FSMContext):
    await state.set_state(Mailing.accept)
    await message.answer("Сообщение:", reply_markup=ReplyKeyboardRemove())


@router.message(Mailing.accept, flags=flags)
async def accept(message: Message, state: FSMContext):
    await state.update_data(MESSAGE=message.text)
    await state.set_state(Mailing.send)
    await message.answer('Отправить это сообщение всем?:', reply_markup=mailing_send())


@router.callback_query(Mailing.send, F.data.startswith('mailing_send:'), flags=flags)
async def send(call: CallbackQuery, state: FSMContext):
    status = call.data[len('mailing_send:'):]

    if status == 'accept':
        users = await db.get_users()
        data = await state.get_data()

        for user in users:
            try:
                await call.bot.send_message(user.telegram_id, data['MESSAGE'])
            except:
                pass

        await call.message.answer('Рассылка выполнена')
    else:
        await call.message.edit_reply_markup(call.inline_message_id, reply_markup=empty())
        await call.message.answer('Рассылка отменена', reply_markup=main_admin())

    await state.clear()
